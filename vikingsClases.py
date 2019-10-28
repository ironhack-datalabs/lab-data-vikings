
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage
        

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength): 
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)  
        else:
            return "{} has died in act of combat".format(self.name)
        
    def battleCry(self):
        return "Odin Owns You All!"
        
# Saxon


class Saxon(Soldier):
# como Soldier ya tiene health como 1er agrumento y strength como 2º, simplemente 
# importando Soldier ya tengo lo que me piden
# tampoco hace falta reimplementar attack
# 
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War


class War:
    pass

