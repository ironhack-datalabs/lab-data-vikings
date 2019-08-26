import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return(self.strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
        #self.health = health
        #self.strength = strength

    def receiveDamage(self, damage):
        self.health = self.health - damage

        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):

    def receiveDamage(self, damage):
        self.health = self.health - damage

        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking_soldier):
        self.vikingArmy.append(viking_soldier)

    def addSaxon(self, saxon_soldier):
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
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."

        else:
            return "Vikings and Saxons are still in the thick of battle."
