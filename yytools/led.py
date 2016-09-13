# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 7
GPIO.setup(pin, GPIO.OUT)


def blink(t):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(t)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(t)


def ledOn():
    GPIO.output(pin, GPIO.LOW)


def ledOff():
    GPIO.output(pin, GPIO.HIGH)


if __name__ == "__main__":
    for i in range(30):
        blink(0.1)

    for i in range(3):
        ledOn()
        time.sleep(0.5)
        ledOff()
        time.sleep(0.5)
