
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
    def __init__(self, name, health,strength):
        self.name = name
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
            
        else:
            
            return f"{self.name} has died in act of combat"
        

    def battleCry(self):
        return "Odin Owns You All!"
    


# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

import random 

class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
    
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        damage = saxon.receiveDamage(viking.attack())
        
        print(self.saxonArmy)
        print(viking.strength)
        print(saxon.health)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return damage
    

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = viking.receiveDamage(saxon.attack())
        if viking.health <= 0: 
            self.vikingArmy.remove(viking)
        return damage

    def showStatus(self):

        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return  "Vikings and Saxons are still in the thick of battle."



    



