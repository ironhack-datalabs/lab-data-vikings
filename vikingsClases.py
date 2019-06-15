
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        attack = self.strength
        return attack
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = (self.health - damage)
       

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super (Viking, self).__init__(health, strength)
        self.name = name
 
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = (self.health - damage) 
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, self.damage)
        else:
            return "{} has died in act of combat".format(self.name)
    def battleCry(self):
        while self.attack:
            return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super (Saxon, self).__init__(health, strength)
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = (self.health - damage) 
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(self.damage)
        else:
            return "A Saxon has died in combat"        


# War


class War:
    pass
