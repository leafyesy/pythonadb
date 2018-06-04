import os
import subprocess


#1.调用截屏adb命令 获取屏幕的截图 
#2.对图片进行检测,格式是否正确
#3.调用opencv对屏幕截图进行分析 得到人脸的个数 并标记人脸
#4.输出人脸图片

orderForStartPhoneScreen ='adb shell /system/bin/screencap -p /sdcard/screenshot.png'
orderForCopyScreen = 'adb pull /sdcard/screenshot.png ~/Documents/python/pythonadbdemo/img/screenshot.png'

#os.system(orderForStartPhoneScreen)
#os.system(orderForCopyScreen)




//export PATH="/Users/leafye/Documents/llvm/llvm2/llvm/build/bin:$    PATH"