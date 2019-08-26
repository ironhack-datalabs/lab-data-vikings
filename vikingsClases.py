import random as rd

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
         
    def receiveDamage(self, damage):
        self.health = self.health - damage
          
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + " has received " +  str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
        
    # Saxon

class Saxon(Soldier):
    
      
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " +  str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, vik):
        if isinstance(vik, Viking):
            self.vikingArmy.append(vik)
                
     
    def addSaxon(self, sax):
        if isinstance(sax, Saxon):
            self.saxonArmy.append(sax)
            
    def vikingAttack(self):
        v = rd.choice(self.vikingArmy)
        s = rd.choice(self.saxonArmy)
        
        dam_sa = s.receiveDamage(v.attack())
       
        if s.health <= 0:
            self.saxonArmy.remove(s)
        
        return dam_sa
    
    def saxonAttack(self):
        u = rd.choice(self.vikingArmy)
        i = rd.choice(self.saxonArmy)
        
        dam_vi = u.receiveDamage(i.attack()) 
        
        if u.health <= 0 :
            self.vikingArmy.remove(u)
            
        return dam_vi
       
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
       
            
           
        
    
    
        
    
