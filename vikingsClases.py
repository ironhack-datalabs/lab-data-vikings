import numpy as np
import random as rd



# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    
    #Methods
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
    
    
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    
    #Methods (attack method is inherited from Soldier class)
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "{} has received {} points of damage.".format(self.name, damage)
        else:
            return "{} has died in act of combat.".format(self.name)
        
    def battleCry(self):
        return "Odin Owns You All!"
    
    


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    
    #Methods (attack method is inherited from Soldier class)
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received {} points of damage.".format(damage)
        else:
            return "A Saxon has died in combat."
        
        


# War


class War:
    def __init__(self, vikingArmy, saxonArmy):
        self.vikingArmy = list()
        self.saxonArmy = list()
    
    
    #Methods
    def addViking(self, viking):
        add_viking = rd.choice(vikingArmy)
        self.vikingArmy.append(add_viking)
    
    def addSaxon(self, saxon):
        add_saxon = rd.choice(saxonArmy)
        self.saxonArmy.append(add_saxon)
        
        
    #A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.    
    def vikingAttack(self):
        viking_attack = rd.choice(self.vikingArmy)
        saxon_damaged = rd.choice(self.saxonArmy)
        conclusion = saxon_damaged.receiveDamage(viking_attack.strength)
        if saxon_damaged.health < 0:
            self.saxonArmy.remove(saxon_damaged)
        return conclusion
    
    def saxonAttack(self):
        saxon_attack = rd.choice(self.saxonArmy)
        viking_damaged = rd.choice(self.vikingArmy)
        conclusion2 = viking_damaged.receiveDamage(saxon_attack.strength)
        if viking_damaged.health < 0:
            self.vikingArmy.remove(viking_damaged)
        return conclusion2
    
    def showStatus(self):
        if self.saxonArmy <= 0:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
        if self.vikingArmy <= 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
