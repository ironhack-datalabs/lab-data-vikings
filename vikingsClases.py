
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
    
    def __init__(self, health, strength, name):
        self.name = name 
        super().__init__(health, strength)
       
      
    def receiveDamage(self, damage): 
        self.health = self.health - damage 
        if self.health > 0:
            return ("{} has received {} points of damage").format(self.name, damage)
        else:
            return ("{} has died in act of combat").format(self.name)

                          
    def battleCry(self):
             return 'Odin Owns You All!'
                     
             
 # Saxon

class Saxon(Soldier):
            
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
             return "A Saxon has received {} points of damage".format(damage)  
        else:
             return "A Saxon has died in combat"   
          
            
# War

class War:    
            
    def __init__(self):        
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
       
    def addSaxon(self, Saxon):
         self.saxonArmy.append(Saxon)
            
    def vikingAttack(self):
        import random
        random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).strength)
        if random.choice(self.saxonArmy).health <= 0:
            self.saxonArmy = self.saxonArmy - 1
        return random.choice(self.vikingArmy).strength
    
    def saxonAttack(self):
        import random
        random.choice(self.vikingArmy).receiveDamage(random.choice(self.saxonArmy).strength)
        if random.choice(self.vikingArmy).health <= 0:
            self.vikingArmy = self.vikingArmy - 1
        return random.choice(self.saxonArmy).strength
    
    def showStatus(self):
        if self.saxonArmy == 0:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy > 0 and self.vikingArmy > 0:
            return "Vikings and Saxons are still in the thick of battle."