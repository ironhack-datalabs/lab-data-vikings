from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
import random

Guerra = War()

vikings_name = ["Aren", "Axe", "Bjorn", "Daven", "Egil", "Einar", "Esben",
 "Gerd", "Gisli", "Haakon", "Helge", "Hans", "Harald", "Ivar", 
 "Jensen", "Jorgen", "Lars", "Niels", "Odín", "Olaf", "Olson", "Sigurd", "Sven", "Thor", "Viggo"]
vikings_health = [int(random.random()*200+100) for e in range(len(vikings_name))]
vikings_strength = [int(random.random()*50+25) for e in range(len(vikings_name))]

saxons_num = 85
saxons_health = [int(random.random()*150+50) for e in range(saxons_num)]
saxons_strength = [int(random.random()*20+10) for e in range(saxons_num)]

for i, e in enumerate (vikings_name):
    Guerra.addViking (Viking (e, vikings_health[i], vikings_strength[i]))

for i in range(saxons_num):
    Guerra.addSaxon (Saxon(saxons_health[i], saxons_strength[i]))
    
while Guerra.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print (Guerra.vikingAttack())
    if Guerra.showStatus() != "Vikings and Saxons are still in the thick of battle.":
        break
    else:
        print (Guerra.saxonAttack())

    if Guerra.showStatus() != "Vikings and Saxons are still in the thick of battle.":
        break
print (Guerra.showStatus())