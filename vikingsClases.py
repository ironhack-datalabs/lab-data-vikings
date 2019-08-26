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
        Soldier.__init__(self, health, strength)
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
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking_s):
        self.vikingArmy.append(viking_s)

    def addSaxon(self, saxon_s):
        self.saxonArmy.append(saxon_s)

    def vikingAttack(self):
        viking_attack = random.choice(self.vikingArmy)
        saxon_attack = random.choice(self.saxonArmy)
        res = saxon_attack.receiveDamage(viking_attack.strength)
        if saxon_attack.health <= 0:
            self.saxonArmy.remove(saxon_attack)
        return res

    def saxonAttack(self):
        viking_attack = random.choice(self.vikingArmy)
        saxon_attack = random.choice(self.saxonArmy)
        res = viking_attack.receiveDamage(saxon_attack.strength)
        if viking_attack.health <= 0:
            self.vikingArmy.remove(viking_attack)
        return res

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
