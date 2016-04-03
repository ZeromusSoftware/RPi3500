# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:16:26 2016

@author: william
"""

import sched, time
import tweepy as tw
import unicodedata
import subprocess
from subprocess import PIPE

# [[consumer key, consumer key secret],[access token, access token secret]]
app1=[["WC1jZvkBEcieApsIMLM0y0cxv","ngcC1zVUjVGmev5GP25Pr5mZFst7LwxhiJlLoeAdwpyuc2bUiT"],["709011390850330624-5Lcgpeg1q3RGkyXOuIu6oGdYNHqZCuU","BgYOE22M3Gwpbwuh6AeJ6cvulDaYq9sCluxyTxOJigEFW"]]
app2=[["XZvYSDfMghAbZeFUEVc6EW9y3","F2GyoFeA4OCNKZIQtjV3IqN4gM87XhCdzbfVUtJPs2Y0purghc"],["709011390850330624-8UuDVQSoPDeMmeXMbplIHo4Fae7k9VK","7hVWltqz8HaxQ6KBwBSx6OFPchJpA2iACkL8v68VaJrBT"]]
app3=[["in1yxCzzWsF0gYlhJurALdlVA","J0xbQ0wVpwDF28C4ecZn8papkFqMyDT6VF0UFgeoYHZAdAc7tr"],["709011390850330624-vynHnIJJpNhh9WhtF2gVIZT70t33n6u","9cEg8zmtPxwyIhPpTxpNYjDCC29eGCdz9pFNtknyEFqXu"]]
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
print("app1")

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
    if count==16:
        app_to_be_used = app2
        refresh_auth()
        print("app2")
    if count==31:
        app_to_be_used = app3
        refresh_auth()
        print("app3")
    if count==46:
        app_to_be_used = app1
        refresh_auth()
        print("app1")
        count = 0
        
    #we fetch the direct messages (with their id) sent to us (Rasp_Berrypi), ignoring smileys ;)
    direct_message_unicode = api.direct_messages(since_id=last_id(),full_text=True)
    message=[i.text for i in direct_message_unicode]
    message_str_list=[unicodedata.normalize('NFKD', message[i]).encode('ascii','ignore') for i in range(len(message))]
    message_id_list = [str(i.id) for i in direct_message_unicode]
    
    print("messages recus :", message_str_list)
    print("id des messages recus :", message_id_list)
    
    n=len(message_str_list)
    for i in range(n): #for each message, execute in the shell and respond to Adam_Menthe
        add_new_id(message_id_list[n-i-1])#index meaning that we execute commands with the recieving order
        p = subprocess.Popen([message_str_list[n-i-1]], stdout=PIPE, stderr=PIPE, shell=True)
        output, err = p.communicate()
        if err == "":
            err = 'None'
        send_message("out : " + output + "error : " + err)
    return True
    
def last_id():#fetches the id of the last task in the memory file
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


#On fait tourner la fonction refresh_messages toutes les 60s
s = sched.scheduler(time.time, time.sleep)
s.enter(21, 1, refresh_messages, (s,))
s.run()