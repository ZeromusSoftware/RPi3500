#!/usr/bin/python
# -*- coding:Utf-8 -*-

import RPi.GPIO as GPIO
import time
import os # Module pour importer les sorties de commande système
GPIO.setmode(GPIO.BOARD) # On utilise la numérotation des gpio physique

TempMax = "45" # Temp max avant déclenchement led + ventilo (max 80 degrès...)
GPIO.setup(18, GPIO.OUT) # On confgure la pin 18 (GPIO24) en sortie.

Ventilo = 18 #pin18 (GPIO24) ou ventilo branché

while 1: #1 plus rapide que true
 cmdtemp = '/opt/vc/bin/vcgencmd measure_temp'  # On définit la commande a appeller pour rapatrier la temperature
 result = os.popen(cmdtemp).readline().strip() # On appelle la cmdtemp avec le module os
 temp = result.split('=')[1].split("'")[0] # Le résultat étant temp=xx.x'C on y supprime pr garder que le chiffre
 if temp < TempMax:
     print("Température inférieure")
     GPIO.output(Ventilo, False)
 else:
     print("Température supérieure, lancement ventilo")
     GPIO.output(Ventilo, True)
 time.sleep(5) # Rafraichissement ttes les 5 secondes
