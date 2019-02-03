
import random


# Soldier

class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage


# Viking

class Viking (Soldier):

    def __init__(self, name, health, strength):

        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)

        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, self.damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

    pass


# Saxon

class Saxon (Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)

        if self.health > 0:
            return "A Saxon has received {} points of damage".format(self.damage)
        else:
            return "A Saxon has died in combat"

    pass


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
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        ataque = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return ataque

    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        ataque = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return ataque

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
