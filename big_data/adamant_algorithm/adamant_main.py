# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import maps_api
import geometry as gm
import time
from matplotlib.path import Path
import matplotlib.patches as patches
import pygeoj
import square_meter_price as sqm

sectors = {"Bouches-du-Rhône":[]}

### values given by the formular filled on internet
concurrent_place_type = 'parking'
coeff_demography = 2
coords_communes_list = []

file13 = pygeoj.load("Data/france-geojson/departements/13/communes.geojson")
for feature in file13:
    sectors["Bouches-du-Rhône"].append(feature.properties['nom'])
    correct_coords = []    
    for [ln,lat] in feature.geometry.coordinates[0]:
        correct_coords.append((ln,lat))
    coords_communes_list.append(correct_coords)


def refresh_database():

    for departement,commune in sectors.iteritems():
        for i in range(len(commune)):
            print('refreshing data of '+ commune[i])
            
            if i>=commune.index('Istres'):            
                places_dataframe = maps_api.search_for_place('',coords_communes_list[i])
                places_dataframe.to_csv("Data/Places/"+commune[i]+"_places.csv")
    sqm.refresh_sqm_price()
                
    
refresh_database()


def get_all_demography():
    
    population_communes = []
    for departement,communes in sectors.iteritems():
        demography_df = pd.read_excel('Data/'+str(departement)+'/pop_communes_'+str(departement)+'.xls',skiprows=7)
        for commune in communes:
            names_communes = demography_df['Nom de la commune']
            name_matched = False
            i=0
            while not(name_matched) and i<len(names_communes):
                if commune.lower().replace(" ","") == names_communes[i].lower().replace(' ',''):
                    population_communes.append(int(demography_df['Population totale'][i]))
                    name_matched = True
                i+=1
            if i>len(names_communes):
                return("Error, names didn't match")
                
    return population_communes
    
    
def get_all_areas():
    
    
    
    area_commune = []
    
    for coords in coords_communes_list:
        area_commune.append(gm.area_for_polygon(coords))
        
    return area_commune
    
def get_population_density():

        
    population = get_all_demography()
    area = get_all_areas()
    
    density = []
    for i in range(len(population)):
        density.append(population[i]/area[i])
        
    return density
    
def get_all_prices():
    
    df = pd.read_csv('Data/square_meters_price.csv',index_col = 'Commune')
    prix,evolution = [],[]
    
    for i in range(len(df.index)):
        prix.append(df["Prix du m2"][i])
        evol = round(df["Evolution sur 3 mois"][i],1)
        if evol == -0.0:
            evol = 0.0
        evolution.append(evol)
    
    return (prix,evolution)
    

def show_graphic_results(notes):
    
    
    colors = []
    for i in range(11):
        colors.append((1,i*0.1,0))
    for j in range(1,11):
        colors.append((1-j*0.1,1,0))
    
    
    
    fig = plt.figure('Resultat')
    X,Y = [],[]
    for i in range(len(notes)):
        m = len(coords_communes_list[i])
        codes = [Path.MOVETO]
        for u in range(m-2):
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
    
        bbPath = Path(coords_communes_list[i], codes)  
        for a,b in coords_communes_list[i]:
            X.append(a)
            Y.append(b)

        ax = fig.add_subplot(111)
        patch = patches.PathPatch(bbPath, facecolor=colors[notes[i]], lw=2)
        ax.add_patch(patch)
            
    ax.set_xlim(min(X),max(X))
    ax.set_ylim(min(Y),max(Y))
    plt.show()
        

def note_giver():
    
    start_time = time.time()
    
    places_df_list = []
    for departement,communes in sectors.iteritems():
        for commune in communes:
            raw_dataframe = pd.read_csv('Data/Places/'+commune+'_places.csv')
            places_df_list.append(raw_dataframe[raw_dataframe.Type.str.contains(concurrent_place_type)==True])
    
    notes_dem = {}
    just_notes_dem = []
    
    density = get_population_density()
    price,evolution = get_all_prices()
    
    for j in sectors:
        for i in range(len(sectors[j])):
            n = len(places_df_list[i])
            if n==0:
                n=1
            print(sectors[j][i],n)
            note = density[i]/(n * price[i] + 1000*evolution[i])
            notes_dem[sectors[j][i]] = note
            just_notes_dem.append(note)
    notemax = max(just_notes_dem)
    
    notes_ponderees = {p:int(round(q*20/notemax,0)) for p,q in notes_dem.iteritems()}
    just_notes_ponderees = [int(round(k*20/notemax,0)) for k in just_notes_dem]
    print(just_notes_ponderees)
    
    finish_time = time.time()
    
    show_graphic_results(just_notes_ponderees)

    print str(finish_time-start_time)+" seconds"    
    
    return notes_ponderees
    
notes = note_giver()
print(notes)


'''To see the sector we are working on

for i in range(len(sectors['Bouches-du-Rhône'])):
    gm.display_sector("13",coords_communes_list[i])
    
    '''