import random

class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        attack = self.strength
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        
            
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return("{} has received {} points of damage".format(self.name, damage))
        else:
            return("{} has died in act of combat".format(self.name))

    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        viking1=random.choice(self.vikingArmy)
        saxon1=random.choice(self.saxonArmy)
        #random_viking = choice(self.vikingArmy)
        #random_saxon = choice(self.saxonArmy)
        #result = random_saxon.receiveDamage(random.viking.attack())
        #return result
        scoreWar=saxon1.receiveDamage(viking1.strength)
        if saxon1.health <=0:
            self.saxonArmy.remove(saxon1)
        return scoreWar 


    def saxonAttack(self):

        viking2=random.choice(self.vikingArmy)
        saxon2=random.choice(self.saxonArmy)
        scoreWar1=viking2.receiveDamage(saxon2.strength)
        if viking2.health <=0:
            self.vikingArmy.remove(viking2)
        return scoreWar1


    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else len(self.saxonArmy) != 0 and len(self.vikingArmy) != 0:
            return "Vikings and Saxons are still in the thick of battle."





