import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) 
state = GPIO.input(11)
pins_code = ""
if state == True:
    pins_code += "1"
elif state == False:
    pins_code += "0"
else :
    pins_code += str(state)
print(pins_code)
