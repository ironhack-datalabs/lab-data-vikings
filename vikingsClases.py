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
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)

        elif self.health <= 0:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        elif self.health <= 0:
            return "A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.Viking = self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.Saxon = self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        Saxon = random.choice(self.saxonArmy)
        Saxon.health -= Saxon.receiveDamage(Viking.damage)
        if Saxon.health == 0:
            self.saxonArmy.remove(Saxon)
        return Saxon.receiveDamage(Viking.strength)

    def saxonAttack(self):
        Viking = random.choice(self.vikingArmy)
        Viking.health -= Viking.receiveDamage(Saxon.damage)
        if Viking.health == 0:
            self.vikingArmy.remove(Viking)
        return Viking.receiveDamage(Saxon.strength)

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
