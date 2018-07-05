import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aqua.settings") 

import django
django.setup()
from studio.models import contamination 
f = open('experiment.csv')
print (u"读取文件结束,开始导入!")
WorkList = []
next(f) #将文件标记移到下一行
y = 0

for line in f:
    row = line.replace('"','') #将字典中的"替换空
    row = row.split(';') #按;对字符串进行切片
    y = y + 1
    WorkList.append(contamination(date=row[0],A_Tem=row[1],O1_Tem=row[2],O2_Tem=row[3],O3_Tem=row[4],O4_Tem=row[5],Cf_Tem=row[6],Ef_Tem=row[7],A_pH=row[8],O1_pH=row[9],O2_pH=row[10],O3_pH=row[11],O4_pH=row[12],Cf_pH=row[13],Ef_pH=row[14],A_Do=row[15],O1_Do=row[16],O2_Do=row[17],O3_Do=row[18],O4_Do=row[19],Cf_Do=row[20],Ef_Do=row[21],
    A_COD=row[22],O1_COD=row[23],O2_COD=row[24],O3_COD=row[25],O4_COD=row[26],Cf_COD=row[27],Ef_COD=row[28],A_NH4=row[29],O1_NH4=row[30],O2_NH4=row[31],O3_NH4=row[32],O4_NH4=row[33],Cf_NH4=row[34],Ef_NH4=row[35],A_NO2=row[36],O1_NO2=row[37],O2_NO2=row[38],O3_NO2=row[39],O4_NO2=row[40],Cf_NO2=row[41],Ef_NO2=row[42],A_NO3=row[43],O1_NO3=row[44],O2_NO3=row[45],O3_NO3=row[46],O4_NO3=row[47],Cf_NO3=row[48],Ef_NO3=row[49],
    A_MLSS=row[50],O1_MLSS=row[51],O2_MLSS=row[52],O3_MLSS=row[53],O4_MLSS=row[54],Cf_MLSS=row[55],Ef_MLSS=row[56]))
contamination.objects.bulk_create(WorkList)

WorkList = []
print (u"成功导入数据"+str(y)+"条")
f.close() 