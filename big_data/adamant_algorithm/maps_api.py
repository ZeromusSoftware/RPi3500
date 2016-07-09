# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:52:22 2016

@author: william
"""

import urllib, json
import time
import pandas as pd
from math import *

latitude = 43.300848
longitude = 5.390919
latitude2 = 43.280144
longitude2 = 5.440978

rayon = 70
type_recherche = ''
api_key = 'AIzaSyBEK3CzYIaelEgSQkUcpbWJs5MCbAxtrIk'



#Grabbing and parsing the JSON data
def GoogPlac(lat,lng,radius,types,key,nextpagetoken):
  #making the url
    AUTH_KEY = key
    LOCATION = str(lat) + "," + str(lng)
    RADIUS = radius
    TYPES = types
    NEXT_PAGE_TOKEN = nextpagetoken
    if NEXT_PAGE_TOKEN!= False:
        MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?pagetoken=%s'
           '&key=%s') % (NEXT_PAGE_TOKEN, AUTH_KEY)
    else :
        MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&types=%s'
           '&sensor=false'
           '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
  #grabbing the JSON result
    response = urllib.urlopen(MyUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    return jsonData


def fetch_places(lat,lng,rad):

    response = GoogPlac(lat,lng,rad,type_recherche,api_key,False)
    data = response['results']
    
    page_to_read = True
    
    
    noms = [] #nom de l'endroit
    types = {} #type de l'endroit
    
    
    while page_to_read :
        for i in range(len(data)):
            print ('nom : '+ data[i]['name'].encode('utf-8'), 'type :' + data[i]['types'][0].encode('utf-8'))
                
            noms.append(data[i]['name'].encode('utf-8'))
                
            try :
                types[data[i]['types'][0].encode('utf-8')]+=1
            except :
                types[data[i]['types'][0].encode('utf-8')]=1
                
        try :
            page_to_read = response['next_page_token']!= False
        except :
            page_to_read = False
        
        if page_to_read:        
            time.sleep(0.8) # delays for 0.8 seconds
            response = GoogPlac(lat,lng,rad,type_recherche,api_key,response['next_page_token'])
            data = response['results']
            
    return types



def departement(d):
    
    col_titles = ['Departement','Slug','Nom','Nom simple','Nom reel','Nom soundex','Nom metaphone','Code postal',
                  'Numéro de commune','Code commune','truc inconnu','Arrondissement','Canton','Population 2010','Population 1999',
                  'Population 2012','Densité 2010','Superficie','longitude (degre)','latitude (degre)','longitude (GRD)','latitude (GRD)',
                  'longitude (DMS)','latitude (DMS)','Altitude min','Altitude max']


    df = pd.read_csv("villes_france.csv",names = col_titles)
    df = df.loc[df['Departement'] == d]
    
    print (df.head())    
    """print(df.loc[4440][4]) nom
    print(df.loc[4440][18]) latitude
    print(df.loc[4440][19]) longitude """
    





    


latfrtouestsud = 43.205151
longfrtouestsud = 5.512977