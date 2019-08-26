
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
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        health - damage
        if health > damage:
            return self.name + " has received" + self.damage + " points of damage"
        elif healt <= damage:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"
        pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack():
        pass
    def recieveDamage():
        pass

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []


# War métodos

    def addViking():
        pass
    def addSaxon():
        pass
    def vikingAttack():
        pass
    def saxonAttack():
        pass
    def showStatus():
        pass
   
