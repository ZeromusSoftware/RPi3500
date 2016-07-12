# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:52:22 2016

@author: william
"""

import urllib, json
import time
import pandas as pd
from math import *
import coords_maps_sector
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


coords_marseille = [
    (5.282416, 43.353962),
    (5.283155, 43.355931),
    (5.281646, 43.356901),
    (5.280039, 43.360451),
    (5.279111, 43.362580),
    (5.279716, 43.368952), 
    (5.297325, 43.387685), 
    (5.322296, 43.368473), 
    (5.337811, 43.377080), 
    (5.355163, 43.374705), 
    (5.350917, 43.382663),
    (5.370581, 43.389544),
    (5.374465, 43.371723),
    (5.439769, 43.390426),
    (5.464046, 43.360251),
    (5.450937, 43.341186),
    (5.517212, 43.319995),
    (5.528865, 43.295970),
    (5.502889, 43.281126),
    (5.510071, 43.200334),
    (5.342123, 43.213331),
    (5.352257, 43.288802),
    (5.279716, 43.368952)
    ]


research_coordinates = coords_maps_sector.maps_points_list()

radius = 1000/(2**(1/2))
type_recherche = 'parking'
api_key1 = 'AIzaSyBEK3CzYIaelEgSQkUcpbWJs5MCbAxtrIk'
api_key2 = 'AIzaSyBPPv6sz-PjrCWbAiw6-zBcRlx8oAWh3RI'


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
    response = urllib.urlopen(MyUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw)
    return jsonData


global places_dataframe
places_dataframe = pd.DataFrame({'Name':[],'Latitude':[],'Longitude':[],'Vicinity':[],'Type':[],'Place_id':[]})


def fetch_places(lat,lng,rad,key):

    global places_dataframe

    response = GoogPlac(lat,lng,rad,type_recherche,key,False)
    data = response['results']
    
    page_to_read = True
    
    
    while page_to_read :
        for i in range(len(data)):
                
            df_to_append = pd.DataFrame({
            'Name':[str(data[i]['name'])],
            'Latitude':[str(data[i]['geometry']['location']['lat'])],
            'Longitude':[str(data[i]['geometry']['location']['lng'])],
            'Vicinity':[str(data[i]['vicinity'])],
            'Type':[data[i]['types']],
            'Place_id':[str(data[i]['place_id'])]})
            
            if  not (str(data[i]['place_id']) in np.array(places_dataframe['Place_id'])):
                places_dataframe = places_dataframe.append(df_to_append)
                
              
        
        try :
            page_to_read = response['next_page_token']!= False
        except :
            page_to_read = False
        
        
        
        if page_to_read:       
            print ("Wait..")
            time.sleep(1.5) # delay for 1.5 seconds
            response = GoogPlac(lat,lng,rad,type_recherche,key,response['next_page_token'])
            data = response['results']
    
    print (len(places_dataframe))



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


def display_places(dataframe):
    
    X=[]
    Y=[]
    
    for i in range(len(dataframe)):
        X.append(float(str(dataframe['Longitude'][i])))
        Y.append(float(str(dataframe['Latitude'][i])))
    
    codes = [Path.MOVETO]
    for u in range(len(coords_marseille)-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)
    
    '''Use this code to plot the figure of the sector'''
    bbPath = Path(coords_marseille, codes)

    
    fig = plt.figure("Places found")
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
    ax.add_patch(patch)
    plt.plot(X,Y,'ro')
    ax.set_xlim(5.26,5.53)
    ax.set_ylim(43.20,43.40)
    
    plt.show()
    
    

for i in range(len(research_coordinates)-1):
    longi, lati = research_coordinates[i]
    print (lati,longi, " et i= "+str(i))
    fetch_places(lati,longi,radius,api_key2)
    
print (places_dataframe.head())
display_places(places_dataframe)
