#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import hashlib
from pathlib import Path
tree_str=''

def get_md5(file_path):
    with open(file_path, 'rb') as f:
        md5_obj = hashlib.md5()
        while True:
            d = f.read(8096)
            if not d:
                break
            md5_obj.update(d)
        hash_code = md5_obj.hexdigest()
        md5 = str(hash_code).lower()
        return md5

def generate_tree(pathname, n=0):
    global tree_str
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + ' '+get_md5(pathname) +'\n'
    elif pathname.is_dir():
        tree_str += '    |' * n + '-' * 4 + \
                    str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1)

generate_tree(Path(r'/Users/jiaqiong/Desktop'))
print(tree_str)
