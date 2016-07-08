# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np





france_regions = ["Alsace","Aquitaine","Auvergne","Basse-Normandie","Bourgogne","Bretagne","Centre","Champagne-Ardenne","Corse",
                  "Franche-Comté","Guadeloupe","Guyane","Haute-Normandie","Île-de-France","La Réunion","Languedoc-Roussillon","Limousin",
                  "Lorraine","Martinique","Midi-Pyrénées","Nord-Pas-de-Calais","Pays de la Loire","Picardie","Poitou-Charentes",
                  "Provence-Alpes-Côte d'Azur","Rhône-Alpes"]
                  
                  
df = pd.read_excel('DataBases/pop_communes_2013.xls')

data = np.array(df)

print(type(data[34][1]))

notes_regions = {}


for i in france_regions :
    pop_totale = 0.
    nbre_communes = 0
    for j in range(len(data)) :
        if str(data[j][1]) == i:
            pop_totale += data[j][9]
            nbre_communes += 1
    notes_regions[i] = int(pop_totale/nbre_communes)
    
print(notes_regions)
       