# -*- coding: utf-8 -*-
# VS2017+python3.6+opencv3.4
# 2018.02.03
# 作者：艾克思

import cv2


def thresh(img):
    x1, y1, w1, h1, x2, y2, w2, h2 = 0, 0, 0, 0, 0, 0, 0, 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray=cv2.GaussianBlur(gray,(13,13),0) #高斯模糊
    h0, w0 = img.shape[:2]
    top = gray[h0 // 3, 10]
    bottom = gray[h0 * 2 // 3, 10]

    thresh1 = cv2.threshold(gray, top, 255, cv2.THRESH_BINARY)[1]
    thresh2 = cv2.threshold(gray, bottom, 255, cv2.THRESH_BINARY_INV)[1]
    img1 = thresh1[h0 // 3:h0 * 2 // 3, 0:w0]
    img2 = thresh2[h0 // 3:h0 * 2 // 3, 0:w0]

    cnts1, hierarchy1, rr1 = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts2, hierarchy2, rr2 = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    aim1 = 0
    y_min = h0 // 3
    for c in hierarchy1:
        if hierarchy1 == None:
            x1, y1, w1, h1 = w0 // 2, h0 // 3, w0 // 3, h0 // 3
            break
        else:
            x, y, w, h = cv2.boundingRect(c)
            if y <= y_min:
                y_min = y
                aim1 = c
                x1, y1, w1, h1 = cv2.boundingRect(aim1)
                cv2.rectangle(img, (x1, y1 + h0 // 3), (x1 + w1, y1 + h1 + h0 // 3), (255, 0, 0), 2)

                aim2 = 0
                y_min = h0 // 3
                for c in hierarchy2:
                    if hierarchy2 == None:
                        x2, y2, w2, h2 = w0 // 2, h0 // 3, w0 // 3, h0 // 3
                        break
                    else:
                        x, y, w, h = cv2.boundingRect(c)
                        if y <= y_min:
                            y_min = y
                        aim2 = c
                        x2, y2, w2, h2 = cv2.boundingRect(aim2)
                        cv2.rectangle(img, (x2, y2 + h0 // 3), (x2 + w2, y2 + h2 + h0 // 3), (0, 255, 0), 2)

    if y1 + h1 // 2 <= y2 + h2 // 2:
        x, y, w, h = x1, y1, w1, h1
    else:
        x, y, w, h = x2, y2, w2, h2

    cv2.imshow('img1', thresh1)
    cv2.imshow('img2', thresh2)

    return (x + w // 2, y + h0 // 3 + h // 2)


def main():
    video = 'jump.avi'
    cap = cv2.VideoCapture(video)
    ret = cap.isOpened()
    ret = True
    while ret:
        # ret,img=cap.read() #读入帧
        img = cv2.imread('e:/python/jump/hsv/006.png')
        if not ret: cv2.waitKey(0)
        point = thresh(img)
        cv2.circle(img, point, 3, (0, 0, 255), -1)
        cv2.circle(img, point, 15, (0, 0, 255), 2)

        cv2.imshow('img', img)
        if cv2.waitKey(25) == ord('q'): break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
