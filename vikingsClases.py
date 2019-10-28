from random import choice

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health> 0:
            return '{} has received {} points of damage'.format(self.name, damage)
        elif self.health <= 0:
            return '{} has died in act of combat'.format(self.name)
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(damage)
        elif self.health <= 0:
            return 'A Saxon has died in combat'

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
#         print('Vikings are {} and Saxons are {}'.format(self.vikingArmy,self.saxonArmy))
    def addViking(self, viking):
        self.vikingArmy.append(viking)  
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        chosenVik = choice(self.vikingArmy)
        chosenSax = choice(self.saxonArmy)
        result = chosenSax.receiveDamage(chosenVik.strength)
        if chosenSax.health <= 0:
            self.saxonArmy.remove(chosenSax)
        return result
    def saxonAttack(self):
        chosenVik = choice(self.vikingArmy)
        chosenSax = choice(self.saxonArmy)
        result = chosenVik.receiveDamage(chosenSax.strength)
        if chosenVik.health <= 0:
            self.vikingArmy.remove(chosenVik)
        return result
    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) >0:
            return "Vikings and Saxons are still in the thick of battle."


