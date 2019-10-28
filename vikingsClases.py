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
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)

        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strenght):
        super().__init__(health, strenght)

    def receiveDamage(self, damage):
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

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking_rd = random.choice(self.vikingArmy)
        saxon_rd = random.choice(self.saxonArmy)
        saxon_rd.receiveDamage(viking_rd.strenght)

        if saxon_rd.health <= 0:
            self.saxonArmy.remove(saxon_rd)
        return saxon_rd.receiveDamage(viking_rd.strength)

    def saxonAttack(self):
        viking_rd = random.choice(self.vikingArmy)
        saxon_rd = random.choice(self.saxonArmy)
        viking_rd.receiveDamage(saxon_rd.strength)

        if viking_rd.health <= 0:
            self.vikingArmy.remove(viking_rd)
        return viking_rd.receiveDamage(saxon_rd.strength)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
