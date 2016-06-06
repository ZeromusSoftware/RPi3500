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
#import Adafruit_DHT
#import RPi.GPIO as GPIO
import switch_gpio

# here is set the board pin number corresponding to each component
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

# setup every component to switched off to initialize their status (make sure all rpis are switched off before launching)
"""GPIO.setmode(GPIO.BOARD)
for name in gpio:
    GPIO.setup(gpio[name],GPIO.OUT)
    GPIO.output(gpio[name],1) #to switch off we must output 1
"""
#///////// FOR FETCHING MESSAGES ONLY \\\\\\\\\\\\

# [[consumer key, consumer key secret],[access token, access token secret]]
getapp1=[["WC1jZvkBEcieApsIMLM0y0cxv","ngcC1zVUjVGmev5GP25Pr5mZFst7LwxhiJlLoeAdwpyuc2bUiT"],["709011390850330624-5Lcgpeg1q3RGkyXOuIu6oGdYNHqZCuU","BgYOE22M3Gwpbwuh6AeJ6cvulDaYq9sCluxyTxOJigEFW"]]
getapp2=[["XZvYSDfMghAbZeFUEVc6EW9y3","F2GyoFeA4OCNKZIQtjV3IqN4gM87XhCdzbfVUtJPs2Y0purghc"],["709011390850330624-8UuDVQSoPDeMmeXMbplIHo4Fae7k9VK","7hVWltqz8HaxQ6KBwBSx6OFPchJpA2iACkL8v68VaJrBT"]]
getapp3=[["in1yxCzzWsF0gYlhJurALdlVA","J0xbQ0wVpwDF28C4ecZn8papkFqMyDT6VF0UFgeoYHZAdAc7tr"],["709011390850330624-vynHnIJJpNhh9WhtF2gVIZT70t33n6u","9cEg8zmtPxwyIhPpTxpNYjDCC29eGCdz9pFNtknyEFqXu"]]
getapp4=[["c2J5PCIOr6zujJJJKj6sbZaDV","ZpgtMptXM03gNP0Jao3V9hlHUYpWrQ7RBo6Kw1Z74QjbB0uOO9"],["709011390850330624-E5XkrKzl3vibJ3mCkMEhSZ6ISFyl3gg","i61kOZALoyJCJ8dJrdaGaROweZ9SyRPOdkZQxeETSrXiF"]]
getapp5=[["qEsDRGYAJGoiNnZqTqPBQDNGk","rMG4T0N5y7G6XvyWcDIsGb5WPp5RLu6A7zZPA0ClpOEuuzK8xY"],["709011390850330624-MmEBD7cRWbu2pYwfrYEkgszNXzpPJ2z","k8NsOMPhAZwQsX2j83eEtVmkkl8QCHeX7NPe5FJgv2Peb"]]
getapp6=[["h15tLod2LvMqauMAYJVvzPAtX","J3VvUxQc74zBkOdhYsp12AowjWTn89qZRmdDqgLlWsFzyKg4S5"],["709011390850330624-umFmzlptmP97bGMG37DuV3Zsiv9iG1Z","TjpaJfUKo7RmioQ7vcMOqdWAhhaJE8AlrPzpuoctGXWSc"]]



#///////// FOR SENDING MESSAGES ONLY \\\\\\\\\\\\

# [[consumer key, consumer key secret],[access token, access token secret]]
sendapp1=[["LmU0FahsKIwYQAKHy50MkVobC","l98QDvrECAbY4jrVIf1ek6y7fmGXG3dUFPSgMtuZTLuP3BcXBA"],["709011390850330624-Pn1ygWvoVSQSnV8wHXRqYFB9BoAdPYj","I5IUMGG4GyFwGGpyNiVfcPQqLllaRSFDpRGb7yDRvkEcN"]]
sendapp2=[["sQggF2BnpJ6ascUJaraRtg3oo","xe26ixfCqGWlVkcSJJucfBG4Opqmn4Kz4N3SfcSuduoLg1jnTr"],["735457364149690368-z4fhKoc0BU0u9FBGycZaTPnSm2APExl","J20h8otYQsbYsob8MiEQSNrukwGAjRhgNZfYeLqBkXx6l"]]
sendapp3=[["40MAgIBn73kgBSNK0qLXxHt4Q","FaZIjriiUKDi0dR0Z5wxylxMOJnJSM4QKhGSLU7RpAdr4AvqZd"],["736174072707612673-P7ax5iRMigIl6oxlFci0LhtAXawTWjc","8A2FEZysj3YTu8vIWz3YV2cc1tLdRhMWXXKOLDVcb3KDt"]]
sendapp4=[["AYjfWoVshtnlUk4PIQhk4YssJ","JQWhka4Jco4SUEqZZQyWH856vD3RymErrmh2wgRp05467Ukelm"],["736208117084655617-bky9pR5bFxNoBT7ySWDjslj3UhYpWBw","60YS70tkXlQFbC1Y99dx8eJtPehOMhpNKX4Rgdqedx0RR"]]
sendapp5=[["xuLWiSlRlAKUhvsIE7MPht4Y7","OisDD38Wqfts7rpehUTjRfIV00Iwpk72rLYSRwTZoyhjSCMRkI"],["736458575451656192-6VzajJ11uzkav6sPtg5ZRDMsBWHyOgw","xz5hcrNa4RKHLQKypgOZ7cCofA2q9C9iVbW5INCqtYxVL"]]
sendapp6=[["tv9RNAeiFD7iu1Q8HrvJn8RVN","scQ8PiXj9RsfU3XKyxWzToLh2k2OmwcyGL2ZaXJJJjk5L2JHvq"],["736458941689925632-Lgh8q07B1TmnRDyDrbJAJR8FqvWrRVa","AVDsHo1sIvN7vopcZ1zTC2VNj6iVyFRNZvrGrv4ek8djj"]]


# these users are those who will send us messages
adamant1user_id="709007460401606656"
adamant2user_id="735446697724268545"
adamant3user_id="736545163393257473"
adamant4user_id="736555302527602688"
adamant5user_id="736555302527602688"
adamant6user_id="736555302527602688"
adam_menthe_ids=[adamant1user_id,adamant2user_id,adamant3user_id,adamant4user_id,adamant5user_id,adamant6user_id]


berrypi_1user_id="709011390850330624"
berrypi_2user_id="735457364149690368"
berrypi_3user_id="736174072707612673"
berrypi_4user_id="736208117084655617"
berrypi_5user_id="736458575451656192"
berrypi_6user_id="736458941689925632"

# in this file the successive message ids will be stored
ids="id_memory_file.txt"


#setting initial authorizations for sending apps
global send_app_to_be_used
send_app_to_be_used = sendapp1

send_auth = tw.OAuthHandler(send_app_to_be_used[0][0],send_app_to_be_used[0][1])
send_auth.set_access_token(send_app_to_be_used[1][0],send_app_to_be_used[1][1])
global send_api
send_api = tw.API(send_auth)

global send_count # incremented for each message sent
send_count = 0

#setting initial authorizations for getting apps
global get_app_to_be_used
get_app_to_be_used = getapp1

get_auth = tw.OAuthHandler(get_app_to_be_used[0][0],get_app_to_be_used[0][1])
get_auth.set_access_token(get_app_to_be_used[1][0],get_app_to_be_used[1][1])
global get_api
get_api = tw.API(get_auth)

global get_count # incremented for each message recieved
get_count = 0



def refresh_auth(): # allows to use new applications for each count increment

    global get_api
    get_auth = tw.OAuthHandler(get_app_to_be_used[0][0],get_app_to_be_used[0][1])
    get_auth.set_access_token(get_app_to_be_used[1][0],get_app_to_be_used[1][1])
    get_api = tw.API(get_auth)
    
    global send_api
    send_auth = tw.OAuthHandler(send_app_to_be_used[0][0],send_app_to_be_used[0][1])
    send_auth.set_access_token(send_app_to_be_used[1][0],send_app_to_be_used[1][1])
    send_api = tw.API(send_auth)
    

def send_message(message): # sends the message with the application hidden in send_api
    send_api.send_direct_message(user_id=int(adamant1user_id),text=message)


def fetch_last_message():# fetches last messages, executes it in the shell or switches gpios on/off
    
    #for each getmessage ( <=> for each sendmessage), increment count variables, change the apps and refresh authorizations
    global send_count
    global send_app_to_be_used    

    send_count+=1
    if send_count==7:
        send_count=1
    send_app_to_be_used = eval("sendapp"+str(send_count))
    print("sendapp"+str(send_count))    
    
    
    global get_count
    global get_app_to_be_used    
        
    get_count+=1
    if get_count==7:
        get_count=1
    get_app_to_be_used = eval("getapp"+str(get_count))
    print("getapp"+str(get_count))


    refresh_auth()


        
    #we fetch the direct messages (with their id) sent to us (Rasp_Berrypi)
    direct_message_unicode = get_api.direct_messages(since_id=last_id(),full_text=True)
    message=[]
    message_id_list = []
    for i in direct_message_unicode :
	if (str(i.sender_id) in adam_menthe_ids) : # this filters senders for getting no disturbing messages
            message.append(i.text)
            message_id_list.append(str(i.id)) 
    
    
    print("messages recus :", message)
    print("id des messages recus :", message_id_list)
    
    
    sendback_text = ""    
    
    n=len(message)
    for i in range(n): #f or each message, execute in the shell and respond to Adam_Menthe
        add_new_id(message_id_list[n-i-1]) # index meaning that we execute commands with the recieving order
    
        # two cases available : the message is a switch gpio message or a command
    
        if message[n-i-1][:20] == "*****{gpio_setting}:" and (len(message[n-i-1]) == 23 or len(message[n-i-1]) == 22): # to change gpio
            l = len(message[n-i-1])
            gpio_changing , status_to_set = message[n-i-1][20:l-1], message[n-i-1][l-1]
            switch_gpio.function(gpio_changing,status_to_set) # we use an imported python file "switch_gpio.py"
        else : # to execute commands
            p = subprocess.Popen([message[n-i-1]], stdout=PIPE, stderr=PIPE, shell=True) # executes command
            output, err = p.communicate() # gets the command answer
        
            # this makes the displayed message clear and gives information on the time of execution
            maintenant = datetime.now()
            Y,M,day = str(maintenant.year), str(maintenant.month), str(maintenant.day)
            h,m,s = str(maintenant.hour), str(maintenant.minute), str(maintenant.second)
            date_list = [M,day,h,m,s]
            for k in range(len(date_list)):
                if len(date_list [k])==1:
                    date_list[k] = "0" + date_list[k]
                        
            message_caracteristics = date_list[1] + "/" + date_list[0] + "/" + Y + " - " + date_list[2] + ":" + date_list[3] + ":" + date_list[4] + " - RPi --> "
        
    # this end handles the sending back of messages with {codes} that are used for slicing in getDirectMessage.js       
        
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

    sendback_text += "{GpioCode}" + getGpioStatus() # gpio code will give the status of each component and the box temperature
    print ("Sendback text : " + sendback_text)
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

def refresh_messages(sc): # used for executing fetch_last_message() in intervals of time
    fetch_last_message()
    sc.enter(11, 1, refresh_messages, (sc,))
    print("waiting 10secs..")



def getGpioStatus(): # gets the current status of the raspberrypi gpios, which represents the components state (on/off)
    
    pins_code = ""
    
    pins_code+=get_temperature()
    """
    # we need to transform the gpio dictionnary into a list so the for loop travels the pins in the same order (python issue)
    sorted_gpio_list = [x for x in gpio.iteritems()] 
    sorted_gpio_list.sort(key=lambda x: x[0])
    
    for i in sorted_gpio_list:
        state = GPIO.input(i[1]) # gets the current status of gpio i. state = 1 means component is off, 0 means on
        if state == 0:
            pins_code += "1"
        else:
	    pins_code += "0"
    """
    return pins_code+"01011101"

def get_temperature(): # uses module Adafruit to get the box temperature with the sensor
    """
    sensor = Adafruit_DHT.DHT11
    pin = 4 # the BCM pin used by the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    k=0
    while (humidity is None or temperature is None) and k<30:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        k+=1
    temp = str(int(temperature))
    """
    return "23"
    
# the function executes itself every 11 s
s = sched.scheduler(time.time, time.sleep)
s.enter(11, 1, refresh_messages, (s,))
s.run()
