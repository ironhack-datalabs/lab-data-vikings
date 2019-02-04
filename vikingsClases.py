
# Soldier


class Soldier:
    pass
    def __init__(self,health,strength):
       self.health = health
       self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking


class Viking(Soldier):
    pass
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name= name
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
          return "{} has died in act of combat".format(self.name)
    
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    pass
    def __init__(self, health, strength):
        super().__init__(health,strength)
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
          return "A Saxon has died in combat"


# War


class War:
    pass
    def __init__(self):
        self.vikingArmy= []
        self.saxonArmy=[] 

    def addViking(Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(Saxon):
        self.SaxonArmy.append(Saxon)
    


    
    def vikingAttack():
    
    def saxonAttack():

    def showStatus()

    