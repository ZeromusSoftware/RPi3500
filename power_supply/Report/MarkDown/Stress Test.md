#Stress Test
---
###Préambule

Suite à nos tests de la semaine dernière, nous avons continué nos recherches et sommes parvenus à notre but final ! Nous avons pousser nos bêtes dans leurs derniers retranchements, cela afin de mesurer la consommation maximale de nos Rapsberry Pi 2.

###Principe de Mesure 

Nous avons donc effectué un Stress Test, communément appelé ainsi. Cela consiste en utilisant à 100% la puissance fourni par nos petits RPi2. Pendant ce temps, nous avons mesuré la consommation électrique de ces petites bébêtes.

###Mode Opératoire Détaillé

A l’aide d’une ligne de commande entré dans le terminal des Pi sous raspbian, nous pouvons augmenter par palier de 25% la charge du CPU (Processeur). 

	 yes > /dev/null&

Dans ce cas nous avons pu effectué nos mesures à l’aide d’un ampèremètre branché en série du circuit d’alimentation.
En parallèle nous refroidissions aussi le processeur à l’aide d’un ventilateur, afin de ne pas le faire surchauffer, ce qui pourrait l’endommager prématurément.

###Mesures

| Charge CPU (%) | Consommation (A) | 
| :-----------   | :--------------: | 
| 0 %   		    |	     0,260      |
| 25 %           |       0,283      | 
| 50 %           |       0,318      | 
| 75%            |       0,355      |
| 100%           |       0,395      |


Nous pouvons alors extraire une courbe presque linéaire :




![Consommation Electrique f() Charge Processeur](http://imagizer.imageshack.us/v2/440x320q90/923/ISoakE.png)

###Analyse Des Mesures

Cela est pour le moins déconcertant mais le RPi2 ne consomme pas plus de 0,4 A contrairement aux caractéristiques données par la Raspberry Pi Foundation qui préconise une alimentation de 1,8 A minimum.

La consommation est quasi proportionnelle à la charge processeur.
Néanmoins ce qui est positif pour nous c’est qu’ainsi, le courant d’alimentation ne devra point être très important sur l’ensemble du système. Ainsi nous aurons besoin que de cables dimensionnées pour faire passer tout au plus 2 A sous 5V. Ce qui implique un coût bien moindre et donc largement maitrisé.

###Conclusion

Nous pouvons ainsi conclure sur une consommation bien plus faible qu'indiqué pour nos petits RPi et ce même à pleine puissance, Alors notre alimentation pourra aisément alimenter l’ensemble de notre sytème et bien plus !

