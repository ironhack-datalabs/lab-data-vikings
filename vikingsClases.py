import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
  
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        
    def attack(self):
        return super().attack()
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
            
    def battleCry(self):
        return "Odin Owns You All!"

#Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def attack(self):
        return super().attack()
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        randomViking = random.randint(0,len(self.vikingArmy) - 1)
        randomSaxon = random.randint(0, len(self.saxonArmy) - 1)
        confrontation = self.saxonArmy[randomSaxon].receiveDamage(self.vikingArmy[randomViking].attack())
        if confrontation == "A Saxon has died in combat":
            self.saxonArmy.remove(self.saxonArmy[randomSaxon])
        return confrontation
    def saxonAttack(self):
        randomViking = random.randint(0,len(self.vikingArmy) - 1)
        randomSaxon = random.randint(0, len(self.saxonArmy) - 1)
        confrontation = self.vikingArmy[randomViking].receiveDamage(self.saxonArmy[randomSaxon].attack())
        if " has died in act of combat" in confrontation:
            self.vikingArmy.remove(self.vikingArmy[randomViking])
        return confrontation
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."