#! /usr/bin/env python
# -*- coding: utf-8 -*-
#导入你需要的库
import sqlite3
import os
print('数据库当前路径为：'+ os.getcwd())
#建立与数据库的连接，如果当前路径没有该数据库则会创建
connection=sqlite3.connect('main.db')
#创建数据游标
cursor=connection.cursor()
#执行一些SQL操作
sql='''create table userinfo(
id  integer primary key  unique not null,
name text,
passwd text,
sex text CHECK(sex=='M' OR sex=='F' OR sex is NULL),
signature text,
email text,
image text,
sendemail,text CHECK(sendemail=='0' OR sendemail=='1'),
isdelete text CHECK(isdelete=='0' OR isdelete=='1'),
Reserved1 text,
Reserved2 text,
Reserved3 text)'''
cursor.execute(sql)
#提交所做的修改，使修改永久保留
connection.commit()

#创建对话表

sql='''create table msg(
fromid test,
toid test,
content,
fire test,
TIME DATE )'''
cursor.execute(sql)
connection.commit()


#完成时关闭链接
connection.close()