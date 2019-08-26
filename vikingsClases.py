
# Soldier
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
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return ("{} has received {} points of damage".format(self.name, damage))
        else:
            return ("{} has died in act of combat".format(self.name))

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return ("A Saxon has received {} points of damage".format(damage))
        else:
            return ("A Saxon has died in combat")


# War


class War:

    def __innit__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):
        sax1 = random.choice(self.saxonArmy)
        vik1 = random.choice(self.vikingArmy)
        receive_damage = sax1.receiveDamage(vik1.strength)
        if sax1.health <= 0:
            self.saxonArmy.remove(sax1)
        return receive_damage

    def saxonAttack(self):
        sax1 = random.choice(self.saxonArmy)
        vik1 = random.choice(self.vikingArmy)
        receive_damage = vik1.receiveDamage(sax1.strength)
        if vik1.health <= 0:
            self.vikingArmy.remove(vik1)
        return receive_damage

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"

        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
