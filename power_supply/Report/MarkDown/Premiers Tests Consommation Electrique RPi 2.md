#Premiers Tests Consommation Electrique Raspberry Pi 2
****

##Consommation Théorique

* La [Raspberry Pi Foundation](https://www.raspberrypi.org) préconise une alimentation minimale de 1,8 A. Comme tout bon étudiant scientifique, j'ai cherché à coroborer ces dires.

##Mesures

###Principe de Mesure

J'ai effectué ces mesures avec un Ampèremètre en série du circuit d'alimentation et du RPi. On module la charge CPU en lançant des applications plus ou moins gourmande en ressources.

### Résultats
	
| CPU Load (%) |     Courant Consommé (A) |
| -------------| ----------------------:  |
| 2%           |          0,260           |
| 26%          |          0,308           |
| No Data      |          0,602           |
	
	
	
##Analyse
	
* L'état “No Data“ correspondait au premier allumage de notre RPi, quand il n'y avait pas d'OS installé.
* L'augmentation d'une charge processeur de 24% n'emploie que 0,05 A de plus.
* Le Raspberry consomme très peu, on relève ici un courant maximale de 0,3 A en utilisation.


## Conclusion

Nos tests révèlent que le Raspberry est un appareil très peu gourmand en énergie, consommation inferieure ou égal à 3 Watts. Il apparaît aussi que nous sommes encore bien loin des 1,8 A annoncés par la Raspberry Pi Foundation.  
Afin d'augmenter sensiblement la consommation, nous pousserons cette carte au maximum de ses capacitées en essayant d'encoder une vidéo en Full HD par exemple, ou alors de provoquer ceci par des lignes de commandes.

*To be continued*
   


	
	



