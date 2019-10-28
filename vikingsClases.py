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
        if self.health == 0:
            return "{} has died in act of combat".format(self.name)

        else:
            return "{} has received {} points of damage".format(self.name, damage)

    def battleCry(self):
        return "Odin Owns You All!"

    pass


# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)

        else:
            return "A Saxon has died in combat"

    pass


# War
import random


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        peleitasS = random.choice(self.saxonArmy)
        peleitasV = random.choice(self.vikingArmy)

        result = peleitasS.receiveDamage(peleitasV.attack())

        if peleitasS.health <= 0:
            self.saxonArmy.remove(peleitasS)
        return result

    def saxonAttack(self):
        peleitasS = random.choice(self.saxonArmy)
        peleitasV = random.choice(self.vikingArmy)
        result = peleitasV.receiveDamage(peleitasS.attack())
        if peleitasV.health <= 0:
            self.vikingArmy.remove(peleitasV)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

        pass
