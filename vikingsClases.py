
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, dmg):
        self.health -= dmg

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, dmg):
        self.health -= dmg
        return (self.name + ' has received ' + str(dmg) + ' points of damage') if self.health > 0 else (self.name + ' has died in act of combat')
    
    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, dmg):
        self.health -= dmg
        return ('A Saxon has received ' + str(dmg) + ' points of damage') if self.health > 0 else ('A Saxon has died in combat')
    
# War

import random 

class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, vikingo):
        self.vikingArmy.append(vikingo)
        
    def addSaxon(self, saxono):
        self.saxonArmy.append(saxono)
        
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damageDone = saxon.receiveDamage(viking.strength)
        
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            
        return damageDone
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damageDone = viking.receiveDamage(saxon.strength)      
        
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        
        return damageDone
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
    
        
        
        

        
        