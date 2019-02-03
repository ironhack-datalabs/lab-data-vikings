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
        self.health = self.health - self.damage
    
    
    

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    
    #Methods (attack method is inherited from Soldier class)
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return print("{} has received {} points of damage.".format(self.name, self.damage))
        else:
            return print("{} has died in act of combat.".format(self.name))
        
    def battleCry(self):
        self.battleCry = print("Odin Owns You All!")
        return self.battleCry
    
    


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    
    #Methods (attack method is inherited from Soldier class)
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return print("A Saxon has received {} points of damage.".format(self.damage))
        else:
            return print("A Saxon has died in combat.")
        
        


# War


class War:
    def __init__(self, vikingArmy, saxonArmy):
        self.vikingArmy = np.array(vikingArmy)
        self.saxonArmy = np.array(saxonArmy)
    
    
    #Methods
    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)
    
    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(self.saxon)
        
        
    #A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.    
    def vikingAttack(self):
        if Saxon.health < 0:
            self.saxonArmy.remove(self.saxon)
        return receiveDamage(Saxon, damage = Viking.strength)
    
    def saxonAttack(self):
        if Viking.health < 0:
            self.vikingArmy.remove(self.viking)
        return receiveDamage(Viking, damage = Saxon.strength)
    
    def showStatus(self):
        if self.saxonArmy <= 0:
            return print("Vikings have won the war of the century!")
        else:
            return print("Vikings and Saxons are still in the thick of battle.")
        if self.vikingArmy <= 0:
            return print("Saxons have fought for their lives and survive another day...")
        else:
            return print("Vikings and Saxons are still in the thick of battle.")
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
