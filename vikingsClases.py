import random

# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return(self.strength)

    def receiveDamage(self, damage):
        self.health = self.health-damage
        pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return("{} has received {} points of damage".format(self.name, damage))
        else:
            return("{} has died in act of combat".format(self.name))

    def battleCry(self):
        return ("Odin Owns You All!")

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return("A Saxon has received {} points of damage".format(damage))
        else:
            return("A Saxon has died in combat")
    pass

# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, cv):
        self.vikingArmy.append(cv)

    def addSaxon(self, cs):
        self.saxonArmy.append(cs)

    def vikingAttack(self):
        v = random.randrange(len(self.vikingArmy))
        s = random.randrange(len(self.saxonArmy))
        z = self.saxonArmy[s].receiveDamage(self.vikingArmy[v].attack())
        if self.saxonArmy[s].health <= 0:
            self.saxonArmy.remove(self.saxonArmy[s])
        return z

    def saxonAttack(self):
        v = random.randrange(len(self.vikingArmy))
        s = random.randrange(len(self.saxonArmy))
        z = self.vikingArmy[s].receiveDamage(self.saxonArmy[v].attack())
        if self.vikingArmy[v].health <= 0:
            self.vikingArmy.remove(self.vikingArmy[v])
        return z

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

# todo listo
