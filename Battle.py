from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon

# Ejercito Vikingo de freaks data-analíticos:
Vikingo1 = Viking("Alex", 150, 200)
Vikingo2 = Viking("Julio", 100, 300)
Vikingo3 = Viking("Ovi", 50, 200)
Vikingo4 = Viking("Cris", 10, 100) # Muy mala salud
Vikingos = [Vikingo1, Vikingo2, Vikingo3, Vikingo4]

# Ejercito Sajón:
Sajon1 = Saxon(500,500)
Sajon2 = Saxon(50,50)
Sajon3 = Saxon(150,150)
Sajon4 = Saxon(100,100)
Sajones = [Sajon1, Sajon2, Sajon3, Sajon4]

Guerra = War()

# Ejercito Vikingo:
for e in Vikingos:
    Guerra.addViking(e)

# Ejercito Sajón:
for e in Sajones:
    Guerra.addSaxon(e)

status = "Vikings and Saxons are still in the thick of battle."
while status == "Vikings and Saxons are still in the thick of battle.":
    print("Viking Attack!:")
    print(Guerra.vikingAttack())
    status = Guerra.showStatus()
    # print(status)
    if status == "Vikings and Saxons are still in the thick of battle.":
        print("Saxon Attack!:")
        print(Guerra.saxonAttack())
        status = Guerra.showStatus()
        print(status)
    else:
        break
