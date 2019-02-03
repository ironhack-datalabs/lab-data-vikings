import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

# Viking

class Viking:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return ("{} has received {} points of damage".format(self.name,damage))
        else:
            return ("{} has died in act of combat".format(self.name))
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

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
        Viking = random.choice(self.vikingArmy)
        Saxon = random.choice(self.saxonArmy)
        Attack = Saxon.receiveDamage(Viking.strength)
        if Saxon.health <= 0: 
            self.saxonArmy.remove(Saxon)
        return Attack

    def saxonAttack(self):
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        Attack = Viking.receiveDamage(Saxon.strength)
        if Viking.health <= 0: 
            self.vikingArmy.remove(Viking)
        return Attack

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."