import random
from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon


vikingos = ["Ragnar", "Lagertha", "Ivar", "Björn", "Ubbe", "Hvitserk", "Alaug", "Sigurd", "Floki", "Rollo"]

guerra = War()

def createVikingArmy():
    vikings = [Viking(random.sample(vikingos, 1), int(random.random()*100), int(random.random()*100)) for e in range(10)]
    [guerra.addViking(e) for e in vikings]
def createSaxonArmy():
    saxons = [Saxon(int(random.random()*100), int(random.random()*100)) for e in range(10)]
    [guerra.addSaxon(e) for e in saxons]


def batalla():
    createVikingArmy()
    createSaxonArmy()
    while True:
        if int((random.random()*10 + 1))/2 == 0:
            print(guerra.vikingAttack())
            if len(guerra.saxonArmy ) > 0:
                print(guerra.saxonAttack())
        else:
            print(guerra.saxonAttack())
            if len(guerra.vikingArmy) > 0:
                print(guerra.vikingAttack())
        print(guerra.showStatus())
        if len(guerra.vikingArmy) == 0 or len(guerra.saxonArmy) == 0:
            break

batalla()