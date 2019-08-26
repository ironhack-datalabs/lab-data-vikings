
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
        self.health -= damage
        if self.health > damage:
            return "{} has received {} points of damage".format(self.name, damage)
        elif self.health <= damage:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"


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