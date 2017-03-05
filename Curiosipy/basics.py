import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.HIGH)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,GPIO.HIGH)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.HIGH)

def turn(direction):
    if direction == "left":
        pin = 12
    elif direction == "right":
        pin = 11
    GPIO.output(pin,GPIO.LOW)
    
def forward(direction):
    
    pin = 0
    
    if direction == "left":
        pin = 12
    elif direction == "right":
        pin = 11
        
    if pin == 0:
        GPIO.output(18,GPIO.LOW)
        #print('Going forward')
    else :
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        #print('Going forward and ' + direction)
        

def backward(direction):
    
    pin = 0
    
    if direction == "left":
        pin = 12
    elif direction == "right":
        pin = 11
        
    if pin == 0:
        GPIO.output(7,GPIO.LOW)
        #print('Going backward')
    else :
        GPIO.output(pin,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        #print('Going backward and ' + direction)
        

def stop():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,GPIO.HIGH)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,GPIO.HIGH)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7,GPIO.HIGH)
    



def distance(direction):
    echo = 0
    trig = 0
    if direction == "front" or direction == 0:
        echo = 5
        trig = 3
    elif direction == "back" or direction == 3:
        echo = 16
        trig = 15
    elif direction == "left" or direction == 1:
        echo = 21
        trig = 3
    elif direction == "right" or direction == 2:
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
        return distance
    except:
        distance = 10000
        GPIO.output(trig,GPIO.HIGH)
        return distance