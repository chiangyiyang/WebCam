# -*- coding:UTF-8 -*-

from picamera import PiCamera
import time


def getImage():
    img = str(time.time()) + '.jpg'
    imgPath = '/home/pycharm/projects/WebCam/static/' + img
    camera = PiCamera()
    camera.vflip=True
    camera.hflip=True
    camera.capture(imgPath)
    camera.close()
    return img


if __name__ == "__main__":
    getImage()
