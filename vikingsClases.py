
# Soldier


class Soldier:
    
    def __init__(self, health, strengh):
        self.health = health
        self.strengh = strengh

    def attack(self):
        return self.strengh
    
    def receiveDamage(self, damage):
        self.health - damage
        


# Viking


class Viking(Soldier):

    def __init__(self, name, health, strengh):
        self.name = name
        super().__init__(health, strengh)
    
    def attack(self):
        super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health > 0:
            return "Viking has recived " + str(damage) + " points of damage."
        else:
            return "Viking has died in act of combat."


# Saxon


class Saxon:
    pass

# War


class War:
    pass
