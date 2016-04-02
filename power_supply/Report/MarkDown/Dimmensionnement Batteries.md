#Dimmensionnement Batteries
---
###Préambule

Pour parer à l'éventualité de la coupure de courant EDF, il nous faut une seconde source d'alimentation afin d'assurer le fonctionnement en continu de notre Data Center. Nous planchons, comme cité [précedemment](https://github.com/ZeromusSoftware/RPi3500/blob/master/power_supply/Report/MarkDown/In%20Case%20Of%20Emergency.md), sur une autonomie de 3h soit 180 minutes.

###Choix des Batteries

Nous comptons utiliser des batteries Li-Ion ou Li-Po, très couramment utilisées dans les appareils électronique portatif. Néanmoins ces batteries sont exigeantes, il faudra les surveiller constamment en particulier lors des phases de recharge et de décharge.


Puisque nous utilisons deux circuits de deux tensions différentes, nous utiliserons deux "piles".

* l'une délivrant une tension de 5V
* l'autre délivrant une tension de 12V

###Sous Tension de 5V

Sous cette tension, nous alimenterons les 4 Raspberry Pi 2 et le Raspberry Pi B+.
Au cours de nos tests, la consommation maximale relevé à été de 0,5 Ampères.  

En prenant une marge de sécurité alors de 0,1 Ampère :

* 0,6 A x 5 RPi = **3,5 A**

Or nous souhaitons 3h d'autonomie :

 * Q = I x T 
 * 3,5 A x 3h = **10,5 A.h**

 Il nous faudra alors une batterie avec une capacité de 10,5 A.h et capable de délivrer un courant superieur à 3,5 A sous une tension continue de 5V.


###Sous Tension de 12V

Sous cette tension, nous alimenterons les 4 ventilateurs et le switch ethernet.

Selon les caractéristiques constructeurs, sous cette tension la batterie devra fournir un courant d'environ 2,5 Ampères en s'imposant une petite marge de sécurité de 0,25 Ampères.

Or nous souhaitons 3h d'autonomie aussi :

* Q = I x T
* 2,5 x 3 = **7,5 A.h**

	Il nous faudra alors une capacité de 7,5 A.h sous cette batterie délivrant une tension continue de 12V qui doit être capable de délivrer un courant de 2,5 A.



