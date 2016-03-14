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



auth = tw.OAuthHandler("WC1jZvkBEcieApsIMLM0y0cxv","ngcC1zVUjVGmev5GP25Pr5mZFst7LwxhiJlLoeAdwpyuc2bUiT")
auth.set_access_token("709011390850330624-5Lcgpeg1q3RGkyXOuIu6oGdYNHqZCuU","BgYOE22M3Gwpbwuh6AeJ6cvulDaYq9sCluxyTxOJigEFW")
api = tw.API(auth)
adam_menthe_id="709007460401606656"
ids="id_memory_file.txt"



def send_message(message):
    api.send_direct_message(user_id=int(adam_menthe_id),text=message)


def fetch_last_message():#everything is in the title

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
        message_str_list[n-i-1]
        p = subprocess.Popen([message_str_list[n-i-1]], stdout=PIPE, stderr=PIPE, shell=True)
        output, err = p.communicate()
        if err == "":
            err = 'None'
        send_message("out : " + output + "\nerror : " + err)
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
    sc.enter(60, 1, refresh_messages, (sc,))
    print("waiting 60sec..")


#On fait tourner la fonction refresh_messages toutes les 60s
s = sched.scheduler(time.time, time.sleep)
s.enter(60, 1, refresh_messages, (s,))
s.run()
