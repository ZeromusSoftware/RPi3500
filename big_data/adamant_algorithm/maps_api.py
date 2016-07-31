# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:52:22 2016

@author: william
"""
import time
import urllib, json
import pandas as pd
from math import *
import numpy as np
import coords_maps_sector
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

distance_between_points = 1000

coords_commune = []
research_coordinates = []

radius = distance_between_points/(2**(1/2))
type_recherche = ''
api_key1 = 'AIzaSyApQuQ55Ml2q7bJLXQs2U-w47yqCB7ccPs'
api_key2 = 'AIzaSyBEK3CzYIaelEgSQkUcpbWJs5MCbAxtrIk'
api_key3 = 'AIzaSyBPPv6sz-PjrCWbAiw6-zBcRlx8oAWh3RI'
used_key = api_key1

def change_api_key():
    global used_key
    
    if used_key == api_key1:
        used_key = api_key2
    elif used_key == api_key2:
        used_key = api_key3
    else:
        used_key = api_key1


#Grabbing and parsing the JSON data
def GoogPlac(lat,lng,rad,research_type,key,nextpagetoken):
  #making the url
    AUTH_KEY = key
    LOCATION = str(lat) + "," + str(lng)
    RADIUS = rad
    TYPE = research_type
    NEXT_PAGE_TOKEN = nextpagetoken
    if NEXT_PAGE_TOKEN!= False:
        MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?pagetoken=%s'
           '&key=%s') % (NEXT_PAGE_TOKEN, AUTH_KEY)
    else :
        MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&type=%s'
           '&sensor=false'
           '&key=%s') % (LOCATION, RADIUS, TYPE, AUTH_KEY)
  #grabbing the JSON result
    grabbed = False
    k=0
    while not(grabbed) and k<10:
        try:
            response = urllib.urlopen(MyUrl)
            grabbed = True
        except:
            k+=1
            print('failed '+str(k)+' time(s)')
            pass
        
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    return jsonData


places_dataframe = pd.DataFrame({'Name':[],'Latitude':[],'Longitude':[],'Type':[],'Place_id':[]})


def fetch_places(lat,lng,rad):

    global places_dataframe

    response = GoogPlac(lat,lng,rad,type_recherche,used_key,False)
    
    while response['status'] == 'OVER_QUERY_LIMIT':
        change_api_key()
        response = GoogPlac(lat,lng,rad,type_recherche,used_key,False)
        
    data = response['results']
    
    page_to_read = True
    
    
    while page_to_read :
        for i in range(len(data)):
                
            df_to_append = pd.DataFrame({
            'Name':[str(data[i]['name'])],
            'Latitude':[str(data[i]['geometry']['location']['lat'])],
            'Longitude':[str(data[i]['geometry']['location']['lng'])],
            'Type':[data[i]['types']],
            'Place_id':[str(data[i]['place_id'])]})
            
            if  not (str(data[i]['place_id']) in np.array(places_dataframe['Place_id'])):
                places_dataframe = places_dataframe.append(df_to_append)
              
        
        try :
            page_to_read = response['next_page_token']!= False
        except :
            page_to_read = False
        
        
        
        if page_to_read:       
            print ("Looking for places..")
            time.sleep(1.5) # delay for 1 second
            response = GoogPlac(lat,lng,rad,type_recherche,used_key,response['next_page_token'])
            data = response['results']
    


X,Y = [],[]

def display_places(dataframe):
    
    fig = plt.figure(type_recherche + " found")
    
    U=[]
    V=[]
    
    
    
    n = len(coords_commune)
    m = 0
    is_multipolygon = type(coords_commune[0])==list
    
    for i in range(len(dataframe)):
        lt = float(str(np.array(dataframe['Latitude'])[i]))
        ln = float(str(np.array(dataframe['Longitude'])[i]))
        if is_multipolygon :
            count = 0
            for h in range(n):
                if coords_maps_sector.is_in_sector(coords_commune[h],(ln,lt)):
                    count+=1
            if count>0:
                U.append(ln)
                V.append(lt)
        else :            
            if coords_maps_sector.is_in_sector(coords_commune,(ln,lt)):
                U.append(ln)
                V.append(lt)
    
    
    if not is_multipolygon :
        n = 1
    global X,Y
    for k in range(n) :
        if is_multipolygon :
            m = len(coords_commune[k])
        else :
            m = len(coords_commune)
        codes = [Path.MOVETO]
        for u in range(m-2):
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
        
        
        
        if is_multipolygon :
            bbPath = Path(coords_commune[k], codes)   
            for i,j in coords_commune[k]:
                X.append(i)
                Y.append(j)
        else :
            bbPath = Path(coords_commune, codes)  
            for i,j in coords_commune:
                X.append(i)
                Y.append(j)

        ax = fig.add_subplot(111)
        patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
        ax.add_patch(patch)
    plt.plot(U,V,'ro')
    ax.set_xlim(min(X),max(X))
    ax.set_ylim(min(Y),max(Y))
    plt.show()
    
    
def search_for_place(place_type, coordinates_commune):
    global type_recherche
    global coords_commune
    global research_coordinates
    global places_dataframe
    
    places_dataframe = pd.DataFrame({'Name':[],'Latitude':[],'Longitude':[],'Type':[],'Place_id':[]})
    
    coords_commune = coordinates_commune
    research_coordinates = coords_maps_sector.maps_points_list(coords_commune)
    type_recherche = place_type    
    
    for i in range(len(research_coordinates)):
        longi, lati  = research_coordinates[i]
        fetch_places(lati,longi,radius)

    
    display_places(places_dataframe)
    return places_dataframe
