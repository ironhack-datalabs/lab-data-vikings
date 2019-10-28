
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
            return ('{} has received {} points of damage'.format(self.name, damage))
        else:
            return ('{} has died in act of combat'.format(self.name))

    def battleCry(self):
        return ("Odin Owns You All!")

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return ('A Saxon has received {} points of damage'.format(damage))
        else:
            return ('A Saxon has died in combat')
# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxson):
        self.saxonArmy.append(Saxson)

    def vikingAttack(self):
        saxsonpelea = random.choice(self.saxonArmy)
        vikingpelea = random.choice(self.vikingArmy)
        result = saxsonpelea.receiveDamage(vikingpelea.attack())
        if saxsonpelea.health <= 0:
            self.saxonArmy .remove(saxsonpelea)
        return result

    def saxonAttack(self):
        saxsonpelea = random.choice(self.saxonArmy)
        vikingpelea = random.choice(self.vikingArmy)
        result = vikingpelea.receiveDamage(saxsonpelea.attack())
        if vikingpelea.health <= 0:
            self.vikingArmy.remove(vikingpelea)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) != 0 and len(self.vikingArmy) != 0:
            return "Vikings and Saxons are still in the thick of battle."

        pass
