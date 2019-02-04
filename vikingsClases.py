
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

class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name 
    def receiveDamage (self, damage):
        self.health -= damage
        if self.health >0:
            return '{} has received {} points of damage'. format (self.name, damage)
        if self.health <=0:
            return '{} has died in act of combat'. format (self.name)
    def battleCry (self):
        return "Odin Owns You All!"

# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receiveDamage (self, damage):
        self.health -= damage
        if self.health >0:
            return 'A Saxon has received { } points of damage'. format (damage)
        if self.health <=0:
            return "A Saxon has died in combat"



# War


class War:

    def__init__(self,):
        vikingArmy = []
        saxonArmy = []
    def addViking (self, Viking)
        self.Viking = Viking
        vikingArmy.append(Viking)
    def addSaxon (self, Saxon)
        self.Saxon = Saxon
        vikingSaxon.append(Saxon)
    def vikingAttack
    
