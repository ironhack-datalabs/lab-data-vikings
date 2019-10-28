
# Soldier


import random


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
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0:
            return (str(self.name)+' has received '+str(damage)+' points of damage')
        else:
            return (str(self.name)+' has died in act of combat')

    def battleCry(self):
        return 'Odin Owns You All!'
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0:
            return ('A Saxon has received '+str(damage)+' points of damage')
        else:
            return 'A Saxon has died in combat'


# War


class War(Saxon, Viking, Soldier):
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        random.choice(self.vikingArmy)
        super().receiveDamage(super(Soldier).attack())

    def saxonAttack(self):
        random.choice(self.saxonArmy)
        super().receiveDamage(super(Soldier).attack())

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
