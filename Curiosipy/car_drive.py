import RPi.GPIO as GPIO
import time
import numpy as np
import os
import multiprocessing

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.HIGH)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,GPIO.HIGH)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,GPIO.HIGH)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.HIGH)

def forward(direction):
    pin = 0
    
    if direction == "left":
        pin = 12
    elif direction == "right":
        pin = 11
        
    if pin == 0:
        GPIO.output(8,GPIO.LOW)
        print('Going forward')
    else :
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        print('Going forward and ' + direction)

def backward(direction):
    pin = 0
    
    if direction == "left":
        pin = 12
    elif direction == "right":
        pin = 11
        
    if pin == 0:
        GPIO.output(7,GPIO.LOW)
        print('Going backward')
    else :
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        print('Going backward and ' + direction)

def stop():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,GPIO.HIGH)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.HIGH)
    GPIO.setup(8,GPIO.OUT)
    GPIO.output(8,GPIO.HIGH)
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7,GPIO.HIGH)
    



def distance(direction):
    echo = 0
    trig = 0
    if direction == "front":
        echo = 5
        trig = 3
    elif direction == "back":
        echo = 16
        trig = 15
    elif direction == "left":
        echo = 21
        trig = 3
    elif direction == "right":
        echo = 22
        trig = 10
    else :
        return "Error, args are 'front','back','left' or 'right'"
    
    try:
        GPIO.setup(trig,GPIO.OUT)
        GPIO.output(trig,GPIO.HIGH)
        GPIO.setup(echo,GPIO.IN)
        GPIO.output(trig,False)
        
        while GPIO.input(echo) == 0:
            nosig = time.time()

        while GPIO.input(echo) == 1:
            sig = time.time()

        tl = sig - nosig

        distance = tl / 0.000058 #pour obtenir la mesure en cm

        GPIO.output(trig,GPIO.HIGH)
        return distance,sig
    except:
        distance = "error"
        GPIO.output(trig,GPIO.HIGH)
        return distance,0

""" TEST DIRECTION 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(8,GPIO.LOW)
time.sleep(3)
GPIO.output(12,GPIO.LOW)
time.sleep(3)
GPIO.output(12,GPIO.HIGH)
GPIO.output(11,GPIO.LOW)
time.sleep(3)
stop()"""

'''
M = np.zeros((1000,1000))
for i in range(23):
    for j in range(33):
        M[500-11+i][500-16+j]=2
print(M[500-11][500+16])
'''

''' ARRET A DETECTION DE LOBSTACLE '''
stop()
for i in range(3):
    d,t = distance("front")
    advanced = False
    forward(0)
    print(d)
    while d>20:
        advanced = True
        time.sleep(0.05)
        d,t = distance('front')
        print(d)
    stop()
    if advanced :
        backward(0)
        time.sleep(0.1)
        stop()


""" FONCTIONNEMENT CAPTEURS
cotes = ['front','back','left','right']
for d in cotes:
    for i in range(30):
        print(d+" : "+str(distance(d)))
"""
"""
V,D = [],[]
for i in range(10):
    d1,t1 = distance('front')
    forward(0)
    time.sleep(0.05)
    stop()
    d2,t2 = distance('front')
    V.append((d1-d2)/(t2-t1))
    D.append(d2-d1)
    time.sleep(5)

v = sum(V)/10
d = sum(D)/10
print('distance min ='+str(d),'vitesse ='+str(v))
"""
