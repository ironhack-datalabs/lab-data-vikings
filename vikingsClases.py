
import random

class Soldier:
    def __init__(self, health, strength):
        self.strength=strength
        self.health=health

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health=self.health-damage   #añadir condicional 

class Viking(Soldier):
    def __init__(self,name,health,strength):
        super(Viking, self).__init__(health, strength)
        self.name=name
               
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)
    def battleCry(self):
        return "Odin Owns You All!"

class Saxon(Soldier):
    def __init__(self,health,strength):
        super(Saxon, self).__init__(health,strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.viking=Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.Saxon=Saxon
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        Aleatorio= random.randint(self.vikingArmy, self.saxonArmy)

        Vikingo = Viking()
        vikingo.strength
        return  receiveDamage()

        var vikingAttackReturn = randomSaxon.receiveDamage(randomViking.strength)

