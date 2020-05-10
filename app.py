#! /usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import render_template
from flask import request
from flask import Response
from werkzeug.utils import secure_filename
from flask import render_template, jsonify
import json
from flask import send_from_directory

#app = Flask(__name__,static_url_path='/static/',template_folder='templates')
app=Flask(__name__)

# def return_img_stream(img_local_path):
#     """
#     工具函数:
#     获取本地图片流
#     :param img_local_path:文件单张图片的本地绝对路径
#     :return: 图片流
#     """
#     import base64
#     img_stream = ''
#     with open(img_local_path, 'r') as img_f:
#         img_stream = img_f.read()
#         img_stream = base64.b64encode(img_stream)
#     return img_stream


@app.route('/')
def index_page():
    return 'welcome to web'


# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/' + secure_filename(f.filename))
#         return ('upload success')


# @app.route('/work_time')
# def work_time(name=None):
#     return render_template('hello.html')

# #https://www.zhihu.com/question/20575288
# @app.route('/weather')
# def weather():
#     #接口
#     pass
#     return 'weather'

# @app.route('/json_format')
# #json 在线格式化
# def json_format():
#     dic = {'a': 1, 'b': 2, 'c': 3}
#     js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
#     print(js)
#     return (js)



@app.route('/user/<username>',methods=['POST'])
def show_user_profile(username):
    return request.get_data()
    #return 'User %s' % username

@app.route('/hbase/postOrderData', methods=['POST'])
def login():
    return(request.get_data())
    #return request.args.get("name")





if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
