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
        super().receiveDamage(damage)
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name, damage)
        else:
            return '{} has died in act of combat'.format(self.name)

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(damage)
        else:
            return 'A Saxon has died in combat'

# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        id_saxon = 0  # random.randint(0, len(self.saxonArmy))
        id_viking = 0  # random.randint(0, len(self.vikingArmy))

        saxon = self.saxonArmy[id_saxon]
        viking = self.vikingArmy[id_viking]

        if saxon.health <= 0:
            self.saxonArmy.pop(id_saxon)

        return saxon.receiveDamage(viking.strength)

    def saxonAttack(self):
        id_saxon = 0  # random.randint(0, len(self.saxonArmy))
        id_viking = 0  # random.randint(0, len(self.vikingArmy))

        saxon = self.saxonArmy[id_saxon]
        viking = self.vikingArmy[id_viking]

        if viking.health <= 0:
            self.vikingArmy.pop(id_viking)

        return viking.receiveDamage(saxon.strength)

    def showStatus(self):

        num_saxon = len(self.saxonArmy)
        num_viking = len(self.vikingArmy)

        if num_saxon == 0:
            return 'Vikings have won the war of the century!'
        elif num_viking == 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif num_saxon > 0 and num_viking > 0:
            return 'Vikings and Saxons are still in the thick of battle.'


if __name__ == '__main__':
    pass
