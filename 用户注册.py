#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import hashlib
connection=sqlite3.connect('main.db')
cursor=connection.cursor()

#对密码进行加密
import hashlib
import bcrypt
paswd1='$密码'
paswd2=hashlib.sha512(paswd1.encode("utf-8")).hexdigest()
hash = bcrypt.hashpw(paswd2.encode("utf-8"), bcrypt.gensalt(11))
insert_sql="insert into userinfo (name,passwd,email) values (?,?,?)"# ? 为占位符
cursor.execute(insert_sql,('$username',hash,'$email'))
connection.commit()
connection.close()
#比较方法
def pascom():
    if bcrypt.checkpw(paswd2.encode("utf-8"), hash) ==True:
        print('ok')
#        return('ok')
    else:
        print('not ok')
#        print('not ok')
pascom()