
# Soldier
import math
import random


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name, damage)

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"


# War

def sample(lst):
    rndIndex = math.floor(random.random() * len(lst))
    return lst[rndIndex], rndIndex


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Viking):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        saxon, saxonIndex = sample(self.saxonArmy)
        viking, _ = sample(self.vikingArmy)
        solved = saxon.receiveDamage(viking.strength)

    if saxon.health <= 0:
        del self.saxonArmy[saxonIndex]
    return solved

    def saxonAttack(self):
        saxon, _ = sample(self.saxonArmy)
        viking, vikingIndex = sample(self.vikingArmy)
        solved = viking.receiveDamage(saxon.strength)

    if saxon.health <= 0:
        del self.saxonArmy[saxonIndex]
    return solved

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for thei lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
