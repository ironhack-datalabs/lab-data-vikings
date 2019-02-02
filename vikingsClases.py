
# Soldier


class Soldier:
    pass
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    pass
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def attack(self):
        Soldier.attack(self)
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    pass
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        Soldier.attack(self)
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War(Soldier):
    pass
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        damage = self.Viking.strength
        Saxon.receiveDamage(self, damage)
        self.health = self.health - damage
        if self.Saxon.health == 0:
            self.saxonArmy.remove(Saxon)
        return Saxon.receiveDamage - self.Viking.strength   
        #Saxon.receiveDamage = self.Viking.strength
        #if self.Saxon.health == 0:
            #vikingArmy.remove(Saxon)
        #return Saxon.receiveDamage - self.Viking.strength

    def saxonAttack(self):
        damage = self.Saxon.strength
        Viking.receiveDamage(self, damage)
        self.health = self.health - damage
        if self.Viking.health == 0:
            self.vikingArmy.remove(Viking)
        return Viking.receiveDamage - self.Saxon.strength
        #Viking.receiveDamage = self.Saxon.strength
        #if self.Viking.health == 0:
            #saxonArmy.remove(Viking)
        #return Viking.receiveDamage - self.Saxon.strength

    def showStatus(self):
        if self.vikingArmy == False:
            return "Vikings have won the war of the century!"
        elif self.saxonArmy == False:
            return "Saxons have fought for their lives and survive another day..."
        elif self.vikingArmy == True and self.saxonArmy == True:
            return "Vikings and Saxons are still in the thick of battle."