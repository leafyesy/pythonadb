import numpy as np
import cv2
import os

c_path = os.getcwd()
# lower_blue = np.array([115, 75, 75])
# upper_blue = np.array([130, 255, 125])
# hsv (Hue 色度，Saturation 饱和度，Value 纯度)

current_flag_img = cv2.imread(c_path + r'/img2/i.png')
hsv_flag = cv2.cvtColor(current_flag_img, cv2.COLOR_BGR2HSV)  # 转到HSV空间
# for pixel in current_flag_img:
    # print("h:%d - s:%d - v:%d" % (pixel[0], pixel[1], pixel[2]))
    # print(pixel)
current_screen_img = cv2.imread(c_path + r'/img2/2.jpg')

h, s, v = cv2.split(hsv_flag)


'''
H色度取值范围是[0,179]
S饱和度的取值范围是[0,255]
V明度的取值范围是[0,255]
'''

# lower_blue = np.array([115, 75, 75])  # 设定蓝色的阈值
# upper_blue = np.array([130, 255, 255])


lower_blue = np.array([67, 45, 50])  # 设定蓝色的阈值
upper_blue = np.array([90, 65, 70])

hsv = cv2.cvtColor(current_screen_img, cv2.COLOR_BGR2HSV)  # 转到HSV空间
mask_blue = cv2.inRange(current_screen_img, lower_blue, upper_blue)
cnts = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

# cv2.matchTemplate()

if len(cnts) > 0:
    c = max(cnts, key=cv2.contourArea)  # 找到面积最大的轮廓
    ((x, y), radius) = cv2.minEnclosingCircle(c)  # 确定面积最大的轮廓的外接圆
    mt_pixel_h = y + 30
    mt_pixel_w = x
    center = (int(x), int(y + 30))
    cv2.circle(current_screen_img, center, int(radius + 10), (0, 0, 255), 3)  # 画出圆心
    cv2.circle(current_screen_img, center, 3, (0, 0, 255), -1)
    cv2.circle(mask_blue, center, int(radius + 10), (255, 255, 255), 3)  # 画出圆心
    cv2.circle(mask_blue, center, 3, (0, 0, 255), -1)
    cv2.circle(hsv, center, int(radius + 10), (0, 0, 255), 3)  # 画出圆心
    cv2.circle(hsv, center, 3, (0, 0, 255), -1)

cv2.imwrite(c_path + r"/img2/hvs.jpg", current_screen_img)
cv2.imwrite(c_path + r"/img2/hvs.jpg", hsv)
cv2.imwrite(c_path + r"/img2/mask.jpg", mask_blue)
