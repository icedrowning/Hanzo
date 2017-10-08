#! /usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import os

choice=input('''请选择计算哈希的目标：
a for characters 
b for file
\n->''')
if choice.strip().lower()=='a':
    user_input = input('please input characters:')
    print('md5: ' + hashlib.md5(user_input.encode('utf-8')).hexdigest())
    print('sha1: '+ hashlib.sha1(user_input.encode('utf-8')).hexdigest())
    print('sha256: '+ hashlib.sha256(user_input.encode('utf-8')).hexdigest())


elif choice.strip().lower()=='b':
    def get_md5(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
        return md5

    def get_sha1(file_path):
        f = open(file_path, 'rb')
        sha1_obj = hashlib.sha1()
        while True:
           d = f.read(8096)
           if not d:
               break
           sha1_obj.update(d)
        hash_code = sha1_obj.hexdigest()
        f.close()
        sha1 = str(hash_code).lower()
        return sha1

    def get_sha256(file_path):
        f = open(file_path, 'rb')
        sha256_obj = hashlib.sha256()
        while True:
            d = f.read(8096)
            if not d:
                break
            sha256_obj.update(d)
        hash_code = sha256_obj.hexdigest()
        f.close()
        sha256 = str(hash_code).lower()
        return sha256


    file_path = input('path: ')

    if bool(os.path.exists(file_path))== True:

        start = time.time()
        print('正在计算中，请稍后......')
        md5_value = get_md5(file_path)
        sha1_value = get_sha1(file_path)
        sha256_value = get_sha256(file_path)
        print('计算完成!')
        end = time.time()
        print('文件路径：'+file_path)
        #根据文件大小给出合适字节单位
        if 0 < os.path.getsize(file_path) < 1024:
            file_size = str(os.path.getsize(file_path))
            print('文件大小：' + file_size + 'B')
        elif 1024 <= os.path.getsize(file_path) < 1048576:
            file_size = str(round(os.path.getsize(file_path) / 1024, 2))
            print('文件大小：' + file_size + 'KB')
        elif 1048576 <= os.path.getsize(file_path) < 1073741824:
            file_size = str(round(os.path.getsize(file_path) / 1048576, 2))
            print('文件大小：' + file_size + 'MB')
        else :
            file_size = str(round(os.path.getsize(file_path) / 1073741824, 2))
            print('文件大小：' + file_size + 'GB')




        print('耗时： '+'%.3f' % (end-start)+' 秒')

        print('md5: '+md5_value)
        print('sha1: '+sha1_value)
        print('sha256: '+sha256_value)
    else:
        print('sorry，文件路径有误，请重新核对')

else:
    print('计算字符串请输入a，计算文件请输入b')