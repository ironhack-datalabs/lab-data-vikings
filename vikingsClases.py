
# Soldier
import random


class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health - damage

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage

        if self.health > 0:
            return("{} has received {} points of damage".format(self.name, damage))
        else:
            return("{} has died in act of combat".format(self.name))

    def battleCry(self):
        return ("Odin Owns You All!")

# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return("A Saxon has received {} points of damage".format(damage))
        else:
            return("A Saxon has died in combat")


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        randsaxon = random.choice(self.saxonArmy)
        randviking = random.choice(self.vikingArmy)
        saxondamage = randsaxon.receiveDamage(randviking.attack())
        if randsaxon.health <= 0:
            self.saxonArmy.remove(randsaxon)
        return saxondamage

    def saxonAttack(self):
        randsaxon = random.choice(self.saxonArmy)
        randviking = random.choice(self.vikingArmy)
        vikingdamage = randviking.receiveDamage(randsaxon.attack())
        if randviking.health <= 0:
            self.vikingArmy.remove(randviking)
        return vikingdamage

    def showStatus(self):

        if len(self.saxonArmy) and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        else:
            return "Saxons have fought for their lives and survive another day..."

        '''
        #ALSO WITH NESTED ITERATION
        while len(self.saxonArmy) and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."

        else:
            if len(self.saxonArmy) == 0:
                return "Vikings have won the war of the century!"
            else:
                return "Saxons have fought for their lives and survive another day..."
        '''
