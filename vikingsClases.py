import random


# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        #llamamos a super 
        Soldier.__init__(self,health,strength)



    def receiveDamage(self,damage):
        
        self.health -= damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
    
class Saxon(Soldier):
    def receiveDamage(self,damage):
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
    

    def addViking(self,Viking):
        self.vikingArmy.append(Viking)


    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        #se elige un numero aleatorio desde el principio hasta el final de la lista
        sizeSaxon = len(self.saxonArmy)
        sizeViking = len(self.vikingArmy)
        saxonRandom = self.saxonArmy[random.randrange(0,sizeSaxon)]
        vikingRandom = self.vikingArmy[random.randrange(0,sizeViking)]
        isLive =saxonRandom.receiveDamage(vikingRandom.attack())

        if sizeSaxon and isLive == "A Saxon has died in combat":
            self.saxonArmy.remove(saxonRandom)

        return isLive

    def saxonAttack(self):
        sizeSaxon = len(self.saxonArmy)
        sizeViking = len(self.vikingArmy)
        saxonRandom = self.saxonArmy[random.randrange(0,sizeSaxon)]
        vikingRandom = self.vikingArmy[random.randrange(0,sizeViking)]
        isLive =vikingRandom.receiveDamage(saxonRandom.attack())
        
        if sizeViking and vikingRandom.name + " has died in act of combat" == isLive:
            self.vikingArmy.remove(vikingRandom)
        

        return isLive

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        if self.vikingArmy and self.saxonArmy:
            return "Vikings and Saxons are still in the thick of battle."








