#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello tester!'

@app.route('/index/')
def hello_index():
    return 'this is index！！！！！！'

@app.route('/register/')
#后期需增加判断当前用户登录状态
def hello_register():
    #return(pprint.pprint(open(r'F:\project\用户守则.txt',encoding= 'UTF-8').readlines()))
    print('helloooooo')

@app.route('/user/<username>/')
def show_user_profile(username):
    # 后期需要判断用户是否存在，登录成功则跳转并提示
    return 'welcome %s' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return('111')
    else:
        return('222')

if __name__ == '__main__':
    app.run(debug=True)