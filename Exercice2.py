#! / usr / bin / env python3 
import ev3dev.ev3 as ev3
from ev3dev.ev3  import  *
from time import sleep
import sys

def exitRouge():
   if cl.value(0) > 100:
      if cl.value(1) + cl.value(2) < 50:
         m1.run_forever(speed_sp = 0)
         m2.run_forever(speed_sp = 0)
         beeps(3)
         sleep(1)
         sys.exit(0)

m1 = LargeMotor('outB') 
assert m1.connected, "Connecter un large motor sur outB" #vérification de la variable m1
m2 = LargeMotor('outC')
assert m2.connected, "Connecter un large motor sur outC" #vérification de la variable m2

ir = InfraredSensor() #définir le capteur comme capteur infrarouge
assert ir.connected, "Connecter le senseur infrarouge a un des ports" #vérifier que le capteur est connecté
ir.mode = 'IR-PROX' #mettre le capteur ir en mode prowimité

distance = ir.value() #ir détecte la distance entre le robot et un éventuel obstacle

m1.run_forever(speed_sp = 0)
m2.run_forever(speed_sp = 0)

while ir.value() > 30:
    exitRouge()
	distance = ir.value()

    while ir.value() > 70:
       exitRouge()

       distance = ir.value()
       m1.run_forever(speed_sp = 300 - 2000/(cur_distance + 3))
       m2.run_forever(speed_sp = 300 - 2000/(cur_distance + 3))

    m1.run_forever(speed_sp = 0)
    m2.run_forever(speed_sp = 0)
    m1.run_forever(speed_sp = 400)
    m2.run_forever(speed_sp = 400)
    sleep(1.5)

    exitRouge() 

    for num in range(1,5):
        m2.run_timed(speed_sp=400)
        sleep(0.6)
        exitRouge()

        if ir.value() < 70:
            break

m1.run_forever(speed_sp = 0)
m2.run_forever(speed_sp = 0)
