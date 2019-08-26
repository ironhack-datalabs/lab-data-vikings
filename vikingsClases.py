import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage=0):
        # This will probably need to be changed in the future due to over complicating the function
        if self.health > 0:
            if (self.health - damage) <= 0:
                self.health = 0
            else:
                self.health -= damage
        else:
            0


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage=0):
        self.health -= damage
        if self.health <= 0:
            return self.name + " has died in act of combat"
        else:
            return self.name + " has received " + str(damage) + " points of damage"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage=0):
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received " + str(damage) + " points of damage"


# War

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking_soldier):
        if isinstance(viking_soldier, Viking):
            self.vikingArmy.append(viking_soldier)

    def addSaxon(self, saxon_soldier):
        if isinstance(saxon_soldier, Saxon):
            self.saxonArmy.append(saxon_soldier)

    def vikingAttack(self):
        a = random.choice(self.vikingArmy)
        b = random.choice(self.saxonArmy)
        res = b.receiveDamage(a.strength)
        if b.health <= 0:
            self.saxonArmy.remove(b)
        return res

    def saxonAttack(self):
        a = random.choice(self.vikingArmy)
        b = random.choice(self.saxonArmy)
        res = a.receiveDamage(b.strength)
        if a.health <= 0:
            self.vikingArmy.remove(a)
        return res

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
