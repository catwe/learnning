# 调用邮件库
import smtplib

# 发邮件的文本库
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = 'smtp.163.com'

#发邮件的地址
sender = 'weichen_vip_top@163.com'

#发邮件密码(授权码)
passwd = 'wangcong123'



#设置发送的内容
message = '邮件测试'
#转换成邮件文本
msg = MIMEText(message)
#标题
msg['Subject'] = 'Python邮件访问'
#发送者
msg['From'] = sender



# 创建STMP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
#登陆邮箱
mailServer.login(sender,passwd)
# 发送邮件
# mailServer.sendmail(sender,['1697126697@qq.com'],msg.as_string())

for x in range(5):
	mailServer.sendmail(sender, ['1697126697@qq.com'], msg.as_string())
#退出邮件
mailServer.quit()