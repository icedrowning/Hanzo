#! /usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

user_input = input('please input characters:')
print('your input is: '+ user_input)

hashmode = input('''Please select your encryption method:
a for md5
b for sha1
c for sha256: 
''')

if hashmode.strip().upper()=='A':
    print('md5: ' + hashlib.md5(user_input.encode('utf-8')).hexdigest())
elif hashmode.strip().upper()=='B':
    print('sha1: '+ hashlib.sha1(user_input.encode('utf-8')).hexdigest())
elif hashmode.strip().upper()=='C':
    print('sha256: '+ hashlib.sha256(user_input.encode('utf-8')).hexdigest())
else :
    print('QAQ invalid parameter,please try again')
