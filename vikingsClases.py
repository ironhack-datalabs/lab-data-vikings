
# Soldier


class Soldier:
    
    def __init__(self, health, strengh):
        self.health = health
        self.strengh = strengh

    def attack(self):
        return self.strengh
    
    def receiveDamage(self, damage):
        return self.health - damage
        


# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
