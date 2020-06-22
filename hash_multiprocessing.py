#! /usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import os
import multiprocessing

# #计算文件或字符串的哈希值
def get_md5(file_path,return_dict):
    print()
    with open(file_path, 'rb') as f:
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
        md5 = str(hash_code).lower()
        return_dict['md5']= md5

def get_sha1(file_path,return_dict):
    f = open(file_path, 'rb')
    with open(file_path, 'rb') as f:
        sha1_obj = hashlib.sha1()
        while True:
            d = f.read(8096)
            if not d:
                break
            sha1_obj.update(d)
        hash_code = sha1_obj.hexdigest()
        sha1 = str(hash_code).lower()
        return_dict['sha1'] = sha1

def get_sha256(file_path,return_dict):
    with open(file_path, 'rb') as f:
        sha256_obj = hashlib.sha256()
        while True:
            d = f.read(8096)
            if not d:
                break
            sha256_obj.update(d)
        hash_code = sha256_obj.hexdigest()
        sha256 = str(hash_code).lower()
        return_dict['sha256'] = sha256

#为了方便，写成了循环

while True:
    file_path = input('''请输入目标文件绝对路径: \n''')
    if file_path.strip().lower() == 'jiaqiong':
        user_input = input('please input characters:')
        print('md5: ' + hashlib.md5(user_input.encode('utf-8')).hexdigest())
        print('sha1: ' + hashlib.sha1(user_input.encode('utf-8')).hexdigest())
        print('sha256: ' + hashlib.sha256(user_input.encode('utf-8')).hexdigest())
    else:
        if bool(os.path.exists(file_path)) == True:
            manager = multiprocessing.Manager()
            return_dict = manager.dict()
            start = time.time()
            print('正在计算中，请稍后......')

            # 任务本身是CPU密集型，多进程很难带来性能提升，就当熟悉process的方法了
            p1 = multiprocessing.Process(target=get_md5, args=(file_path,return_dict))
            p2 = multiprocessing.Process(target=get_sha1, args=(file_path,return_dict))
            p3 = multiprocessing.Process(target=get_sha256, args=(file_path,return_dict))
            p1.start()
            p2.start()
            p3.start()
            p1.join()
            p2.join()
            p3.join()
            md5_value = return_dict['md5']
            sha1_value = return_dict['sha1']
            sha256_value = return_dict['sha256']
            print('计算完成!')
            end = time.time()
            print('文件路径：' + file_path)
            # 根据文件大小给出合适字节单位
            if 0 < os.path.getsize(file_path) < 1024:
                file_size = str(os.path.getsize(file_path))
                print('文件大小：' + file_size + 'B')
            elif 1024 <= os.path.getsize(file_path) < 1048576:
                file_size = str(round(os.path.getsize(file_path) / 1024, 2))
                print('文件大小：' + file_size + 'KB')
            elif 1048576 <= os.path.getsize(file_path) < 1073741824:
                file_size = str(round(os.path.getsize(file_path) / 1048576, 2))
                print('文件大小：' + file_size + 'MB')
            else:
                file_size = str(round(os.path.getsize(file_path) / 1073741824, 2))
                print('文件大小：' + file_size + 'GB')

            print('耗时： ' + '%.3f' % (end - start) + ' 秒')

            print('md5: ' + return_dict['md5'])
            print('sha1: ' + return_dict['sha1'])
            print('sha256: ' + return_dict['sha256'])

        else:
            print('sorry，文件路径有误，请重新核对')




