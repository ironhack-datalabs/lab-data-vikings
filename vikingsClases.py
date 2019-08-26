
# Soldier


import random


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - (damage)


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - (damage)
        if self.health <= 0:
            return ("{} has died in act of combat" .format(self.name))
        else:
            return ("{} has received {} points of damage" .format(self.name, damage))

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - (damage)
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return ("A Saxon has received {} points of damage".format(damage))


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        a_saj = random.choice(self.saxonArmy)
        a_vik = random.choice(self.vikingArmy)
        res = a_saj.receiveDamage(a_vik.strength)
        if a_saj.health <= 0:
            self.saxonArmy.remove(a_saj)
        return res

    def saxonAttack(self):
        a_saj = random.choice(self.saxonArmy)
        a_vik = random.choice(self.vikingArmy)
        res = a_vik.receiveDamage(a_saj.strength)
        if a_vik.health <= 0:
            self.vikingArmy.remove(a_vik)
        return res

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
