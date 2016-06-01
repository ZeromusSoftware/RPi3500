#!/usr/bin/python

import RPi.GPIO as GPIO
import sys

gpio = ['5','7','11','13','15','19','22','23']

if len(sys.argv) == 3 and sys.argv[1] in gpio :
    
    GPIO.setmode(GPIO.BOARD)
    
    pin = sys.argv[1]
    status = sys.argv[2]
    
    if status=='0' :
        GPIO.setup(pin, GPIO.IN)
        
    elif status=='1' :
        GPIO.setup(pin, GPIO.OUT)
    
    else :
        print('usage: python2.7 switch_gpio.py 13 1')
        sys.exit(1)
else:
    print('usage: python2.7 switch_gpio.py 13 1')
    sys.exit(1)
