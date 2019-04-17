
import random


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage

class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name= name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

class Saxon(Soldier):

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

class War:
    def __init__ (self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        Viking1 = random.choice(self.vikingArmy)
        Saxon1 = random.choice(self.saxonArmy)
        result = Saxon1.receiveDamage(Viking1.strength)
        if Saxon1.health <= 0:
            self.saxonArmy.remove(Saxon1)
        return result 

    def saxonAttack(self):
        Viking2 = random.choice(self.vikingArmy)
        Saxon2 = random.choice(self.saxonArmy)
        result = Viking2.receiveDamage(Saxon2.strength)
        if Viking2.health <= 0:
            self.vikingArmy.remove(Viking2)
        return result 

    def showStatus(self):
        if len(self.saxonArmy)==0 :
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy)!=0 and len(self.saxonArmy)!=0:
            return "Vikings and Saxons are still in the thick of battle."



