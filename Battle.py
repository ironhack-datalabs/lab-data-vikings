from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
import random

# Ejercito Vikingo de freaks data-analíticos:
Vikingo1 = Viking("Alex", random.randint(1,201), random.randint(1,101))
Vikingo2 = Viking("Julio", random.randint(1,201), random.randint(1,101))
Vikingo3 = Viking("Ovi", random.randint(1,201), random.randint(1,101))
Vikingo4 = Viking("Cris", 10, random.randint(1,101)) # Muy mala salud
Vikingos = [Vikingo1, Vikingo2, Vikingo3, Vikingo4]

# Ejercito Sajón:
n = 6
Sajones = []
for i in range(n):
    Sajones.append(Saxon(random.randint(1,201),random.randint(1,101)))

# Guerra:
Guerra = War()

for e in Vikingos:
    Guerra.addViking(e)

for e in Sajones:
    Guerra.addSaxon(e)

status = "Vikings and Saxons are still in the thick of battle."
while status == "Vikings and Saxons are still in the thick of battle.":
    print("\nVikings attack:")
    print(Guerra.vikingAttack())
    status = Guerra.showStatus()
    print(status)
    if status == "Vikings and Saxons are still in the thick of battle.":
        print("\nSaxons attack:")
        print(Guerra.saxonAttack())
        status = Guerra.showStatus()
        print(status)
    else:
        break
