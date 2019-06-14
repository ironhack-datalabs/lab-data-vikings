
# Soldier


import random


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health-damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        super(Viking, self).receiveDamage(damage)
        if self.health > 0:
            return ('{} has received {} points of damage'.format(self.name, damage))
        else:
            return('{} has died in act of combat'.format(self.name))

    def battleCry(self):
        return ('Odin Owns You All!')


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)

    def receiveDamage(self, damage):
        super(Saxon, self).receiveDamage(damage)
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(damage)
        else:
            return 'A Saxon has died in combat'

    pass

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
        pv = random.randint(0, len(self.vikingArmy)-1)
        ps = random.randint(0, len(self.saxonArmy)-1)
        viking = self.vikingArmy[pv]
        saxon = self.saxonArmy[ps]
        att = self.saxonArmy[ps].receiveDamage(self.vikingArmy[pv].attack())

        if self.saxonArmy[ps].health <= 0:
            self.saxonArmy.remove(self.saxonArmy[ps])
            return att

    def saxonAttack(self):
        pv = random.randint(0, len(self.vikingArmy)-1)
        ps = random.randint(0, len(self.saxonArmy)-1)
        viking = self.vikingArmy[pv]
        saxon = self.saxonArmy[ps]

        att = self.vikingArmy[pv].receiveDamage(self.saxonArmy[ps].attack())

        if self.vikingArmy[ps].health <= 0:
            self.vikingArmy.remove(self.vikingArmy[pv])

        return att

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
