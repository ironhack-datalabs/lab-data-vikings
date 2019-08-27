
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
          
    
    def recieveDamage(self, damage):
        self.health = self.health - damage
        


# Viking

class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name = name
        
        super().__init__(health, strength)
       #Soldier.__init__(self,health,strength)
    
    def recieveDamage(self, damage):
        #self.health = self.health - damage (ESTO ES LO MISMO QUE: super().receiveDamage(damage))
        super().recieveDamage(damage)
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else: 
            return "{} has died in act of combat".format(self.name)
    
    
    def battleCry(self):
        return "Odin Owns You All!"
        
        

# Saxon


class Saxon(Soldier):
    
   # def __init__(self, health, strength):
        
        Soldier.__init__(self,health, strength)
    
    def recieveDamage(self, damage):
        #self.health = self.health - damage
        super().recieveDamage(damage)
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else: 
            return "A Saxon has died in combat"
        
    


# War
from random import choice

class War(self):
    
     def __init__(self):
            self.vikingarmy = []
            self.saxonarmy = []
    
        def addViking(self, viking):
            self.vikingarmy.append(viking)
    
    
        def addSaxon(self, saxon):
            self.saxonarmy.append(saxon)
    
    
    
        def vikingAttack(self):
            random_viking = choice(self.vikingarmy)
            random_saxon = choice(self.saxonarmy)
            
            result = random_saxon.recieveDamage(random_viking.attack())
            
            if random_saxon.health <= 0:
                self.saxonarmy.remove(random_saxon)
            return result
            
        
        def saxonAttack(self):
            
            random_viking = choice(self.vikingarmy)
            random_saxon = choice(self.saxonarmy)
            
            result = random_viking.recieveDamage(random_saxon.attack())
            
            if random_viking.health <= 0:
                self.vikingarmy.remove(random_viking)
            return result
            
            
    
        def showStatus(self):
            if len(saxonarmy) == 0:
                return "Vikings have won the war of the century!"
            if len(vikingarmy) == 0:
                return "Saxons have fought for their lives and survive another day..."
            else:
                return "Vikings and Saxons are still in the thick of battle"
