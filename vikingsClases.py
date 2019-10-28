import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        vikingRandom=random.choice(self.vikingArmy)
        saxonRandom=random.choice(self.saxonArmy)
        s=saxonRandom.receiveDamage(vikingRandom.strength)
        if saxonRandom.health <=0:
            self.saxonArmy.remove(saxonRandom)
        return s
    def saxonAttack(self):
        vikingRandom=random.choice(self.vikingArmy)
        saxonRandom=random.choice(self.saxonArmy)
        r = vikingRandom.receiveDamage(saxonRandom.strength)
        if vikingRandom.health <=0:
            self.vikingArmy.remove(vikingRandom)
        return r
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy)>=1 and len(self.saxonArmy)>=1:
            return "Vikings and Saxons are still in the thick of battle."