#!/usr/bin/env python

import time
import requests
import base64


r=requests.get('https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt')
#time.strftime("%Y%m%d%H%M%S",time.localtime())
newtime=time.strftime("%Y%m%d%H%M%S",time.localtime())
f=open(r"D:\%sgfw.txt" % newtime,'w')
f.write(str(base64.b64decode(r.content),encoding='utf-8'))
f.close()
print('写入完毕')