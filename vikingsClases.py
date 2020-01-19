# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        health = health - damage
    
# Viking
class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength) 
        self.name = name

    def attack(self):
        super().__init__() 

    def receiveDamage(self, damage):
        super().__init__(self, damage) #Incorporar aquí la función de restar al health el damage.
        self.damage = damage
    
        if self.health > 0:
            return (str(self.name)) + " has received " + (str(self.damage)) + " points of damage"
        elif self.health <= 0:
            return (str(self.name)) + " has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__() #Tiene las mismas características que un soldado
    
    def attack(self):
        super().__init__() # Llamar esta función desde la de soldier
        
    def receiveDamage(self, damage):
        # Llamar la parte de Viking de esta misma función
        
        if self.health > 0:
            return "A Saxon has received " + (str(self.damage)) + " points of damage"
        elif self.health <= 0:
            return  "A Saxon has died in combat"
    

# War
class War:
    def __init__(vikingArmy, saxonArmy):
        self.vikingArmy = vikingArmy
        self.saxonArmy = saxonArmy

    def addViking(self, viking):
        vikingArmy = vikingArmy + viking
    
    def addSaxon(self, saxon):
        saxonArmy = saxonArmy + saxon
    
    def vikingAttack(): 
        Saxon.health = health - viking.strength #pero con sintaxis buena
        return Saxon.receiveDamage (self, damage)

    def saxonAttack():
        Viking.health = health - saxon.strength
        return Viking.receiveDamage (self, damage)
   
    def showStatus():

        if saxonArmy == 0:
            return "Vikings have won the war of the century!"
        elif vikingArmy == 0:
                return "Saxons have fought for their lives and survive another day..."
        else: 
            return "Vikings and Saxons are still in the thick of battle."