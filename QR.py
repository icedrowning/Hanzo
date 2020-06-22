#! /usr/bin/env python
# -*- coding: utf-8 -*-

#https://qr.alipay.com/a7x07596sxdqgbc7saenof1

from MyQR import myqr
import os
#醉了，这个库不支持中文
version, level, qr_name = myqr.run(
	'welcome jiaqiong',
    version=1,
    level='L',
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name='welcome.jpg',
    save_dir=os.getcwd()
	)