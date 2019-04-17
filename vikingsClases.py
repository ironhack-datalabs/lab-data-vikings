
# Soldier


class Soldier:
    def __init__(self,health,strength):
     self.health = health
     self.strength = strength

    def attack(self): 
        return self.strength
        
    def receiveDamage(self,damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.strength = strength

    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health >0:
            return ("{} has received {} points of damage" .format(self.name, damage))
        else:
            return ("{} has died in act of combat".format(self.name))
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health >0:
            return ("A Saxon has received {} points of damage" .format(damage))
        else:
            return ("A Saxon has died in combat")
# Wars

class War():
    def__init__(self):
        self.vikingArmy = []
        self.saxonArmy = []