
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage

# Viking


class Viking:
    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"    

# War

import random
class War:
        def __init__(self):
            self.vikingArmy=[]
            self.saxonArmy=[]
        
        def addViking(self,viking):
            self.vikingArmy.append(viking)

        def addSaxon(self,saxon):
            self.saxonArmy.append(saxon)
        
        def vikingAttack(self):
            viking=random.choice(self.vikingArmy)
            saxon=random.choice(self.saxonArmy)
            res=saxon.receiveDamage(viking.strength)
            if res == "A Saxon has died in combat":
                self.saxonArmy.remove(saxon)
            return res
        
        def saxonAttack(self):
            viking=random.choice(self.vikingArmy)
            saxon=random.choice(self.saxonArmy)
            res=viking.receiveDamage(saxon.strength)
            if res == viking.name + " has died in act of combat":
                self.vikingArmy.remove(viking)
            return res
        
        def showStatus(self):
            if len(self.saxonArmy) == 0:
                return "Vikings have won the war of the century!"
            elif len(self.vikingArmy) == 0:
                return "Saxons have fought for their lives and survive another day..."
            elif len(self.saxonArmy)==1 and len(self.vikingArmy)==1:
                return "Vikings and Saxons are still in the thick of battle."
