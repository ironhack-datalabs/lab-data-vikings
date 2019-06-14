
import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        super(Viking, self).receiveDamage(damage)
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        super(Saxon, self).receiveDamage(damage)
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
        p_saxo = random.randint(0 ,len(self.saxonArmy)-1)
        saxon = self.saxonArmy[p_saxo]
        result = saxon.receiveDamage(random.choice(self.vikingArmy).strength)
        if "died" in result:
            self.saxonArmy.pop(p_saxo)
        return result

    def saxonAttack(self):
        p_viking = random.randint(0, len(self.vikingArmy)-1)
        viking = self.vikingArmy[p_viking]
        result = viking.receiveDamage(random.choice(self.saxonArmy).strength)
        if "died" in result:
            self.vikingArmy.pop(p_viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

