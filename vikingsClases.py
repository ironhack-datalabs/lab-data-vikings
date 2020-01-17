import random

# Soldier


class Soldier(object):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

    pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return str(self.name) + ' has died in act of combat'
        else:
            return str(self.name) + ' has received ' + str(damage) + ' points of damage'

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        super().attack()
        pass

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return 'A Saxon has died in combat'
        else:
            return 'A Saxon has received ' + str(damage) + ' points of damage'
        pass

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        pass

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        pass

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        pass

    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        return saxon.receiveDamage(viking.attack())

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        return viking.receiveDamage(saxon.attack())

    def showStatus(self):
        if self.saxonArmy == []:
            return 'Vikings have won the war of the century!'
        elif self.vikingArmy == []:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle'
        pass
