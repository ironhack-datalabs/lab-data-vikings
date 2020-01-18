from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
import random

# Generar ejércitos (pedir por teclado cantidad o hacer random)
# generar salud y fuerza aleatorias entre un minimo y un maximo
# preguntar quién inicia el conflicto
# Hacer métodos de representación para las clases (poder hacer print de un soldado y del estado de los ejercitos)
# versión "coward mode" de VikingAttack y SaxonAttack en los que, en lugar de elegirlos de forma aleatoria, sea el más fuerte el que ataque al contrario de menos salud



nombres_vikingos = ['Aren','Axe','Bjorn','Daven','Egil','Einar','Erik','Esben','Gerd','Gisli','Haakon','Helge','Hans',\
    'Harald','Ivar','Jensen','Jorgen','Lars','Niels','Olav','Olson','Olson','Sveinn','Thor','Viggo']


def askArmySize():
    while True:
        try:
            tam = int(input("How many soldiers will fight for each army? (max 10) -> "))
            if tam > 0:
                return tam
            else:
                raise Exception
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
    if (random.randint(0,9) >= 5):
        #g.removeViking()
        g.vikingArmy[0].becomeBerserker()
        #g.addViking(Viking('^^BERSERKER^^',250,80))


def battle(g,turno):
    while len(g.saxonArmy) != 0 and len(g.vikingArmy) != 0:
        if(turno=="s"):
            g.saxonAttackCow()
            turno="v"
        else:
            g.vikingAttackCow()
            turno="s"
        print(g)
        #print(g.showStatus())
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass

guerra = War()

n = askArmySize()
generateArmies(guerra,min(10,n))
# como maximo seran 10 por ejercito
print(guerra)
emp = askWhichOneStarts()
if emp == "s":
    print("Saxons will start the war")
else:
    print("Vikings will start the war")

battle(guerra,emp)
print(guerra.showStatus())
guerra.heroesOfWar()



