import tensorflow as tf  
import tensorlayer as tl  
import numpy as np  
import pandas as pd  
from statsmodels.tsa.tsatools import lagmat  
from sklearn.preprocessing import MinMaxScaler  
import matplotlib.pyplot as plt  
  
sess = tf.InteractiveSession()  
# 读取数据、划分数据集  
df = pd.read_csv('monthly-flows-chang-jiang-at-han.csv', engine='python',  
                 skipfooter=3, names=['YearMonth', 'WaterFlow'],  
                 parse_dates=[0], infer_datetime_format=True, header=0)  
df.YearMonth = pd.to_datetime(df.YearMonth)  
df.set_index("YearMonth", inplace=True)  
train = df.WaterFlow[:-14]  
test = df.WaterFlow[-14:]  
  
# 构造数据  
def create_dataset(dataset, timestep=1, look_back=1, look_ahead=1):  
    dataX = lagmat(dataset, maxlag=look_back, trim='both', original='ex')  
    dataY = lagmat(dataset[look_back:], maxlag=look_ahead, trim='backward', original='ex')  
    dataX = dataX.reshape(-1, timestep, dataX.shape[1])[: -(look_ahead - 1)]  
  
    return np.array(dataX), np.array(dataY[: -(look_ahead - 1)])  
  
look_back = 60  
look_ahead = 24  
scaler = MinMaxScaler(feature_range=(0, 1))  
trainstd = scaler.fit_transform(train.values.astype(float).reshape(-1, 1))  
trainX, trainY = create_dataset(trainstd, timestep=1, look_back=look_back, look_ahead=look_ahead)  
test_data = scaler.transform(df.WaterFlow['1972':'1976'].values.reshape(-1, 1)).copy()  
testX = (test_data).reshape(1, 1, look_back)  
  
# 定义placeholder  
x = tf.placeholder(tf.float32, shape=[None, 1, look_back], name='x')  
y_ = tf.placeholder(tf.float32, shape = [None, look_ahead], name='y_')  
  
# 建立模型  
network = tl.layers.InputLayer(inputs=x, name='input_layer')  
network = tl.layers.RNNLayer(network, cell_fn=tf.nn.rnn_cell.LSTMCell, cell_init_args={},  
                             n_hidden=48, initializer=tf.random_uniform_initializer(0, 0.05), n_steps=1,  
                             return_last=False, return_seq_2d=True, name='lstm_layer')  
network = tl.layers.DenseLayer(network, n_units=look_ahead, act=tf.identity, name='output_layer')  
  
# 定义损失函数  
y = network.outputs  
cost = tl.cost.mean_squared_error(y, y_, is_mean=True)  
  
# 定义优化器  
train_param = network.all_params  
train_op = tf.train.AdamOptimizer(learning_rate=0.0001, use_locking=False).minimize(cost, var_list=train_param)  
  
# 初始化参数  
tl.layers.initialize_global_variables(sess)  
  
# 列出模型信息  
network.print_layers()  
network.print_params()  
  
# 训练模型  
tl.utils.fit(sess, network, train_op, cost, trainX, trainY, x, y_,  
            batch_size=11, n_epoch=50, print_freq=10,  
            eval_train=False, tensorboard=True)  
  
# 预测  
prediction = tl.utils.predict(sess, network, testX, x, y)  
prediction = scaler.inverse_transform(prediction.reshape(-1, 1))  
  
# 绘制结果  
actual = df.WaterFlow['1977':'1978'].copy().reshape(-1, 1)  
plt.plot(prediction, label='prediction')  
plt.plot(actual, label='actual')  
plt.legend(loc='best')  
plt.show()  
  
# 保存模型  
tl.files.save_npz(network.all_params, name='model.npz')  
sess.close()