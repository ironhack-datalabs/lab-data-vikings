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


status = "Vikings and Saxons are still in the thick of battle."
while status == "Vikings and Saxons are still in the thick of battle.":
    print("Hala Real Madrid al Ataque!!!")
    print(guerra.vikingAttack())
    status = guerra.showStatus()
    print(status)
    if status == "Vikings and Saxons are still in the thick of battle.":
        print("Lomo de Sajonia al poder!!!")
        print(guerra.saxonAttack())
        status = guerra.showStatus()
        print(status)
    else:
        break

