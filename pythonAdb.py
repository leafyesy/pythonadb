# -*- coding: utf-8 -*-
import subprocess

orderListDevices='adb devices' #获取连接设备
orderScreenShotToPC = 'adb pull /sdcard/screenshot.png ~/Documents/python/pythonadbdemo/screenshot.png'
orderScreenShotToPhone = 'adb shell /system/bin/screencap -p /sdcard/screenshot.png'


pi= subprocess.Popen(orderScreenShotToPC,shell=True,stdout=subprocess.PIPE)

print pi.stdout.read()#打印结果