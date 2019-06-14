

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage=damage
        self.health -= damage


# Viking

"""
class Viking:
    def __init__(self, health, strength, name):
        super(Viking, self).__init__(health, strength)
        self.name=name
"""
# Saxon


class Saxon:
    pass

# War


class War:
    pass
