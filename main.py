#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,request,Response
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
import os
import random
app = Flask(__name__)
@app.route('/')
def defaultpage():
    return('假装有内容，后面等index页面做好想跳到index页')

@app.route('/index/')#这个页面想法是一张背景图，然后右侧有登录区域，可以登录，没有账号点击创建账号的链接可以跳转到注册页面
def indexpage():
    return('这个页面想法是一张背景图，然后右侧有登录区域，可以登录。如果没有账号点击创建账号的链接可以跳转到注册页面')



@app.route('/register/')
def register():
    username=input('请输入用户名：')
    passwd=input('请输入密码：')
    passwd_check=input('请再次输入密码：')
    user_email = input('请输入邮箱，稍后会给该邮箱发送验证码:')
    sender_email = 'icedrowning@163.com'

    ret=True
    try:
        check_code = random.randint(100000, 999999)
        msg=MIMEText('''您的验证码是 %s''' % check_code,'plain','utf-8')
        msg['From']=formataddr(["sender",sender_email])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["user",user_email])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="欢迎注册圣光包子铺" #邮件的主题，也可以说是标题
        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(sender_email,"naruto123456")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender_email,[user_email,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    if  ret==1:
        return('发送成功，请查收邮箱')
    else:
        return('不好意思，邮件出问题了请联系本站管理员QQ575307062')



if __name__ == '__main__':
    app.run(debug=True)
#    app.run(host='0.0.0.0',port=80)


