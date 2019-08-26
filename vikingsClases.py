
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


class Viking(Soldier):
    def __init__(self,name,health,strenght):
        Soldier.__init__(self, health, strenght)
        self.name = name
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)
    
    def battleCry(self):
        return "Odin Owns you All!"

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strenght):
        Soldier.__init__(self, health, strenght)

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in act of combat"
        

# War


class War:
    pass
