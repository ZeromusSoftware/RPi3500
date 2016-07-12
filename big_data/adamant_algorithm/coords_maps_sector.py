# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:38:10 2016

@author: william
"""

''' Ce fichier va se charger de déterminer les coordonnées gps des endroits où effectuer les requêtes maps de rayon
    350m afin de quadriller la ville en question. Pour cela, il est nécessaire de fournir des coordonnées frontières 
    de la ville qui auront été relevées à la main et placés dans une liste de tuples (coords)'''


import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from math import *


distance_between_points = 1000

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



def is_in_sector(sector_coords, point_coords):
    
    codes = [Path.MOVETO]
    for i in range(len(sector_coords)-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)

    bbPath = Path(sector_coords, codes)
    
    return bool(bbPath.contains_point(point_coords))
    
    
def neighbour_points(focalised_point):
    
    lo,la = focalised_point     
    
    pt1 = (round( lo - acos((cos(distance_between_points * 57.30/6371000)-sin(radians(la))**2)/cos(radians(la))**2), 6), la)
    pt2 = (round( lo + acos((cos(distance_between_points * 57.30/6371000)-sin(radians(la))**2)/cos(radians(la))**2), 6), la)
    pt3 = (lo, round(la + distance_between_points * 57.30/6371000, 6))  
    pt4 = (lo, round(la - distance_between_points * 57.30/6371000, 6))
    
    return [pt1,pt2,pt3,pt4]

def distance(lat1,long1,lat2,long2):
    
    r = sin(radians(lat1))*sin(radians(lat2))+cos(radians(lat1))*cos(radians(lat2))*cos(radians(long1-long2))
    epsilon = 10**(-10)    
    
    if abs(1-r) < epsilon :
        r = 1
    elif abs (r) < epsilon :
        r = 0
        
    return acos(r)*6371000


def maps_points_list():
    return_coords = [coords_marseille[0]]
    continue_loop = True
    i = 0

    while continue_loop :
    
        focalised_point = return_coords[i]
        
        four_points_list = neighbour_points(focalised_point)
    
        for k in four_points_list :
        
            if is_in_sector(coords_marseille,k):
            
                count = 0
                for j in return_coords:
                
                    b,a = j
                    d,c = k
                
                    if distance(a,b,c,d)< (distance_between_points-100) :
                        count+=1
            
                if count==0:
                    return_coords.append(k)   
        i += 1
    
        if i > len(return_coords)-1:
            continue_loop = False
        
    X=[]
    Y=[]
    for n,m in return_coords :
        X.append(n)
        Y.append(m)
            
    codes = [Path.MOVETO]
    for u in range(len(coords_marseille)-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)
    
    '''Use this code to plot the figure of the sector'''
    bbPath = Path(coords_marseille, codes)

    
    fig = plt.figure("Points Generated")
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
    ax.add_patch(patch)
    plt.plot(X,Y,'ro')
    ax.set_xlim(5.26,5.53)
    ax.set_ylim(43.20,43.40)
    plt.show()
    
    print(len(return_coords))
    return return_coords
