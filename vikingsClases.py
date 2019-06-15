# Soldier
import random


class Soldier:
    def __init__(self, health, strength):

        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name


class Viking (Soldier):

    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)

        self.name = name

    def receiveDamage(self, damage):
        super(Viking, self).receiveDamage(damage)

        self.health -= damage

        if self.health > 0:

            return "{} has received {} points of damage".format(self.name, damage)

        else:

            return "{} has died in act of combat".format(self.name)

    def battleCry(self):

        return "Viva la virgen de la Macarena"


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)

    def receiveDamage(self, damage):
        super(Saxon, self).receiveDamage(damage)

        if self.health > 0:

            return "A Saxon has received {} points of damage".format(self.damage)

        else:

            return "A Saxon has died in combat"


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.Viking = Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):

        random_saxon = random.choice(self.saxonArmy)

        random_viking = random.choice(self.vikingArmy)

        vik_attack = random_saxon.receiveDamage(random_viking.attack())

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return vik_attack

    def saxonAttack(self):

        random_saxon = random.choice(self.saxonArmy)

        random_viking = random.choice(self.vikingArmy)

        sax_attack = random_viking.receiveDamage(random_saxon.health)

        if random_viking.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return sax_attack

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy == self.vikingArmy:
            return "Vikings and Saxons are still in the thick of battle."
