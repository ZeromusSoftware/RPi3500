#Dimmensionnement Alimentation
---

###Composition du Système

Notre Data Center se compose de plusieurs éléments consommant de l'énergie :

* 4 Raspberry Pi 2
* 1 Raspberry Pi B+
* 1 Switch Ethernet
* 4 Ventilateurs

###Spécifications Constructeurs
Pour la partie Réseau et Informatique

* Raspberry Pi 2 : Il doit être alimenté en 5V avec un courant minimum de 1,8 A
* Raspberry Pi B+ : Il doit être alimenté en 5V avec un courant minimum de 0,7 A
* Switch Ethernet Netgear GS608 : Il doit être alimenté en 12V et consommme au maximum 0,5 A 

Pour la partie Refroidissement :

* 2 ventilateurs consommant 0,45 A chacun et alimenté en 12V
* 1 ventilateur consommant 0,7 A et alimenté en 12V
* 1 ventilateur consommant 0,16 A et alimenté en 12V

###Courant Nécéssaire

Nous pouvons établir le courant nécéssaire pour l'alimentation du système 

* Sur le 5V : 4 x 1,8 + 0,7 = **7,9A**
* Sur le 12V : 0,5 + 2 x 0,45 + 0,7 + 0,16 = **2,26A**

###Solution Apportée
 Nous avons récupéré une alimentation de PC 500W. Ces générateurs sont destinés à alimenter des composants éléctroniques fragiles, elle sera donc particulièrement bien adapté à l'alimentation de notre Data Center.
 
 De plus selon ses caractéristiques, elle peut fournir :
 
 * Sur le 5V : **36A**
 * Sur le 12V : **20A**

Elle est donc largement dimmensionnée pour notre système et lui permettra de nombreuses évolutions.




