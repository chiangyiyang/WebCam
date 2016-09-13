#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 8
GPIO.setup(pin, GPIO.IN)

def isHigh():
    return GPIO.input(pin)


if __name__ == "__main__":
    print(isHigh())
