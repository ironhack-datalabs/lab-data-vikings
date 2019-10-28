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


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy += Viking

    def addSaxon(self, Saxon):
        self.saxonArmy += Saxon

    def vikingAttack(self):
        receiveDamage()

    def saxonAttack(self):
        pass

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) > 1 and len(self.saxonArmy) > 1:
            return "Vikings and Saxons are still in the thick of battle."
