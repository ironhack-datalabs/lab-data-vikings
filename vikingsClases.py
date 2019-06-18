import random
# Soldier

class Soldier():
    def __init__ (self,health,strength):
        self.strength = strength
        self.health = health

    def attack(self):
    #should return **the `strength` property of the `Soldier`*
        return self.strength
    
    def receiveDamage(self,damage):
        self.health -= damage

class Viking(Soldier):
    def __init__(self,name,health,strength):
        super(Viking, self).__init__(health,strength)
        self.name = name
    def attack (self):
        super(Viking, self).attack()
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
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
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0: 
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        #hacer un Saxon receiveDamage()igual al strength de un Viking
        v = random.choice(range(len(self.vikingArmy)))
        s = random.choice(range(len(self.saxonArmy)))
        #gv = self.vikingArmy[a]
        #gs = self.saxonArmy[b]
        ataque = self.saxonArmy[s].receiveDamage(self.vikingArmy[v].attack())
        if self.saxonArmy[s].health <= 0:
            self.saxonArmy.remove(self.saxonArmy[s])
        return ataque

    def saxonAttack(self):
        c = random.choice(range(len(self.vikingArmy)))
        d = random.choice(range(len(self.saxonArmy)))
        #gvv = self.vikingArmy[c]
        #gss = self.saxonArmy[d]
        ataq_s = self.vikingArmy[c].receiveDamage(self.saxonArmy[d].attack())
        if self.vikingArmy[c].health <= 0:
            self.vikingArmy.remove(self.vikingArmy[c])
        return ataq_s

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
    
        









