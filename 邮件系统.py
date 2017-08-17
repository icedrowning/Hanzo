#! /usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='icedrowning@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
#这个后面会配置
my_user='1003000644@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
def mail():
    ret=True
    try:
        msg=MIMEText('''
        尊敬的用户您好~
            万分感谢您注册成为圣光小笼包会员~
            每逢网站新迭代上线，我们将通过邮件将新增功能与改动介绍给您！
            本封邮件是系统自动发出，请勿回复哦。
            若不想再继续接受本站邮件请联系本站管理员，虽然万分伤心QAQ但我们不会打扰您的~
        ''','plain','utf-8')
        msg['From']=formataddr(["sender",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["user",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="欢迎光临圣光小笼包(´・ω・`)" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"naruto123456")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed