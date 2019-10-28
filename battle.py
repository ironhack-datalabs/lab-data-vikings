from vikingClassesimproved import War
from vikingClassesimproved import Viking
from vikingClassesimproved import Saxon
import random

war = War()

war.addViking(Viking('Pepeluis', 45, 80))
war.addViking(Viking('Victorina', 30, 95))
war.addViking(Viking('Blanca', 3, 487))
war.addViking(Viking('Alvaro Cotelo', 100, 14))

war.addSaxon(Saxon('Ignacio', 120, 50))
war.addSaxon(Saxon('Curra', 20, 89))
war.addSaxon(Saxon('Caraballo', 97, 80))

round = 1
while war.showStatus() == 'Vikings and Saxons are still in the thick of battle.':
    print('\nROUND: ', round)
    if (random.choice([0, 1])):
        print(war.vikingAttack())
    else:
        print(war.saxonAttack())
    round += 1

war.showSurvivors()