# # # # # # # # #      vikingsClases      # # # # # # # # # # # # # #
# Contains classes and methods for an epic battle between Vikings   #
# and their arch-nemeses, the Saxons.                               #
# Create your Viking and Saxon men, summon them to war and watch    #
# them murder each other to extinction. May the best nation win!    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Importing Libraries

import random


# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return '{} has died in act of combat'.format(self.name)
        else:
            return '{} has received {} points of damage'.format(self.name, damage)

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return 'A Saxon has died in combat'
        else:
            return 'A Saxon has received {} points of damage'.format(damage)


# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        attackingViking = (random.choice(self.vikingArmy))
        defendingSaxon = random.choice(self.saxonArmy)
        attack = defendingSaxon.receiveDamage(attackingViking.strength)
        if attack == 'A Saxon has died in combat':
            self.saxonArmy.remove(defendingSaxon)
        return attack

    def saxonAttack(self):
        defendingViking = (random.choice(self.vikingArmy))
        attackingSaxon = random.choice(self.saxonArmy)
        attack = defendingViking.receiveDamage(attackingSaxon.strength)
        if attack == '{} has died in act of combat'.format(defendingViking.name):
            self.vikingArmy.remove(defendingViking)
        return attack

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        if len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return 'Vikings and Saxons are still in the thick of battle.'
