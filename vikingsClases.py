
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health=self.health-damage


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name=name
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health-=damage
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
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        vikingo=random.choice(self.vikingArmy)
        sa=random.choice(self.saxonArmy)
        strength_of_viking=sa.receiveDamage(vikingo.attack())
        self.saxonArmy=[s for s in self.saxonArmy if s.health>0]
        return strength_of_viking
    def saxonAttack(self):
        saxo=random.choice(self.saxonArmy)
        vik=random.choice(self.vikingArmy)
        strength_of_saxon=vik.receiveDamage(saxo.attack())
        self.vikingArmy=[v for v in self.vikingArmy if v.health>0] 
        return strength_of_saxon
    def showStatus(self):
        if (len(self.saxonArmy))==0 :
            return "Vikings have won the war of the century!"
        elif (len(self.vikingArmy))==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

