#!/usr/local/bin/python
#coding=utf-8

import os
import json
import time
import schedule
from subprocess import call
import ctypes

#参考https://code-maven.com/display-notification-from-the-mac-command-line

#to be done
#1.自定义提示框的图标，目前是一个文件夹，有点丑
#https://developer.apple.com/design/human-interface-guidelines/macos/windows-and-views/alerts/
#2.配置文件没有大问题，但是有点傻。后面能不能换个方式
#3.交互！！！！初步方向有，在研究实现方式

#目前配置文件格式类似【{"10:00":"电话面试陈浩","11:15":"和春琳同步下拉框长度问题","21:10":"回家喂喵"}】

def timer():
    with open(r"/Users/jiaqiong/Desktop/面试.txt",'r',encoding='utf-8') as f:
        dict=json.loads(f.readlines()[0])
        for i in dict.keys():
            if i==time.strftime('%H%M',time.localtime())[:2]+':'+time.strftime('%H%M',time.localtime())[2:]:

                if os.name=='posix':
                    #三种方式都ok，各有特点，看个人喜好

                    # 调用mac通知栏
                    #cmd = 'display notification "第二个字段" with title "定时提醒的标题" subtitle "第三个字段" sound name "Submarine"'
                    #call(["osascript", "-e", cmd])

                    # 调用提示窗口
                    cmd = 'display alert "定时提醒!" message "该去%s了！！" buttons {"朕知道了"}' % dict[i]
                    call(["osascript", "-e", cmd])

                    # 调用系统事件
                    #cmd='tell app "System Events" to display dialog "该去%s了" buttons {"朕知道了"} ' % dict[i]
                    #call(["osascript", "-e", cmd])

                # windows可以用win32api.MessageBox的消息弹窗，或者直接用vbs
                if os.name == 'nt':

                    #有点丑，后面试试其他的方式吧
                    ##  Styles:
                    ##  0 : OK
                    ##  1 : OK | Cancel
                    ##  2 : Abort | Retry | Ignore
                    ##  3 : Yes | No | Cancel
                    ##  4 : Yes | No
                    ##  5 : Retry | No
                    ##  6 : Cancel | Try Again | Continue
                    ctypes.windll.user32.MessageBoxW(0, "该去%s了" % dict[i], "定时提醒", 0)





schedule.every().minute.at(":30").do(timer)


while True:
    schedule.run_pending()
    time.sleep(1)

