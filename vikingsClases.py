
# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.strength = strength
        self.health = health
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name, damage)
        else:
            return '{} has died in act of combat'.format(self.name)
    def battleCry(self):
        return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):
    def receiveDamage(self,damage):
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
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        saxon_damage = saxon.receiveDamage(viking.attack())
        self.saxonArmy = [s for s in self.saxonArmy if s.health > 0]
        return saxon_damage
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        viking_damage = viking.receiveDamage(saxon.attack())
        self.vikingArmy = [v for v in self.vikingArmy if v.health > 0]
        return viking_damage
    def showStatus(self):
        if not len(self.saxonArmy):
            return 'Vikings have won the war of the century!'
        elif not len(self.vikingArmy):
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
