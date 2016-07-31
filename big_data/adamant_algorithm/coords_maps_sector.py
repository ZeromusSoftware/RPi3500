# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:38:10 2016

@author: william
"""



import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from math import *

distance_between_points = 1000




def is_in_sector(sector_coords, point_coords):
    
    codes = [Path.MOVETO]
    for i in range(len(sector_coords)-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)

    bbPath = Path(sector_coords, codes)
    
    return bool(bbPath.contains_point(point_coords))
    
    
def neighbour_points(focalised_point):
    
    la,lo = focalised_point     
    
    pt1 = (la, round( lo - acos((cos(distance_between_points * 57.30/6371000)-sin(radians(la))**2)/cos(radians(la))**2), 6))
    pt2 = (la, round( lo + acos((cos(distance_between_points * 57.30/6371000)-sin(radians(la))**2)/cos(radians(la))**2), 6))
    pt3 = (round(la + distance_between_points * 57.30/6371000, 6), lo)  
    pt4 = (round(la - distance_between_points * 57.30/6371000, 6), lo)
    
    return [pt1,pt2,pt3,pt4]

def distance(lat1,long1,lat2,long2):
    
    r = sin(radians(lat1))*sin(radians(lat2))+cos(radians(lat1))*cos(radians(lat2))*cos(radians(long1-long2))
    epsilon = 10**(-10)    
    
    if abs(1-r) < epsilon :
        r = 1
    elif abs (r) < epsilon :
        r = 0
        
    return acos(r)*6371000

    
def area_for_polygon(polygon):
    result = 0
    imax = len(polygon) - 1
    for i in range(0,imax):
        result += (polygon[i][0] * polygon[i+1][1]) - (polygon[i+1][0] * polygon[i][1])
    result += (polygon[imax][0] * polygon[0][1]) - (polygon[0][0] * polygon[imax][1])
    return result / 2.

def centroid_for_polygon(polygon):
    area = area_for_polygon(polygon)
    imax = len(polygon) - 1

    result_x = 0
    result_y = 0
    for i in range(0,imax):
        result_x += (polygon[i][0] + polygon[i+1][0]) * ((polygon[i][0] * polygon[i+1][1]) - (polygon[i+1][0] * polygon[i][1]))
        result_y += (polygon[i][1] + polygon[i+1][1]) * ((polygon[i][0] * polygon[i+1][1]) - (polygon[i+1][0] * polygon[i][1]))
    result_x += (polygon[imax][0] + polygon[0][0]) * ((polygon[imax][0] * polygon[0][1]) - (polygon[0][0] * polygon[imax][1]))
    result_y += (polygon[imax][1] + polygon[0][1]) * ((polygon[imax][0] * polygon[0][1]) - (polygon[0][0] * polygon[imax][1]))
    result_x /= (area * 6.0)
    result_y /= (area * 6.0)

    return (result_x, result_y)

total = 0

X,Y = [],[]
def maps_points_list(coords_canton):
    
    global total    
    
    is_multipolygon = type(coords_canton[0])==list
    
    return_coords = []
    global i
    i = 0
    def add_research_points(coords):
        global i
        
        continue_loop = True
        
        while continue_loop :
            focalised_point = return_coords[i]
        
            four_points_list = neighbour_points(focalised_point)
    
            for k in four_points_list :
                if is_in_sector(coords,k):
                    
                    count = 0
                    for j in return_coords:
                
                        a,b = j
                        c,d = k
                
                        if distance(a,b,c,d)< (distance_between_points/1.5) :
                            count+=1
            
                    if count==0:
                        return_coords.append(k)   
            i += 1
    
            if i > len(return_coords)-1:
                continue_loop = False
                
    if is_multipolygon :
        for a in range(len(coords_canton)):
            p = centroid_for_polygon(coords_canton[a])
            return_coords.append(p)
            add_research_points(coords_canton[a])
    else :
        p = centroid_for_polygon(coords_canton)
        return_coords.append(p)
        add_research_points(coords_canton)
        
    
    
    fig = plt.figure("Points Generated")
    
    
    n = len(coords_canton)
    m = 0
    
    if not is_multipolygon :
        n = 1
    global X,Y
    for k in range(n) :
        if is_multipolygon :
            m = len(coords_canton[k])
        else :
            m = len(coords_canton)
        codes = [Path.MOVETO]
        for u in range(m-2):
            codes.append(Path.LINETO)
        codes.append(Path.CLOSEPOLY)
        
        '''Use this code to plot the figure of the sector'''
        
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
    
    U=[]
    V=[]
    for n,m in return_coords :
        U.append(n)
        V.append(m)
    plt.plot(U,V,'ro')
    
    ax.set_xlim(min(X),max(X))
    ax.set_ylim(min(Y),max(Y))
    plt.show()
    
    total+=len(return_coords)
    print(str(total) + " points")
    return return_coords
