from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
import random


nombres_vikingos = ['Aren','Axe','Bjorn','Daven','Egil','Einar','Erik','Esben','Gerd','Gisli','Haakon','Helge','Hans',\
    'Harald','Ivar','Jensen','Jorgen','Lars','Niels','Olav','Olson','Olson','Sveinn','Thor','Viggo']


def askArmySize():
    while True:
        try:
            tam = int(input("How many soldiers will fight? -> "))
            return tam
        except:
            print('invalid value. try again')

def askWhichOneStarts():
    while True:
        try:
            ini = input("Who will start the war? [v/s] -> ")
            if ini not in ("v","s"):
                raise NameError("Not in [v/s]")
            else:
                return ini
        except:
            print('invalid value. try again')

def generateArmies(g,size):
    for i in range(0,size):
        g.addViking(Viking(random.choice(nombres_vikingos),random.randint(1,51)+50,random.randint(1,11)+25))
        g.addSaxon(Saxon(random.randint(1,51)+50,random.randint(1,11)+25))


def battle(g,turno):
    while len(g.saxonArmy) != 0 and len(g.vikingArmy) != 0:
        if(turno=="s"):
            g.saxonAttack()
            turno="v"
        else:
            g.vikingAttack()
            turno="s"
        print(g)
        print(g.showStatus())

guerra = War()

n = askArmySize()
generateArmies(guerra,n)
print("Armies are:",guerra)
emp = askWhichOneStarts()
if emp == "s":
    print("Saxons will start the war")
else:
    print("Vikings will start the war")

battle(guerra,emp)


#print(guerra)


