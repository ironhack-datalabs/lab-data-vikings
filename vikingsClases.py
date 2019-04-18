
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return(self.strength)

    def receiveDamage(self, damage):
        self.health-=damage
   
    

# Viking


class Viking(Soldier):
               
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
     

    def receiveDamage(self, damage):
        self.health-=damage
        #super().receiveDamage(damage)
        if self.health > 0:
            return("{} has received {} points of damage".format(self.name, damage))
        else:
            return("{} has died in act of combat".format(self.name))
#""NAME has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

    
        

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
     

    def receiveDamage(self, damage):
        self.health-=damage
        #super().receiveDamage(damage)
        if self.health > 0:
            return("A Saxon has received {} points of damage".format(damage))
        else:
            return("A Saxon has died in combat")

# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []


    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
       
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        import random
        x=random.choice(self.vikingArmy)
        y=random.choice(self.saxonArmy)
        if y.health <=0:
            self.saxonArmy.remove(y)
        return y.receiveDamage(x.strength)

  
   def saxonAttack(self):
        q=random.choice(self.vikingArmy)
        z=random.choice(self.saxonArmy)
        if z.health <=0:
            self.vikingArmy.remove(z)
        return q.receiveDamage(z.strength)
   # def showStatus()

