# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:05:44 2016

@author: william
"""


import quandl
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import style
#style.use('ggplot')


""" Cours 1

web_stats= {'Day':[1,2,3,4,5,6], 'Visitors':[43,54,73,84,32,44], 'Bounce_Rate':[23,43,23,54,54,32]}

df = pd.DataFrame(web_stats)

print (df)


print(df.set_index('Day'))


print(df['Bounce_Rate'].tolist())
"""

# Cours 2

"""db = quandl.get("INSEE/29_000067699_A", authtoken="1AAV-23SHR15ewBJtmSX")

print (db)


data = pd.read_csv('INSEE-29_000067699_A.csv')

data.set_index('Date', inplace=True)

print(data.head())

data.to_csv('INSEE-29_000067698_A.csv')

data2 = pd.read_csv('INSEE-29_000067698_A.csv', index_col=0)

print(data2)

data2.columns = ['Population'] #change column name

print (data2)


data3 = pd.read_csv('INSEE-29_000067699_A.csv')
data3.rename(columns={'Value':'Population'}, inplace = True)
data3 = data3.set_index('Date')
print(data3.head())"""


#Entrainement + avance projet

col_titles = ['Departement','Slug','Nom','Nom simple','Nom reel','Nom soundex','Nom metaphone','Code postal',
'Numéro de commune','Code commune','truc inconnu','Arrondissement','Canton','Population 2010','Population 1999',
'Population 2012','Densité 2010','Superficie','longitude (degre)','latitude (degre)','longitude (GRD)','latitude (GRD)',
'longitude (DMS)','latitude (DMS)','Altitude min','Altitude max']


df = pd.read_csv("villes_france.csv",names = col_titles)

print(df.loc[4440][4])
print(df.loc[4440][18])
print(df.loc[4440][19])


