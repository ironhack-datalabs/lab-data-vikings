
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health

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

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        chosen_saxon = random.choice(self.saxonArmy)

        chosen_viking = random.choice(self.vikingArmy)
        attack = chosen_saxon.receiveDamage(chosen_viking.strength)
        if chosen_saxon.health <= 0:
            self.saxonArmy.pop(self.saxonArmy.index(chosen_saxon))
        return attack

    def saxonAttack(self):
        import random
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        attack = chosen_viking.receiveDamage(chosen_saxon.strength)
        if chosen_viking.health <= 0:
            self.vikingArmy.pop(self.vikingArmy.index(chosen_viking))
        return attack

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
