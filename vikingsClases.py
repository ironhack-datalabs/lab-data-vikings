
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
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)

        elif self.health <= 0:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
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

    def addViking(self, Viking):
        self.Viking = vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.Saxon = saxonArmy.append(Saxon)

    def vikingAttack(self):
        self.saxonArmy
