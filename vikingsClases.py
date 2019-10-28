
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
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
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

    def vikingAttack(self):
        rd_viking = random.choice(self.vikingArmy)
        rd_saxon = random.choice(self.saxonArmy)
        viking_attack = rd_saxon.receiveDamage(rd_viking.attack())
        if rd_saxon.health <= 0:
            self.saxonArmy.remove(rd_saxon)
        return viking_attack

    def saxonAttack(self):
        rd_saxon = random.choice(self.saxonArmy)
        rd_viking = random.choice(self.vikingArmy)
        saxon_attack = rd_viking.receiveDamage(rd_saxon.attack())
        if rd_viking.health <= 0:
            self.vikingArmy.remove(rd_viking)
        return saxon_attack

    def showStatus(self):
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif len(self.saxonArmy) == 1 & len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."
