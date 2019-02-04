
# Soldier


class Soldier:
    pass
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    pass
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def attack(self):
        Soldier.attack(self)
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    pass
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def attack(self):
        Soldier.attack(self)
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War

import random

class War(Soldier):
    pass
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)
        result_attack = saxon_soldier.receiveDamage(viking_soldier.strength)
        if saxon_soldier.health <= 0:
            self.saxonArmy.remove(saxon_soldier)
        return result_attack

    def saxonAttack(self):
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier = random.choice(self.saxonArmy)
        result_attack = viking_soldier.receiveDamage(saxon_soldier.strength)
        if viking_soldier.health <= 0:
            self.vikingArmy.remove(viking_soldier)
        return result_attack

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."