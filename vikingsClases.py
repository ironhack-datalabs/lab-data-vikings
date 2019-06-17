
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        # params = [self.strength]
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        super(Viking, self)  # .__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, self.damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        super(Saxon, self)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(self.damage)
        else:
            return "A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.viking = Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxon = Saxon
        self.saxonArmy.append(Saxon)

    def vikingAttack():

        vik =
        for i in self.vikingArmy:
            if self.vikingArmy.health <= 0:

            return

    def saxonAttack():
        receive Damag
        for i in self.saxonArmy:
            if self.health < 0:

            return

    def showStatus():
        if len(saxonArmy) <= 0:
            return "Vikings have won the war of the century!"
        elif len(vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of the battle."
