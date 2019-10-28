
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
    
    def attack(self):
        
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

       
# Viking


class Viking(Soldier):
    def __init__(self,name,health, strength):
        super().__init__(health,strength)        
        self.name = name


    def receiveDamage(self,damage): 
        self.health -= damage
        
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name,damage)
        if self.health <= 0:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
  
class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)

    def receiveDamage(self,damage):  
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage" .format(damage)
        if self.health <= 0:
            return "A Saxon has died in combat"
    

# War
import random
   

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,Viking):
        
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
       
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        vikingo_ale= random.choice(self.vikingArmy)
        saxon_ale = random.choice(self.saxonArmy)
        ataque =saxon_ale.receiveDamage(vikingo_ale.attack())
        

        '''utilizar remove'''
        if vikingo_ale.health <= 0:
            self.vikingArmy.remove(vikingo_ale)

        return ataque

        
    
    def saxonAttack(self):  
        vikingo_ale= random.choice(self.vikingArmy)
        saxon_ale = random.choice(self.saxonArmy)
        ataque =vikingo_ale.receiveDamage(saxon_ale.attack())
        
        if saxon_ale.health <= 0:
            saxonArmy.remove(saxon_ale)

        return ataque    

    def showStatus(self):  
        '''if not self.saxonArmy in saxon_ale:'''
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day ..."    
        else:
            return "Vikings and Saxons are still in the thick of the battle."



