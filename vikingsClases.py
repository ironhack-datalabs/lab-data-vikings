
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
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health <= 0:
            status = "{} has died in act of combat".format(self.name)
        else:
            status = "{} has received {} points of damage".format(
                self.name, str(damage))
        return status

    def battleCry(self):
        cry = "Odin Owns You All!"
        return cry

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health <= 0:
            status = "A Saxon has died in combat"
        else:
            status = "A Saxon has received {} points of damage".format(
                str(damage))
        return status

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
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        damage = Viking.attack()
        result = Saxon.receiveDamage(damage)
        if Saxon.health <= 0:
            self.saxonArmy.pop()
        return result

    def saxonAttack(self):
        Viking = random.choice(self.vikingArmy)
        Saxon = random.choice(self.saxonArmy)
        damage = Saxon.attack()
        result = Viking.receiveDamage(damage)
        if Viking.health <= 0:
            self.vikingArmy.pop()
        return result

    def showStatus(self):
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            result = "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy) <= 0:
            result = "Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0:
            result = "Saxons have fought for their lives and survive another day..."

        return result
