
# Soldier


class Soldier:

    def __init__(self, health=0 , strength=0):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health-=damage

# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
