import math
import random from math

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
        Soldier.__init__(self, health, strength)
        self.name = name
        """self.health = health
        self.strength = strength"""
    # no hace falta     def attack(self):
    #                      return self.strength
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health == 0:
            return   "{} has died in act of combat".format(self.name)
        else:
            return "{} has received {} points of damage".format(self.name,damage)
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    """def __init__(self, health, strength):
        self.health = health
        self.strength = strength                            es igual que el de Soldier"""
    """def attack(self):
        return self.strength """
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health == 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received {} points of damage".format(damage)

from random import choice

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        self.vikingArmy.append(viking) 
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon) 
    def vikingAttack (self):
        random_viking = choice(self.vikingArmy)
        random_saxon = choice(self.saxonArmy)
        result = random_saxon.receiveDamage(random_viking.attack())
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random.saxon)
        return result
    def saxonAttack (self):
        random_viking = choice(self.vikingArmy)
        random_saxon = choice(self.saxonArmy)
        result = random_viking.receiveDamage(random_saxon.attack())
        if random_viking.health <= 0:
            self.vikingArmy.remove(random.viking)
        return result
    def showStatus (self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len (self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


