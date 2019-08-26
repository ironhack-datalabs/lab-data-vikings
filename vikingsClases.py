
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

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking_soldier):
        self.vikingArmy = viking_soldier + self.vikingArmy
        
    def addSaxon(self, saxon_soldier):
        self.saxonArmy = saxon_soldier + self.vikingArmy
        
    def vikingAttack(self):
        random_a = random.choice(self.VikingArmy)
        random_b = random.choice(self.saxonArmy)
        rip = random_a.receiveDamage(a.strength)
        if b.health <= 0:
            self.VikingArmy.pop(viking_soldier)
        return rip
        
    def saxonAttack(self):
        random_a = random.choice(self.VikingArmy)
        random_b = random.choice(self.saxonArmy)
        rip = random_a.receiveDamage(a.strength)
        if b.health <= 0:
            self.VikingArmy.pop(viking_soldier)
        return rip
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
        
        
        
        
        
        
        
        
