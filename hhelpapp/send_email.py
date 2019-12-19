import smtplib
from email.mime.text import MIMEText
import random

def send_email(receiver, vercode):
    mailserver = "smtp.163.com"  #邮箱服务器地址
    username_send = 'lijingxin02@163.com'  #邮箱用户名
    password = '163shouquan'   #邮箱密码：需要使用授权码
    content = "您的验证码是：" + vercode
    mail = MIMEText(content)
    mail['Subject'] = 'hhelp验证码'    # 邮件主题
    mail['From'] = username_send  #发件人
    mail['To'] = receiver
    smtp = smtplib.SMTP(mailserver, port=25) # 连接邮箱服务器，smtp的端口号是25
    # smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
    smtp.login(username_send, password)  #登录邮箱
    smtp.sendmail(username_send, receiver, mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
    smtp.quit() # 发送完毕后退出smtp
    return 0


def createvercode():
    res = ''
    res = res + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    return res


def createtoken():
    return "token"

if __name__ == '__main__':
    res = createvercode()
    print(res)