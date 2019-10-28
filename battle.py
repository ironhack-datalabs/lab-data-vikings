from vikingsClases import Soldier
from vikingsClases import Viking
from vikingsClases import Saxon
from vikingsClases import War
import random
print('Cuantos soldados tendra cada ejercito?')
numsoldiers = int(input())
Guerra = War()
names = ['Juan', 'Antonio', 'Pepa', 'Ragnar', 'Lagertha']
health = [100, 200, 150, 250, 300]
strength = [5, 10, 15, 20, 25, 30]
Vikingo = Viking(random.choice(names), random.choice(
    health), random.choice(strength))
Sajon = Saxon(random.choice(health), random.choice(strength))
for e in range(numsoldiers):
    Guerra.addSaxon(Sajon)
    Guerra.addViking(Vikingo)
while True:
    Guerra.vikingAttack()
    if len(Guerra.saxonArmy) == 0 or len(Guerra.vikingArmy) == 0:
        print(Guerra.showStatus())
        break
    Guerra.saxonAttack()
    if len(Guerra.saxonArmy) == 0 or len(Guerra.vikingArmy) == 0:
        print(Guerra.showStatus())
        break
