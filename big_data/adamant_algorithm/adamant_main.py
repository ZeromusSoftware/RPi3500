# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import maps_api
import sector_boundaries as sb
import time
from matplotlib.path import Path
import matplotlib.patches as patches

sectors = {"Bouches-du-Rhône":["Aix-en-Provence-1","Aix-en-Provence-2","Allauch","Arles","Aubagne","Berre-l'Étang","Châteaurenard","Gardanne","Istres",
                               "La Ciotat","Marignane","Marseille-1","Marseille-2","Marseille-3","Marseille-4","Marseille-5","Marseille-6",
                               "Marseille-7","Marseille-8","Marseille-9","Marseille-10","Marseille-11","Marseille-12","Martigues","Pélissanne",
                               "Salon-de-Provence-1","Salon-de-Provence-2","Trets","Vitrolles"]}



### values given by the formular filled on internet
concurrent_place_type = 'parking'
coeff_demography = 2



def get_all_places():

    coords_cantons_list = []
    places_df_list = []
              
    for departement,cantons in sectors.iteritems():
        for canton in cantons:
            coords_canton = sb.get_boundaries(canton)
            coords_cantons_list.append(coords_canton)
            places_df_list.append(maps_api.search_for_place(concurrent_place_type,coords_canton))
    
    return places_df_list, coords_cantons_list
    



def get_all_demography():
    
    population_canton = []
    for departement,cantons in sectors.iteritems():
        demography_df = pd.read_excel('DataBases/'+str(departement)+'/pop_cantons_'+str(departement)+'.xls',skiprows=7)
        for canton in cantons:
            population_canton.append(int(demography_df[demography_df['Nom du canton'] == canton]['Population totale']))
                
    return population_canton
    
    
def get_all_areas():
    
    area_canton = []
    for departement,cantons in sectors.iteritems():
        for canton in cantons:
            coordinates = sb.get_boundaries(canton)
            if type(coordinates[0])==list:
                somme = 0
                for i in range(len(coordinates)):
                    somme += sb.area_for_polygon(coordinates[i])
                area_canton.append(somme)
            else:
                area_canton.append(sb.area_for_polygon(coordinates))
    return area_canton

def show_graphic_results(notes,coords_cantons_list):
    
    
    colors = []
    for i in range(11):
        colors.append((1,i*0.1,0))
    for j in range(1,11):
        colors.append((1-j*0.1,1,0))
    
    
    
    fig = plt.figure('Resultat')
    X,Y = [],[]
    for i in range(len(notes)):
        n = len(coords_cantons_list[i])
        m=0
        is_multipolygon = type(coords_cantons_list[i][0])==list
        if not is_multipolygon :
            n = 1
        
        for k in range(n) :
            if is_multipolygon :
                m = len(coords_cantons_list[i][k])
            else :
                m = len(coords_cantons_list[i])
            codes = [Path.MOVETO]
            for u in range(m-2):
                codes.append(Path.LINETO)
            codes.append(Path.CLOSEPOLY)
    
            if is_multipolygon :
                bbPath = Path(coords_cantons_list[i][k], codes)  
                for a,b in coords_cantons_list[i][k]:
                    X.append(a)
                    Y.append(b)
            else :
                bbPath = Path(coords_cantons_list[i], codes)  
                for a,b in coords_cantons_list[i]:
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
    
    places_df_list, coords_cantons_list = get_all_places()    
    
    notes_dem = {}
    just_notes_dem = []
    
    population = get_all_demography()
    area = get_all_areas()
    
    for j in sectors:
        for i in range(len(sectors[j])):
            if len(places_df_list[i])>0:
                note = population[i]/(area[i] * len(places_df_list[i]))
                notes_dem[sectors[j][i]] = note
            else :
                note = population[i]/area[i]
                notes_dem[sectors[j][i]] = note
            just_notes_dem.append(note)
    notemax = max(just_notes_dem)
    
    notes_ponderees = {p:int(round(q*20/notemax,0)) for p,q in notes_dem.iteritems()}
    just_notes_ponderees = [int(round(k*20/notemax,0)) for k in just_notes_dem]
    
    
    finish_time = time.time()
    
    show_graphic_results(just_notes_ponderees,coords_cantons_list)

    print str(finish_time-start_time)+" seconds"    
    
    return notes_ponderees
    
notes = note_giver()
print(notes)


        