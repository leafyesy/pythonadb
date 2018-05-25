# -*- coding: utf-8 -*-

# 进入QQ好友列表 然后对好友自动点赞

import subprocess
import os,sys
import time

#print sys.argv[0]

#print os.path.dirname(__file__)#获取当前文件的目录

#phoneClickDemoF = open("phoneClickDemo.sh")
#content = phoneClickDemoF.read()

#orderScreenInfo = 'adb shell dumpsys window displays'#获取当前屏幕的主要信息
orderScreenWmSize = 'adb shell wm size'#获取屏幕的分辨率

orderScreenWm = 'adb shell wm'

wmSize = subprocess.Popen(orderScreenWmSize,shell=True,stdout=subprocess.PIPE)
wmSizeStr = wmSize.stdout.read()
xIndex = wmSizeStr.index("x")
conIndex = wmSizeStr.index(":")
screenWidth = wmSizeStr[conIndex+1:xIndex].strip()
screenHeight = wmSizeStr[xIndex+1:].strip()

print screenWidth+"x"+screenHeight#输出屏幕的宽度*高度

orderClickScreen = 'adb shell input tap '+ str(int(screenWidth)/2) +" "+ str(int(screenHeight)/3)
clickCount = 0
while clickCount<100:
	subprocess.Popen(orderClickScreen,shell = True)
	time.sleep(0.05)
	subprocess.Popen(orderClickScreen,shell = True)
	clickCount+=1
	print clickCount
	time.sleep(1)
