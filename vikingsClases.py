import random


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        self.damage = damage


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):

        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, self.damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(self.damage)
        else:
            return "A Saxon has died in combat"


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        vikingo = random.choice(self.vikingArmy)
        sajon = random.choice(self.saxonArmy)
        estadosajon = sajon.receiveDamage(vikingo.attack())
        if sajon.health <= 0:
            self.saxonArmy.remove(sajon)
        return estadosajon

    def saxonAttack(self):
        sajon2 = random.choice(self.saxonArmy)
        vikingo2 = random.choice(self.vikingArmy)
        estadovikingo = vikingo2.receiveDamage(sajon2.attack())
        if vikingo2.health <= 0:
            self.vikingArmy.remove(vikingo2)
        return estadovikingo

    def showStatus(self):
        if len(self.saxonArmy) == 0 and ...:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and ...:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
