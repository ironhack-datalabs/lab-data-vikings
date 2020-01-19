import random
from vikingsClases import War
from vikingsClases import Viking
from vikingsClases import Saxon
#create your army  vikingos & saxons
def CreateArmy():
    while True:
        try:
            length_vikings = int(input("Introduce length of vikings army:"))
            length_saxon = int(input("Introduce length of saxon army:"))
            return length_vikings, length_saxon
        except ValueError:
            print("That's not a number")
len_vikings, len_saxon = CreateArmy()
war = War()
def CreateArmyVikings():
    y = [Viking(random.sample(['Harald','Einar','Ragnar','Astrid','Erika'],1)[0],random.randint(50,100),random.randint(50,100)) for i in range(len_vikings)]
    [war.addViking(i) for i in y]

def CreateArmySaxons():
    x = [Saxon(random.randint(50,100),random.randint(50,100)) for i in range(len_saxon)]
    [war.addSaxon(e) for e in x]

#Battle
def Battle():
    CreateArmySaxons()
    CreateArmyVikings()
    while len(war.vikingArmy)!= 0 and len(war.saxonArmy)!=0 :
        if random.sample(["S","V"],1)[0] == "S":
            print(war.saxonAttack())
            if len(war.vikingArmy)!= 0 :
                print(war.vikingAttack())
        else:
            print(war.vikingAttack())
            if len(war.saxonArmy)!= 0 :
                print(war.saxonAttack())
    print(war.showStatus())

Battle()