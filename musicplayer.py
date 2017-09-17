#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
#音乐文件存放路径

def updatemusiclist(dir_path):
    f_list=os.listdir(dir_path)
#    print(f_list)
    for i in f_list:
        if os.path.splitext(i)[1].lower() =='.mp3':
            print(i)


dir_path = input('Please choice you music dir: ')
os.chdir(dir_path)
updatemusiclist(dir_path)







