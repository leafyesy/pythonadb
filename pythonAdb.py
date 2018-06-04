# -*- coding: utf-8 -*-
import subprocess
import os

orderListDevices = 'adb devices'  # 获取连接设备
orderScreenShotToPC = 'adb pull /sdcard/screenshot.png ~/study/pythonadb/img/screenshot.png'
orderScreenShotToPhone = 'adb shell /system/bin/screencap -p /sdcard/screenshot.png'

# pi= subprocess.Popen(orderScreenShotToPhone,shell=True,stdout=subprocess.PIPE)
# pi= subprocess.Popen(orderScreenShotToPC,shell=True,stdout=subprocess.PIPE)
os.system('adb shell input swipe 200 300 200 300 1000')

# print pi.stdout.read()#打印结果
