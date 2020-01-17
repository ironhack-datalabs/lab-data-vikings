
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

    #attack se hereda automaticamente

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if(self.health > 0):
            return self.name+" has received "+str(damage)+" points of damage"
        else:
            return self.name+" has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    #attack se hereda automaticamente

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if(self.health > 0):
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        #viki = 
        #saxo = 

    def saxonAttack():
        pass

    def showStatus():
        pass
