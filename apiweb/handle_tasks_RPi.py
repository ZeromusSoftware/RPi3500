# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:16:26 2016

@author: william
"""

import tweepy as tw
import unicodedata

auth = tw.OAuthHandler("L0kBOCV1IMqtHStaFND2o8h78","rgKaICgWEYu07CMvRBhb5e8HVpDu70xb5Z5RlDdGP7S7mMB91Y")
auth.set_access_token("2878700986-62BKfaV8Jnd916cpUE3FP25hnDRlIaVd4J77zRj","vJIryO1tX64AXnYcbZGrA3IhkZ2RoRofAAZQjCXHrSIFr")
api = tw.API(auth)
bastien_id = "292141911"

def send_message(message):
    api.send_direct_message(user_id=bastien_id,text=message)
    
def fetch_last_message():
    direct_message_unicode = api.direct_messages(count=1,full_text=True)[0]
    message_str = unicodedata.normalize('NFKD', direct_message_unicode.text).encode('ascii','ignore')
    return message_str
    
print(fetch_last_message())