#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time
caps = DesiredCapabilities.CHROME
#as per latest docs
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(desired_capabilities=caps)
time.sleep(3)
driver.get('https://www.jianshu.com/p/81ce4bf0d0c0')
#driver.get('https://www.baidu.com/')
##########################################
#to be done 后面找时间慢慢加吧：
#1.代码重构与封装
#2.找原因，为什么performance_log与F12控制台中的请求时间，请求大小会有极细微差异
#3.按照网上的"竞品"参考（https://www.webfx.com/blog/web-design/free-website-speed-testing/）看本脚本的统计需要加什么东西
#4.添加每个请求的状态码，对请求失败的做特殊展示
#5.添加页面加载完成的时间统计
#6.弄清楚window.performance.timing与本脚本中performance_log的异同
#7.代码添加注释
###########################################

performance_log=driver.get_log('performance')

##########################################################
#最终生成的记录，暂定是map形式，包括用于标记记录在原始log中的行号：seqnumber；requestID；请求类型：type；发送请求前的时间：time_before；请求接收完成的时间：time_after；请求接收时间与发送时间的时间差：time_abs
##########################################################

#a在这里用于帮助标记seqnumber
a=0

final_list=[]
mini_list=[]
for i in performance_log:
    try:
        a+=1
        if json.loads(i['message'])['message']['method']=='Network.requestWillBeSent':
            #print(json.loads(i['message'])['message']['params']['requestId'])
            unit_map=dict(seqnumber=a,requestID=json.loads(i['message'])['message']['params']['requestId'],type=None,size=None,time_before=None,time_after=None,time_abs=None)
            final_list.append(unit_map)
        #这里的逻辑应该是，如果存在Network.loadingFinished就先用这个，没有的情况下用Network.responseReceived，再没有的就算了
        elif json.loads(i['message'])['message']['method']=='Network.responseReceived':
            #这里应该可以直接更新
            #mini_list.append(dict(id=json.loads(i['message'])['message']['params']['requestId'],time_after=json.loads(str(i['timestamp']))))
            mini_list.append(dict(id=json.loads(i['message'])['message']['params']['requestId'],
                                  time_after=json.loads(str(i['timestamp'])),
                                  size=json.loads(i['message'])['message']['params']['response']['encodedDataLength']))
    except Exception as e:
        1==1

#driver.quit()

#更新字典中的剩余值
for i in final_list:
    i['type']=json.loads((performance_log[i['seqnumber']-1])['message'])['message']['params']['type']
    i['time_before']=json.loads(str((performance_log[i['seqnumber']-1])['timestamp']))

#更新time_after
for i in mini_list:
    for o in final_list:
        if o['requestID']==i['id']:
            o['time_after']=i['time_after']
            o['size']=i['size']

##这里是不是用列表推导式很方便
for i in final_list:
    if i['time_after'] != None:
        i['time_abs']=i['time_after']-i['time_before']



# for i in final_list:
#     if i['type'] == 'XHR':
#定义一个函数?统计每种类型的大小与数量

def diffent_type_count(type):
    count=0
    total=0
    for i in final_list:
        try:
            if i['type'] == type:
                count+=1
                total+=int(i['size'])
        except Exception as e:
            #没收到response的也统计进来吧，汇总的时候注意NoneType
            pass
    print(type +' 请求数量：' +str(count) +' 请求文件总大小：'+str(total))


set_of_typelist=(set([i['type'] for i in final_list]))
print("Content size & Requests by content type ")
for i in set_of_typelist:
    diffent_type_count(i)

for i in final_list:
    if i['type']=='Stylesheet':
        print(i)
for i in performance_log:
    print(i)