import random

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
        if self.health > 0:
            
            return "{} has received {} points of damage".format(self.name,self.damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            
            return "A Saxon has received {} points of damage".format(self.damage)
        else:
            return "A Saxon has died in combat"


# War


class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)

    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(self.saxon)

    def vikingAttack(self):
        self.ransax = random.choice(self.saxonArmy)
        self.ranvik = random.choice(self.vikingArmy)
        self.saxattacked = self.ransax.receiveDamage(self.ranvik.strength)
        self.saxonArmy[self.saxonArmy.index(self.ransax)] = self.saxattacked
        if self.ransax.health == 0:
            self.saxonArmy.remove(self.ransax)
        return self.saxattacked
        

    def saxonAttack(self):
        self.ransax = random.choice(self.saxonArmy)
        self.ranvik = random.choice(self.vikingArmy)
        self.vikattacked = self.ranvik.receiveDamage(self.ransax.strength)
        if self.ranvik.health == 0:
            self.vikingArmy.remove(self.ranvik)
        return self.vikattacked



    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


