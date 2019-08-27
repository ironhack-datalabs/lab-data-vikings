#Starting my own battle 22222222222222222222222222222

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

# 
    def attack(self):    
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        pass

#Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.health=health
        self.strength=strength
        self.name=name

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health<1:
            return(self.name + "has died in act of combat")
        elif self.health>=1:
            return (self.name + "has received"+ str(self.damage) + "points of damage")

'''
    def battleCry(self,battlecry):
        self.battlecry()=battleCry
        return("Odin Owns You ALL")
    pass
'''
# Saxon


class Saxon:
    pass

# War


class War:
    pass
