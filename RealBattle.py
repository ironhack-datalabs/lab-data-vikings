# Soldier

class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health-damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        bcry=["We are going to die!!","You will die tonight!!"]    
        print(bcry[random.choice([0,1])])


# Saxon

class Saxon(Viking):
    pass


# War

import random

class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.receiveDamage(viking.attack())
        self.saxonArmy = [s for s in self.saxonArmy if s.health>0]
        return (damage + " from the attack of " +viking.name)

    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = viking.receiveDamage(saxon.attack())
        self.vikingArmy = [v for v in self.vikingArmy if v.health>0]
        return (damage + " from the attack of " +saxon.name)


    
    def showStatus(self):
        if len(self.saxonArmy)>0 and len(self.vikingArmy)>0:
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."

    def showSurvivors(self):
        if len(self.saxonArmy):
            print("The saxon survivors are:",*[s.name for s in self.saxonArmy])
            random.choice(self.saxonArmy).battleCry()
        if len(self.vikingArmy):
            print("The viking survivors are:",*[v.name for v in self.vikingArmy])

    

war = War()
war.addViking(Viking("Mercedes", 400, 100))
war.addViking(Viking("Antonio", 400, 50))
war.addViking(Viking("Isa", 500, 75))
war.addSaxon(Saxon("Pepe", 400, 40))
war.addSaxon(Saxon("Ignacio",350, 40))
war.addSaxon(Saxon("Fran",450, 35))

war.showStatus()=="Vikings and Saxons are still in the thick of battle."
n=0
while war.showStatus()=="Vikings and Saxons are still in the thick of battle.":
    n+=1
    print("\nROUND", n)
    if random.choice([0,1]):
        print("\n",war.saxonAttack())
    else:
        print("\n",war.vikingAttack())
    war.showSurvivors()
    print(war.showStatus(), "\n")


