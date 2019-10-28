
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage
        

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength): 
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)  
        else:
            return "{} has died in act of combat".format(self.name)
        
    def battleCry(self):
        return "Odin Owns You All!"
        
# Saxon


class Saxon(Soldier):
# como Soldier ya tiene health como 1er agrumento y strength como 2º, simplemente 
# importando Soldier ya tengo lo que me piden
# tampoco hace falta reimplementar attack
# 
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        vikingRandom=random.choice(self.vikingArmy)
        saxonRandom=random.choice(self.saxonArmy)
        fightViking=saxonRandom.receiveDamage(vikingRandom.attack())
        if saxonRandom.health<=0:
            self.saxonArmy.remove(saxonRandom)
            
        return fightViking

    def saxonAttack(self):
        saxonRandom=random.choice(self.saxonArmy)
        vikingRandom=random.choice(self.vikingArmy)
        fightSaxon=vikingRandom.receiveDamage(saxonRandom.attack())
        if vikingRandom.health<=0:
            self.vikingArmy.remove(vikingRandom)
            
        return fightSaxon

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)==1 and len(self.vikingArmy)==1:
            return "Vikings and Saxons are still in the thick of battle."

    
