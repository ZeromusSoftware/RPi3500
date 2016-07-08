# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np





france_regions = ["Alsace","Aquitaine","Auvergne","Basse-Normandie","Bourgogne","Bretagne","Centre","Champagne-Ardenne","Corse",
                  "Franche-Comté","Guadeloupe","Guyane","Haute-Normandie","Île-de-France","La Réunion","Languedoc-Roussillon","Limousin",
                  "Lorraine","Martinique","Midi-Pyrénées","Nord-Pas-de-Calais","Pays de la Loire","Picardie","Poitou-Charentes",
                  "Provence-Alpes-Côte d'Azur","Rhône-Alpes"]
                  
                  
data = open('regions.xls','rw')
k = data.write(np.array(france_regions))
print (k)

df = pd.