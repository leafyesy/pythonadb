import cv2
import os
import numpy


def testImRead():
    flagArr = [
        cv2.IMREAD_ANYCOLOR,
        cv2.IMREAD_ANYDEPTH,
        cv2.IMREAD_COLOR,
        cv2.IMREAD_GRAYSCALE,
        cv2.IMREAD_UNCHANGED,
        cv2.IMREAD_LOAD_GDAL]
    for flag in flagArr:
        _1img = cv2.imread(os.getcwd() + r"/img/1.jpg", flag)
        cv2.imshow("_%djpg" % flag, _1img)
        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()
    pass


def randomNum2Img():
    randomByteArr = bytearray(os.urandom(120000))
    flatNumpyArr = numpy.array(randomByteArr)
    garyImg = flatNumpyArr.reshape(300, 400)
    cv2.imwrite(os.getcwd() + r"/img/randomNumGrayImg.jpg", garyImg)
    cv2.imshow("randomNumGrayImg", garyImg)

    bgrImg = flatNumpyArr.reshape(200, 200, 3)
    cv2.imwrite(os.getcwd() + r"/img/randomNumBgrImg.jpg", bgrImg)
    cv2.imshow("randomNumBgrImg", bgrImg)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()
    pass


def testNpOperate():
    _1img = cv2.imread(os.getcwd() + r"/img/1.jpg", cv2.IMREAD_UNCHANGED)
    # _1img[:, :, 0] = 0
    # _1img[:, :, 1] = 0
    # _1img[:, :, 2] = 0
    cv2.imshow("_1jpg", _1img)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()


def readVideo():
    videoCapture = cv2.VideoCapture(os.getcwd() + r"/img/1.mp4")
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter("2.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
    success, frame = videoCapture.read()
    while success:
        videoWriter.write(frame)
        success, frame = videoCapture.read()


def readCamera():
    cameraCapture = cv2.VideoCapture(0)
    fps = 30
    size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter('myCameraCapture.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
    success, frame = cameraCapture.read()
    numFrameRemaining = 10 * fps - 1
    while success:
        videoWriter.write(frame)
        success, frame = cameraCapture.read()
        numFrameRemaining -= 1
    cameraCapture.release()


def cameraPreview():
    cameraCapture = cv2.VideoCapture(0)
    # fps = 30
    # size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    while True:
        ret, frame = cameraCapture.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_FLAG_LBUTTON:
        clicked = True


def cameraPreview2():
    clicked = False
    cameraCapture = cv2.VideoCapture(0)
    cv2.namedWindow('capture2')
    cv2.setMouseCallback('capture2', onMouse)

    print('show camera capture')

    ret, frame = cameraCapture.read()
    while ret and cv2.waitKey(1) == -1 and not clicked:
        cv2.imshow('capture', frame)
        ret, frame = cameraCapture.read()

    cv2.destroyAllWindows()
    cameraCapture.release()


if __name__ == '__main__':
    # testImRead()
    # randomNum2Img()
    # testNpOperate()r
    cameraPreview2()
