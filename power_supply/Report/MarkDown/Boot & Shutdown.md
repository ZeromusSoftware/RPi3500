#Boot & Shutdown
---

###Préambule

Afin de bien dimmensionner nos batteries et notre alimentation, nous recherchons toujours la consommation maximale de nos Raspberry. Ainsi, c'est dans ce cadre que s'inscrit ce rapport. Nous avons alors eu l'idée de mesurer la consommation de nos mini-ordinateurs dans des phases critiques.

###Principe de Mesure

La phase d'allumage est critique au sens où le Pi se doit de disposer de tout sa puissance afin de se mettre en route, de tester le fonctionnement de tout ses composants. C'est ici que l'on pourrait atteindre un pic de consommation.	

La phase d'extinction est quant à elle importante afin de constater la consommation du Pi quand il est éteint.

Nous mesurerons alors la consommation de notre Pi lors de ces deux phases.

###Mode Opératoire Détaillé

Nous brancherons en série du circuit d'alimentation un Ampèremetre qui nous afficheras alors la consommation instantanée du RPi.

Nous restranscrirons toutes nos mesures sous forme de graphiques que nous analyserons.

###Mesures
--

1. Démarrage

 ![Boot](https://github.com/ZeromusSoftware/RPi3500/blob/master/power_supply/Report/Ressources/Boot%20RPi.png?raw=true)

2. Extinction


![Shutdown](https://github.com/ZeromusSoftware/RPi3500/blob/master/power_supply/Report/Ressources/Shutdown%20RPi.png?raw=true)

###Analyse des Courbes
--

#####Démarrage

* Nous pouvons d'abord voir un pic à 0,58 Ampères ce qui est la plus haute valeur constatée jusqu'à présent.
* La phase de démarrage dure, avant que tout soit prêt à fonctionner, environ une minute ce qui correspond à la fin du dernier pic de consommation sur la courbe.
* Aussi nous pouvons noter la stabilisation de la consommation au bout d'environ 145 secondes.


#####Extinction

* La phase d'extinction dure environ 40 secondes.
* Nous pouvons observer un pic à plus de 0,530 Ampères, ensuite le courant décroit à nouveau puis un nouveau pic à 10 secondes de la fin de la phase puis presque le silence radio, le Pi à rendu son dernier souffle.
* En étant éteint, notre Raspberry consomme tout de même près de 60 mA ce qui parait assez élevé.


###Conclusion

Le pic de consommation confirme alors nos hypothèses, le RPi consomme le plus de courant durant sa phase d'allumage. Il faudra alors calquer nos dimmensionnement de nos alimentations sur ces résultats.
	
Aussi il paraît encore et toujours très peu gourmand en énergie, moins de 3 Watts de puissance consommé ce qui en constitue un parfait équipement pour rester allumer en permanence tel un Data Center.





