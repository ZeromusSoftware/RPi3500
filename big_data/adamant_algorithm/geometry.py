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

X,Y = [],[]
def display_sector(sector,coords):
    
    '''Use this code to plot the figure of the sector'''
    
    fig = plt.figure(sector)
    
    global X,Y
    
    m = len(coords)
    codes = [Path.MOVETO]
    for u in range(m-2):
        codes.append(Path.LINETO)
    codes.append(Path.CLOSEPOLY)
        
        
    bbPath = Path(coords, codes)  
    for i,j in coords:
        X.append(i)
        Y.append(j)

    ax = fig.add_subplot(111)
    patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
    ax.add_patch(patch)
    ax.set_xlim(min(X),max(X))
    ax.set_ylim(min(Y),max(Y))
    
    plt.show()
    