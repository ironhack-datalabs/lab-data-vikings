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
            return "{} has received {} points of damage" .format(self.name, str(damage))
        else:
            return "{} has died in act of combat" .format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
    # super().receiveDamage()
        if self.health > 0:
            return "A Saxon has received {} points of damage" .format(str(damage))
        else:
            return "A Saxon has died in combat"


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking_1):
        self.vikingArmy.append(viking_1)

    def addSaxon(self, saxon_1):
        self.saxonArmy.append(saxon_1)

    def vikingAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        vikatt = sax.receiveDamage(vik.strength)
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        return vikatt

    def saxonAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        saxatt = vik.receiveDamage(sax.strength)
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        return saxatt

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
