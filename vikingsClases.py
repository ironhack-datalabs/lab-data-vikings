
# Soldier
class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self): 
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        Soldier.__init__(self,health,strength)
        self.name = name
    
    def receiveDamage(self):
        pass
    
    def battleCry(self):
        pass

    

    

# Saxon


class Saxon:
    pass

# War


class War:
    pass


v = Viking(1,2,"GOnzalo")
print(v.health)