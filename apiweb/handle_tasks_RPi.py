# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:16:26 2016

@author: william
"""

import sched, time
import tweepy as tw
import unicodedata
import subprocess

s = sched.scheduler(time.time, time.sleep)
auth = tw.OAuthHandler("L0kBOCV1IMqtHStaFND2o8h78","rgKaICgWEYu07CMvRBhb5e8HVpDu70xb5Z5RlDdGP7S7mMB91Y")
auth.set_access_token("2878700986-62BKfaV8Jnd916cpUE3FP25hnDRlIaVd4J77zRj","vJIryO1tX64AXnYcbZGrA3IhkZ2RoRofAAZQjCXHrSIFr")
api = tw.API(auth)
bastien_id = "292141911"
william_id="2878700986"
ids="id_memory_file.txt"


api.send_direct_message(user_id=int(william_id),text='coucou')


def send_message(message):
    api.send_direct_message(user_id=int(william_id,text=message)


def fetch_last_message():
    
    direct_message_unicode = api.direct_messages(since_id=last_id(),full_text=True)
    message=[i.text for i in direct_message_unicode]
    
    message_str_list=[unicodedata.normalize('NFKD', message[i]).encode('ascii','ignore') for i in range(len(message))]
    message_id_list = [str(i.id) for i in direct_message_unicode]
    
    print("messages recus :", message_str_list)
    print("id des messages recus :", message_id_list)
    
    n=len(message_str_list)
    for i in range(n):
        add_new_id(message_id_list[n-i-1])
        try:
            subprocess.check_call(message_str_list[n-i-1], shell=True)
            send_message(str(subprocess.check_call(message_str_list[n-i-1], shell=True)))
        except:
            pass
    return True
    
def last_id():    
    id_file = open(ids,"r")
    last_id = id_file.read().split("\n")[0]
    id_file.close()
    return last_id

def add_new_id(id_to_add): #add the id of the last task recieved on top of the memory file
    with open(ids, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(id_to_add.rstrip('\r\n') + '\n' + content)

def thing_to_do(sc):
    print("doing stuff..")
    print(open(ids, 'r').read())
    fetch_last_message()
    print(open(ids, 'r').read())
    sc.enter(60, 1, thing_to_do, (sc,))
    
#fetch_last_message()    
    
#s.enter(60, 1, thing_to_do, (s,))
#s.run()
