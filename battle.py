import random
import vikingsClases as vc


#create viking 
def createViking(num):
    return vc.Viking("Harold_"+str(num),random.randint(250,300),random.randint(30,50))

#create saxon
def createSajon():
    return vc.Saxon(random.randint(200,250),random.randint(15,20))

#Attack
def attack(war):
    if random.choice( ['viking', 'saxon'] )=='viking':
        print("=========Ataque vikingo=======")
        return war.vikingAttack()
    else: 
        print("=========Ataque sajon=======")
        return war.saxonAttack()


# Viking Army
print("hola")
war=vc.War()

for i in range(random.randint(10,15)):
    war.addViking(createViking(i))

# Saxon Army
for i in range(random.randint(20,25)):
    war.addSaxon(createSajon())

while len(war.saxonArmy)!=0 and len(war.vikingArmy)!=0:
    print(attack(war))
    print(war.showStatus())
    print(str(len(war.vikingArmy))+" Vikings - "+str(len(war.saxonArmy))+" Saxons")






