# -*- coding: utf-8 -*-
#"""
#Created on Tue Mar  8 22:16:26 2016

#@author: william
#"""

import sched, time
import tweepy as tw
import subprocess
from subprocess import PIPE
from datetime import datetime
import Adafruit_DHT
import RPi.GPIO as GPIO

# setup every component to switched off to initialize their status (make sure all rpis are switched off before launching)
GPIO.setmode(GPIO.BOARD)
for name, value in gpio:
    GPIO.setup(value,GPIO.IN)

# [[consumer key, consumer key secret],[access token, access token secret]]
app1=[["WC1jZvkBEcieApsIMLM0y0cxv","ngcC1zVUjVGmev5GP25Pr5mZFst7LwxhiJlLoeAdwpyuc2bUiT"],["709011390850330624-5Lcgpeg1q3RGkyXOuIu6oGdYNHqZCuU","BgYOE22M3Gwpbwuh6AeJ6cvulDaYq9sCluxyTxOJigEFW"]]
app2=[["XZvYSDfMghAbZeFUEVc6EW9y3","F2GyoFeA4OCNKZIQtjV3IqN4gM87XhCdzbfVUtJPs2Y0purghc"],["709011390850330624-8UuDVQSoPDeMmeXMbplIHo4Fae7k9VK","7hVWltqz8HaxQ6KBwBSx6OFPchJpA2iACkL8v68VaJrBT"]]
app3=[["in1yxCzzWsF0gYlhJurALdlVA","J0xbQ0wVpwDF28C4ecZn8papkFqMyDT6VF0UFgeoYHZAdAc7tr"],["709011390850330624-vynHnIJJpNhh9WhtF2gVIZT70t33n6u","9cEg8zmtPxwyIhPpTxpNYjDCC29eGCdz9pFNtknyEFqXu"]]
app4=[["c2J5PCIOr6zujJJJKj6sbZaDV","ZpgtMptXM03gNP0Jao3V9hlHUYpWrQ7RBo6Kw1Z74QjbB0uOO9"],["709011390850330624-E5XkrKzl3vibJ3mCkMEhSZ6ISFyl3gg","i61kOZALoyJCJ8dJrdaGaROweZ9SyRPOdkZQxeETSrXiF"]]
app5=[["qEsDRGYAJGoiNnZqTqPBQDNGk","rMG4T0N5y7G6XvyWcDIsGb5WPp5RLu6A7zZPA0ClpOEuuzK8xY"],["709011390850330624-MmEBD7cRWbu2pYwfrYEkgszNXzpPJ2z","k8NsOMPhAZwQsX2j83eEtVmkkl8QCHeX7NPe5FJgv2Peb"]]
app6=[["h15tLod2LvMqauMAYJVvzPAtX","J3VvUxQc74zBkOdhYsp12AowjWTn89qZRmdDqgLlWsFzyKg4S5"],["709011390850330624-umFmzlptmP97bGMG37DuV3Zsiv9iG1Z","TjpaJfUKo7RmioQ7vcMOqdWAhhaJE8AlrPzpuoctGXWSc"]]

adam_menthe_id="709007460401606656"
ids="id_memory_file.txt"

global app_to_be_used
app_to_be_used = app1

auth = tw.OAuthHandler(app_to_be_used[0][0],app_to_be_used[0][1])
auth.set_access_token(app_to_be_used[1][0],app_to_be_used[1][1])
global api
api = tw.API(auth)

global count
count = 0

def refresh_auth():
    global api
    auth = tw.OAuthHandler(app_to_be_used[0][0],app_to_be_used[0][1])
    auth.set_access_token(app_to_be_used[1][0],app_to_be_used[1][1])
    api = tw.API(auth)
    

def send_message(message):
    api.send_direct_message(user_id=int(adam_menthe_id),text=message)


def fetch_last_message():#everything is in the title

    global count
    global app_to_be_used    
    
    count+=1
    
    if count%3==1:
        app_to_be_used = app1
        refresh_auth()
        print("app1")
    if count%3==2:
        app_to_be_used = app2
        refresh_auth()
        print("app2")
    if count%3==0:
        app_to_be_used = app3
        refresh_auth()
        print("app3")
        
    count+=1
        
    #we fetch the direct messages (with their id) sent to us (Rasp_Berrypi), ignoring smileys ;)
    direct_message_unicode = api.direct_messages(since_id=last_id(),full_text=True)
    message=[]
    message_id_list = []
    for i in direct_message_unicode :
	if (str(i.sender_id) == adam_menthe_id) :
            message.append(i.text)
            message_id_list.append(str(i.id))
    
    
    print("messages recus :", message)
    print("id des messages recus :", message_id_list)
    
    
    sendback_text = ""    
    
    n=len(message)
    for i in range(n): #for each message, execute in the shell and respond to Adam_Menthe
        add_new_id(message_id_list[n-i-1])#index meaning that we execute commands with the recieving order
        p = subprocess.Popen([message[n-i-1]], stdout=PIPE, stderr=PIPE, shell=True)
        output, err = p.communicate()
        
        maintenant = datetime.now()
        Y,M,day = str(maintenant.year), str(maintenant.month), str(maintenant.day)
        h,m,s = str(maintenant.hour), str(maintenant.minute), str(maintenant.second)
        message_caracteristics = day + "/" + M + "/" + Y + " - " + h + ":" + m + ":" + s + " - RPi --> "
        
        if err == "":
            if i==0:
                sendback_text += message_caracteristics + "out : " + output
            else :
                sendback_text += "{separationdesmessage}" + message_caracteristics + "out : " + output
        else:
            if i==0:
                sendback_text += message_caracteristics + "error : " + err
            else:
                sendback_text += "{separationdesmessage}" + message_caracteristics + "error : " + err

    sendback_text += "{GpioCode}" + getGpioStatus()
    
    send_message(sendback_text)
    
    return True
    

def last_id(): #fetches the id of the last task in the memory file
    id_file = open(ids,"r")
    last_id = id_file.read().split("\n")[0]
    id_file.close()
    return last_id

def add_new_id(id_to_add): #add the id of the last task recieved on top of the memory file
    f = open(ids, 'r+')        
    content = f.read()
    f.seek(0, 0)
    f.write(id_to_add.rstrip('\r\n') + '\n' + content)
    f.close()
    print('id : ' + id_to_add + ' added')

def refresh_messages(sc):
    fetch_last_message()
    sc.enter(21, 1, refresh_messages, (sc,))
    print("waiting 20secs..")

gpio = {
    "rpi1":5,
    "rpi2":7,
    "rpi3":11,
    "rpi4":13,
    "ventilo1":15,
    "ventilo2":19,
    "ventilo3":22,
    "ventilo4":23
    }

def getGpioStatus():
    
    
    pins_code = ""
    
    pins_code+=get_temperature()
    
    for name, value in gpio:
        state = GPIO.input(value)
        if state == 0:
            pins_status += "1"
        else:
	    pins_status += "0"
    return pins_status

def get_temperature():
    sensor = Adafruit_DHT.DHT11
    pin = gpio["capteur"]
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    k=0
    while (humidity is None or temperature is None) and k<30:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        k+=1
    temp = str(int(temperature))
    return temp
    
#On fait tourner la fonction refresh_messages toutes les 60s
s = sched.scheduler(time.time, time.sleep)
s.enter(21, 1, refresh_messages, (s,))
s.run()
