import os,sys, django
sys.path.append('.../aqua_studio/')
os.environ['DJANGO_SETTINGS_MODULE'] ='aqua.settings'
django.setup()
from studio.models import contamination
  
import socket  
import time  
import smtplib    
from email.mime.text import MIMEText  
import pandas as pd
import datetime
mailto_list=["771768137@qq.com"]   
mail_host="smtp.163.com"  #设置服务器  
mail_user="13377875048"    #用户名  
mail_pass="20142014"   #口令   
mail_postfix="163.com"  #发件箱的后缀  
    
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容  
    me="AO4管家"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示  
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件  
    msg['Subject'] = sub    #设置主题  
    msg['From'] = me    
    msg['To'] = ";".join(to_list)    
    try:    
        s = smtplib.SMTP()    
        s.connect(mail_host)  #连接smtp服务器  
        s.login(mail_user,mail_pass)  #登陆服务器  
        s.sendmail(me, to_list, msg.as_string())  #发送邮件  
        s.close()    
        return True    
    except :    
        print ('error')
       
if __name__ == '__main__':  
      
      try:
        today=datetime.date.today()
        contamination_today=contamination.objects.get(date=today)
      except:
        contamination_today=contamination.objects.get(date=datetime.date(2018,1,1))
      data=pd.DataFrame([['/',contamination_today.A_pH,contamination_today.O1_pH,contamination_today.O2_pH,contamination_today.O3_pH,contamination_today.O4_pH,'/'],['/','/',contamination_today.O1_Do,contamination_today.O2_Do,contamination_today.O3_Do,contamination_today.O4_Do,'/'],[contamination_today.If_COD,contamination_today.A_COD,contamination_today.O1_COD,contamination_today.O2_COD,contamination_today.O3_COD,contamination_today.O4_COD,contamination_today.Ef_COD],[contamination_today.If_COD,contamination_today.A_COD,contamination_today.O1_COD,contamination_today.O2_COD,contamination_today.O3_COD,contamination_today.O4_COD,contamination_today.Ef_COD],[contamination_today.If_COD,contamination_today.A_COD,contamination_today.O1_COD,contamination_today.O2_COD,contamination_today.O3_COD,contamination_today.O4_COD,contamination_today.Ef_COD],[contamination_today.If_COD,contamination_today.A_COD,contamination_today.O1_COD,contamination_today.O2_COD,contamination_today.O3_COD,contamination_today.O4_COD,contamination_today.Ef_COD]],columns=['Inflluent','A','1#','2#','3#','4#','Effluent'],index=['pH','DO(mg/L)','COD(mg/L)','Ammonia(mg/L)','Nitrite(mg/L)','Nitrate(mg/L)'])
      
      df.to_html('../media/data.html',escape=False,index=False,sparsify=True,border=0,index_names=False,header=True)
      pandas.set_option('display.max_colwidth', old_width) 
      htmlf=open('../media/data.html','r',encoding="utf-8")
      htmlcont=htmlf.read()
      send_mail(mailto_list,"实时监控预警",htmlcont)

         
 
