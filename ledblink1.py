#!/usr/bin/python3
# blink/unblink an led by push button
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)
while True:
    if GPIO.input(10):
        print('inverse pushbutton is not pressed -> LED is blinkig')
        GPIO.output(8,True)
        time.sleep(0.1)
        GPIO.output(8,False)
        time.sleep(0.1)
    else:
        GPIO.output(8,True)
        print('inverse pushbutton is pressed -> LED is on (no blink)')
        time.sleep(0.2)
    