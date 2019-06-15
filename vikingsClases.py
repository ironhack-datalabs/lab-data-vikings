# Imports

from random import randint

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        attack = self.strength
        return self.strength

    def receiveDamage(self, damage):
        if damage > 0:
            self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        if damage > 0:
            self.health = self.health - damage
            if self.health > 0:
                return "{} has received {} points of damage".format(self.name, damage)
            if self.health < 1:
                return "{} has died in act of combat".format(self.name)
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)

    def receiveDamage(self, damage):
        if damage > 0:
            self.health = self.health - damage
            if self.health > 0:
                return "A Saxon has received {} points of damage".format(damage)
            if self.health < 1:
                return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def getRandomWarrior(self, Army):
        index = randint(0, len(Army) - 1)
        return Army[index]

    def vikingAttack(self):
        defender = self.getRandomWarrior(self.saxonArmy)
        attacker = self.getRandomWarrior(self.vikingArmy)
        result = defender.receiveDamage(attacker.strength)
        if defender.health < 1:
            self.saxonArmy.remove(defender)
        return result

    def saxonAttack(self):
        defender = self.getRandomWarrior(self.vikingArmy)
        attacker = self.getRandomWarrior(self.saxonArmy)
        result = defender.receiveDamage(attacker.strength)
        if defender.health < 1:
            self.vikingArmy.remove(defender)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."  