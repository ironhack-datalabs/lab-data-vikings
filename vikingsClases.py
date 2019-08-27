
# Soldier

class Soldier():
    def __init__(self, health, strength): 
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage): 
        self.health = self.health - damage 
    
    

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
            self.health -= damage
            if self.health > 0: 
                return(str(self.name) + " has received " + str(damage) + " points of damage")
            else:
                return(str(self.name) + " has died in act of combat")
                       
    def battleCry(self):
        return ("Odin Owns You All!")
                
    

# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
    

# War

import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking_soldier):
        self.vikingArmy.append(viking_soldier)
        
    def addSaxon(self, saxon_soldier):
        self.saxonArmy.append(saxon_soldier)
        
    def vikingAttack(self):
        random_vkg = random.choice(self.vikingArmy)
        random_sxn = random.choice(self.saxonArmy)
        vrd = random_sxn.receiveDamage(random_vkg.strength)
        if random_sxn.health <= 0:
            self.saxonArmy.remove(random_sxn)
        return vrd
        
    def saxonAttack(self):
        random_vkg = random.choice(self.vikingArmy)
        random_sxn = random.choice(self.saxonArmy)
        srd = random_vkg.receiveDamage(random_sxn.strength)
        if random_vkg.health <= 0:
            self.vikingArmy.remove(random_vkg)
        return srd
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
        
        
        
        
        
        
        
        
