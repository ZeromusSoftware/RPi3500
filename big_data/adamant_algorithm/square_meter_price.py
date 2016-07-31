# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:25:06 2016

@author: william
"""

import urllib 
import pygeoj
import unicodedata
import pandas as pd

sectors = {"Bouches-du-Rhône":[]}
file13 = pygeoj.load("Data/france-geojson/departements/13/communes.geojson")
for feature in file13:
    s = feature.properties['nom']
    sectors["Bouches-du-Rhône"].append(s)
    
communes = sectors["Bouches-du-Rhône"]

def refresh_sqm_price():
    prix,evolution = [],[]
    
    for s in communes:
        
        normalized_str = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
        commune = "v_"+normalized_str.lower().replace("'","-").replace(" ","-")+"_13"
        if "marseille" in commune:
            try :
                arrondissement = str(int(commune[12:14]))
            except :
                arrondissement = "0"+commune[12]            
            commune = "v_marseille_130"+arrondissement    
        
        page=urllib.urlopen('http://www.efficity.com/prix-immobilier-m2/'+commune) 
        strpage=page.read()
        print(commune)
        try:
            stringevolutiontoseek = '<p class="evol-values">'
    
            indexevol = strpage.index(stringevolutiontoseek)
    
            strevolution = strpage[indexevol+len(stringevolutiontoseek):indexevol+len(stringevolutiontoseek)+4]
            floatevolution = float(strevolution.replace(" ",""))
            print(floatevolution)
            evolution.append(floatevolution)
            
        except :
            print("evolution raté..")
            evolution.append(0.0)
            
        try:
            stringpricetoseek = '<div class="price-per-sqm-width price-per-sqm-values">'
            indexprice = strpage.index(stringpricetoseek)
            firstcut = strpage[indexprice+len(stringpricetoseek):indexprice+len(stringpricetoseek)+50]
            index1 = firstcut.index('<strong>')+len('<strong>')
            index2 = firstcut.index('</strong>')+1
            strprix = firstcut[index1:index2]
    
            intprix = 0
    
            n = len(strprix)
            k = 1
            for i in range(n):
                try:
                    if type (int(strprix[n-i-1]))==int:
                        intprix+=k*int(strprix[n-i-1])
                        k=k*10
                except:
                    pass
            print(intprix)
            prix.append(intprix)
        except:
            return ("prix raté..")
            
    rows = []
    for i in range(len(communes)):
        rows.append((communes[i],prix[i],evolution[i]))
    df = pd.DataFrame(rows,columns = ["Commune","Prix du m2","Evolution sur 3 mois"])
    df.to_csv('Data/square_meters_price.csv')
    
    return True