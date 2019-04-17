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
        s_saxon = random.choice(self.saxonArmy)
        s_viking = random.choice(self.vikingArmy)

        if s_saxon.health <= s_viking.strength:
            self.saxonArmy.remove(s_saxon)

        return s_saxon.receiveDamage(s_viking.strength)

    def saxonAttack(self):
        s_saxon = random.choice(self.saxonArmy)
        s_viking = random.choice(self.vikingArmy)

        if s_viking.health <= s_saxon.strength:
            self.vikingArmy.remove(s_viking)

        return s_viking.receiveDamage(s_saxon.strength)

    def showStatus(self):

        num_saxon = len(self.saxonArmy)
        num_viking = len(self.vikingArmy)

        if num_saxon == 0:
            return 'Vikings have won the war of the century!'
        elif num_viking == 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif num_saxon >= 1 and num_viking >= 1:
            return 'Vikings and Saxons are still in the thick of battle.'


if __name__ == '__main__':
    pass
