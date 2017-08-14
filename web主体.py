#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello tester!'

@app.route('/index')
def hello_index():
    return 'this is index!'

if __name__ == '__main__':
    app.run()