# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 17:58:36 2016

@author: william
"""

import json
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


def area_for_polygon(corners):
    
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area*111.194926645*111.177990689

def segments(p):
    return zip(p, p[1:] + [p[0]])


def get_boundaries(sector):
    filename = sector+".json"
    with open('DataBases/Cantons_Boundaries/' + filename) as f:
        data = json.load(f)

    coords_canton = []
    is_multipolygon = False

    k = 0
    for i in range(len(data['features'])):
        
        TYPE = data['features'][i]['geometry']['type']
        if TYPE == "MultiPolygon" :
            is_multipolygon = True
            for u in range(len(data['features'][i]['geometry']['coordinates'])):
                
                coords_canton.append([])
                for [lng,lat] in data['features'][i]['geometry']['coordinates'][u][0]:
                    coords_canton[k].append((lng,lat))
                area = area_for_polygon(coords_canton[k])
                if area<10**(-4):
                    coords_canton.pop(k)
                    k-=1
                k+=1
                
        elif TYPE == "Polygon" :
            if is_multipolygon :
                coords_canton.append([])
                for [lng,lat] in data['features'][i]['geometry']['coordinates'][0]:
                    
                    coords_canton[k].append((lng,lat))
                    
                area = area_for_polygon(coords_canton[k])
                if area<10**(-4):
                        coords_canton.pop(k)
                        k-=1
            else :
                for [lng,lat] in data['features'][i]['geometry']['coordinates'][0]:
                    coords_canton.append((lng,lat))
            k+=1
    
    '''Use this code to plot the figure of the sector
    
    fig = plt.figure(sector)
    
    
    n = len(coords_canton)
    if n==0:
        return []
    else :
        if type(coords_canton[0])==tuple:            
            print (sector + "'s corners : " + str(n))
        else :
            somme = 0
            for i in range(len(coords_canton)):
                somme+=len(coords_canton[i])
            print (sector + "'s corners : " + str(somme))
    
    m = 0
    
    if not is_multipolygon :
        n = 1
    X,Y = [],[]
    for k in range(n) :
        if is_multipolygon :
            m = len(coords_canton[k])
        else :
            m = len(coords_canton)
        codes = [Path.MOVETO]
        for u in range(m-2):
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
        
        
        
        if is_multipolygon :
            bbPath = Path(coords_canton[k], codes)  
            for i,j in coords_canton[k]:
                X.append(i)
                Y.append(j)
        else :
            bbPath = Path(coords_canton, codes)  
            for i,j in coords_canton:
                X.append(i)
                Y.append(j)

        ax = fig.add_subplot(111)
        patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
        ax.add_patch(patch)
    
    ax.set_xlim(min(X),max(X))
    ax.set_ylim(min(Y),max(Y))
    plt.show()'''
    
    return coords_canton
    
#get_boundaries("Marseille-11")