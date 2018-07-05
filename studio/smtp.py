
import os  
import socket  
import time  
import smtplib    
from email.mime.text import MIMEText  
import pandas
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

      excel_path = './media/data.xlsx'
      df = pandas.read_excel(excel_path,  sheet_name='Sheet1')  
      old_width = pandas.get_option('display.max_colwidth')  
      pandas.set_option('display.max_colwidth', -1)  
      df.to_html('./media/data.html',escape=False,index=False,sparsify=True,border=0,index_names=False,header=True)
      pandas.set_option('display.max_colwidth', old_width) 
      htmlf=open('./media/data.html','r',encoding="utf-8")
      htmlcont=htmlf.read()
      send_mail(mailto_list,"实时监控预警",htmlcont)

         
 
