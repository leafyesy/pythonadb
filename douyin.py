import os
import cv2
import math
import numpy as np
import time
import shutil

path = os.getcwd()


def captureScreenShotToImg(path):
    # fetch phont screenshot and save into img
    os.system("adb shell /system/bin/screencap -p /sdcard/%s.png" % path)
    os.system("adb pull /sdcard/screenshot.png ~/study/pythonadb/img/%s.png" % path)


def checkIsFail(result_shot_img):
    return False


currentIndex = 1
DEF_TOUCH_TIME = 1.5

shutil.rmtree(path + r"/img")
os.mkdir(path + r"/img")

while True:

    screenshot = 'screenshot%d' % currentIndex
    captureScreenShotToImg(screenshot)
    # read img form screenshot
    current_screen_img = cv2.imread(path + r'/img/%s.png' % screenshot)
    img_gray = cv2.cvtColor(current_screen_img, cv2.COLOR_BGR2GRAY)

    '''
    #使用灰度范围定位
    lower_gray = np.array([40])  # 设定蓝色的阈值
    upper_gray = np.array([58])
    tm = cv2.imread(path + r'/img/i.png')

    mask_gray = cv2.inRange(img_gray, lower_gray, upper_gray)

    image2,contours, hierarchy = cv2.findContours(mask_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours,hierarchy = cv2.findContours(mask_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    '''

    '''

    # 使用matchTemplate 进行识别棋子位置

    tm_gray = cv2.cvtColor(tm, cv2.COLOR_BGR2GRAY)

    md = cv2.TM_CCORR
    th, tw = tm_gray.shape[:2]
    result = cv2.matchTemplate(img_gray, tm_gray, md)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if md == cv2.TM_SQDIFF_NORMED:
        tl = min_loc
    else:
        tl = max_loc

    br = (tl[0] + tw, tl[1] + th)
    # 绘制矩形边框，将匹配区域标注出来
    # target：目标图像
    # tl：矩形定点
    # br：举行的宽高
    # (0,0,255)：矩形边框颜色
    # 2：矩形边框大小
    # cv2.rectangle(img_gray, tl, br, (0, 0, 255), 2)
    # cv.imshow('match-'+np.str(md),img_gray)

    '''

    lower_blue = np.array([115, 75, 75])  # 设定蓝色的阈值
    upper_blue = np.array([130, 255, 125])
    hsv = cv2.cvtColor(current_screen_img, cv2.COLOR_BGR2HSV)  # 转到HSV空间
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    cnts = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    mtPixelW = 0
    mtPixelH = 0
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)  # 找到面积最大的轮廓
        ((x, y), radius) = cv2.minEnclosingCircle(c)  # 确定面积最大的轮廓的外接圆
        mtPixelH = y
        mtPixelW = x
        center = (int(x), int(y))
        cv2.circle(current_screen_img, center, int(radius + 10), (0, 0, 255), 3)  # 画出圆心
        cv2.circle(current_screen_img, center, 3, (0, 0, 255), -1)

    '''
    cv2.namedWindow("frame", 0)
    cv2.namedWindow("hsv", 0)
    cv2.namedWindow("mask", 0)
    cv2.imshow('frame', frame)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask', mask_blue)
    # cv2.imshow('gray_mask',mask_gray)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    '''

    '''
    逐行扫描灰度图,获取灰度图上第一个不同于其他点灰度的颜色

    '''

    size = img_gray.shape
    startH = int(size[0] / 3)
    firstPixel = img_gray[startH, 0]
    diffPixel = firstPixel

    diffW = 0
    diffH = 0

    diffW1 = 0
    diffH1 = 0

    for h in range(startH, img_gray.shape[0], 10):
        for w in range(0, img_gray.shape[1], 10):
            # print("w:%d   h:%d" % (w, h))
            currentPixel = img_gray[h, w]
            diffPixelValue = int((int(currentPixel) - int(firstPixel)) / 2)
            if diffPixelValue > 2:
                print(img_gray[h, w])
                diffW = w
                diffH = h
                # 精细查找
                for h1 in range(h - 20, h + 20, 1):
                    for w1 in range(w - 20, w + 20, 1):
                        # print("w1:%d   h1:%d" % (w1, h1))
                        currentPixel1 = img_gray[h1, w1]
                        diffPixelValue1 = int((int(currentPixel1) - int(firstPixel)) / 2)
                        if diffPixelValue1 > 3:
                            print(img_gray[h1, w1])
                            diffPixel = img_gray[h1, w1]
                            diffW1 = w1
                            diffH1 = h1
                            break
                    if diffPixel != firstPixel:
                        break
            if diffPixel != firstPixel:
                break
            else:
                img_gray[h, w] = 0
                pass
            pass
        if diffPixel != firstPixel:
            break
        pass

    print("diffPixel :%d  位置:w:%d   h:%d" % (diffPixel, diffW1, diffH1))

    center = (int(diffW), int(diffH))
    center1 = (int(diffW1), int(diffH1))

    cv2.circle(current_screen_img, center, 10, (0, 0, 255), 1)
    cv2.circle(current_screen_img, center, 1, (0, 0, 255), 1)
    cv2.circle(current_screen_img, center1, 10, (0, 255, 0), 1)
    cv2.circle(current_screen_img, center1, 1, (0, 255, 0), 1)

    # 计算两个点间的距离 并adb 长按事件 进行跳跃
    diff_two_dot = math.sqrt(int((mtPixelH - diffH1) ** 2) + int((mtPixelW - diffW1)) ** 2)
    print("diff_two_dot:%d" % diff_two_dot)

    cv2.imwrite(path + r"/img/%s.png" % screenshot, current_screen_img)

    #
    # cv2.namedWindow("frame", cv2.WINDOW_OPENGL)
    # cv2.imshow('frame', frame)
    # if cv2.waitKey(0) == ord('q'):
    #     cv2.destroyAllWindows()

    touchTime = diff_two_dot * DEF_TOUCH_TIME
    print("touchTime:%d" % touchTime)
    os.system('adb shell input swipe 200 300 200 300 %d' % touchTime)
    # wait shell run stop
    time.sleep(float(touchTime / 1000))

    # do next

    # check result is ok
    result_shot = 'result_shot%d' % currentIndex
    captureScreenShotToImg(result_shot)
    result_shot_img = cv2.imread(path + r'/img/%s.png' % result_shot, cv2.IMREAD_ANYCOLOR)

    # check is fail

    currentIndex += 1

    if checkIsFail(result_shot_img):
        break
