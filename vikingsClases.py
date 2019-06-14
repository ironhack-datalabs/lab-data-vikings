

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage=damage
        self.health -= damage



class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health,strength)
        self.name = name
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage=damage
        self.health -= damage
        if self.health> 0: 
            return  "{} has received {} points of damage".format(self.name, self.damage)
        elif self.health <= 0:
            return  "{} has died in act of combat".format(self.name)
    def battleCry (self):
        return "Odin Owns You All!"  
# Saxon


class Saxon:
    pass

# War


class War:
    pass
