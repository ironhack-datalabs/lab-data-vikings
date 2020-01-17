
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

       #  python3 1-testsSoldier.py
       
# Viking

class Viking:
    
    def __init__(self, name, health, strength):
        super().__init__() 
        self.name = name
        self.strength = strength
        self.health = health
        
    def attack():
        super().__init__() 


    def receiveDamage(self, damage):
        super().__init__() 
        self.damage = damage
    
        if self.health > 0:
            return self.name, "has received ", self.damage, "points of damage"
        elif self.health <= 0: 
            return self.name, "has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

#  python3 2-testsVikings.py





# Saxon


class Saxon:
    pass

# War


class War:
    pass
