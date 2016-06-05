#!/usr/bin/python

import RPi.GPIO as GPIO

def function(arg1, arg2):

    gpio = ['5','7','11','13','15','19','22','23']

    if arg1 in gpio :
        
        GPIO.setmode(GPIO.BOARD)
        
        pin = int(arg1)
        status = arg2
        
        if status=='0' :
            GPIO.output(pin, 1)
        
        elif status=='1' :
            GPIO.output(pin, 0)
        
        print ("success changing gpio " + arg1 + " status to " + arg2)
    else:
        print('error')
