import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        pass


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return ("{} has received {} points of damage".format(self.name, damage))
        else:
            return ("{} has died in act of combat".format(self.name))

    def battleCry(self):
        return ("Odin Owns You All!")


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)
        pass

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return ("A Saxon has received {} points of damage".format(damage))
        else:
            return ("A Saxon has died in combat")


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, c):
        self.vikingArmy.append(c)

    def addSaxon(self, s):
        self.saxonArmy.append(s)

    def vikingAttack(self):
        self.c.receiveDamage = self.c.strength

    def saxonAttack(self):
        self.c.receiveDamage = self.c.strength
