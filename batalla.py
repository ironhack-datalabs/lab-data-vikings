import unittest
from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
from inspect import signature
import random

names = ["Julio", "Alex", "Cristina", "Ovi", "Bego"]
health = [100, 100, 100, 100, 100]
strenght = [5, 7, 8, 6, 10]
Vikinga = Viking(random.choice(names), random.choice(health), random.choice(strenght))
Saxona = Saxon(random.choice(health), random.choice(strenght))

v = int(input("Cuantos Vikingos quieres "))
s = int(input("Cuantos Saxones quieres "))
guerra = War()
for a in range(v + 1):
    guerra.addViking(Vikinga)

for x in range(s + 1):
    guerra.addSaxon(Saxona)


while True:
    guerra.vikingAttack()
    if guerra.vikingArmy == 0 or guerra.saxonArmy == 0:
        print(guerra.showStatus())
        break
    guerra.saxonAttack()
    if guerra.vikingArmy == 0 or guerra.saxonArmy == 0:
        print(guerra.showStatus())
        break

