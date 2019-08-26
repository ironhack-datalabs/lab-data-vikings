
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength 
    def attack(self):
        return self.strength 
    def receiveDamage(self, damage):
        self.health= self.health-damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health == 0:
            return self.name + " has died in act of combat"
        else:
            return self.name + " has received " + str(damage) +  " points of damage"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength 
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health == 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received " + str(damage)+  " points of damage"



class War:
    def __init__(self):
        vikingArmy = []
        saxonArmy = []
    def addViking(self, Viking):
        vikingArmy += 1
    def addSaxon(self, Saxon):
        saxonArmy += 1

