import numpy as np



# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    
    #Methods
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = health - damage
    
    
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    
    #Methods (attack method is inherited from Soldier class)
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = health - damage
        if self.health > 0:
            return print("{} has received {} points of damage.".format(self.name, self.damage))
        else:
            return print("{} has died in act of combat.".format(self.name))
        
    def battleCry(self):
        return print("Odin Owns You All!")
    
    


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    
    #Methods (attack method is inherited from Soldier class)
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = health - damage
        if self.health > 0:
            return print("A Saxon has received {} points of damage.".format(self.damage))
        else:
            return print("A Saxon has died in combat.")
        
        


# War


class War:
    def __init__(self, vikingArmy, saxonArmy):
        self.vikingArmy = np.array(vikingArmy)
        
