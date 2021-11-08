import smtplib
from email.mime.text import MIMEText
mail_host = 'mail4.nospoofing.cn'  
sender = 'user14885233@mail4.nospoofing.cn'  
passward = '19YkkJKn0p31'
receivers = ['security@mail4.nospoofing.cn']  

message = MIMEText('content','plain','utf-8')
message['Subject'] = 'user14885233@mail4.nospoofing.cn' 
message['From'] = 'admin@mail4.nospoofing.cn <user14885233@mail4.nospoofing.cn>'  
message['To'] = receivers[0]  
# message['Bcc'] = receivers[0]

try:
    smtpObj = smtplib.SMTP(mail_host,25) 
    smtpObj.set_debuglevel(True)
    smtpObj.sendmail(sender,receivers,message.as_string()) 
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) 