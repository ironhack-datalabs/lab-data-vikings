
# Soldier


class Soldier:
    def __init__(self, health, strenght):
        self.health = health
        self.strenght = strenght
    
    def atack(self):
        return self.strenght

    def receiveDamage(self,damage):
        self.health = self.health - damage

    
# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
