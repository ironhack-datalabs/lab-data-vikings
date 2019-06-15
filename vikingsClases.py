
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
        self.viking = Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.Saxon=Saxon
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        Aleatorio_viking = random.choice(self.vikingArmy)
        Aleatorio_saxon = random.choice(self.saxonArmy)
        AtaqueVikingo = Aleatorio_saxon.receiveDamage(Aleatorio_viking.attack())
        
        if Aleatorio_saxon.health <=0:
            self.saxonArmy.remove(Aleatorio_saxon)
        return AtaqueVikingo

    def saxonAttack(self):
        Aleatorio_viking = random.choice(self.vikingArmy)
        Aleatorio_saxon = random.choice(self.saxonArmy)
        AtaqueSaxon = Aleatorio_viking.receiveDamage(Aleatorio_saxon.attack())

        if Aleatorio_viking.health <= 0:
            self.vikingArmy.remove(Aleatorio_viking)
        
        return AtaqueSaxon

    def showStatus(self):
        if self.saxonArmy == [] :
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy != [] or self.vikingArmy != []:
            return "Vikings and Saxons are still in the thick of battle."