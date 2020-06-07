from vikingsClases import Soldier
from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
import random

# BATALLA
g = War()

# Meter nombres de vikingos
randomName = ["Arenn", "Axell", "Bjorn", "Daven", "Egill", "Einar", "Esben", "Gaerd", "Hakon", "Helge", "Haens", "Haral"]


# Se llama a los mejores soldados de cada ejercito para luchar 
def ns():
    while True:
        try:
            q = int(input("How many soldiers are going to fight? (max10) -> "))
            if q > 0:
                return q
            else:
                raise Exception
        except:
            print("wrong choice, try again")


# Conseguir que cada soldado tenga una HP y un AT random
def armies(g, bs):
    for e in range(0,min(10,bs)):
        g.addViking(Viking(random.choice(randomName), random.randint(50,100), random.randint(35,45)))
        g.addSaxon(Saxon(random.randint(40,80), random.randint(20,30)))

# Inicio de batalla random
b = ["v", "s"]

def battleTurn(b):
    attackTurn = random.choice(b)
    return attackTurn

# Ataque por turnos
def battleIsBegins(g,t):
    while g.vikingArmy != 0 and g.saxonArmy != 0:
        print("\n")
        if t == "v":
            print("VIKINGS ATTACK")
            g.vikingAttack()
            g.showStatus()
            t = "s"
        elif t == "s":
            print("SAXON ATTACK")
            g.saxonAttack()
            g.showStatus()
            t = "v"
    print(g)
    print(g.showStatus)
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass

ns()
armies(g, ns())
print(g)
battleTurn(b)
battleIsBegins(g,battleTurn)
print("------ THE END ------")