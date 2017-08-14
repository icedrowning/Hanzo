#! /usr/bin/env python
# -*- coding: utf-8 -*-
#导入你需要的库
import sqlite3
import os
print('当前路径为：'+ os.getcwd())
#建立与数据库的连接，如果当前路径没有该数据库则会创建
connection=sqlite3.connect('userinfo.db')
#创建数据游标
cursor=connection.cursor()
#执行一些SQL操作
sql='''create table userinfomation(
id  integer primary key  unique not null,
nickname text,
passwd text,
email text,
image text)'''
cursor.execute(sql)
#提交所做的修改，使修改永久保留
connection.commit()
#完成时关闭链接
connection.close()