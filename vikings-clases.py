# soldier

class Soldier: 
    def __init__(self, health, strength): 
        self.health = health
        self.strength = strength
    def attack(self): 
        return self.strength
    def receiveDamage(self, damage): 
        self.health -= damage

# viking
class Vicking(Soldier): 
    def __init__(self, health, strenght, name): 
        Soldier.__init__(self, health, strenght)
        self.name = name
    
if __name__ == '__main__':
    vicky = Vicking(100, 50, 'vicky')
    vicky.receiveDamage(25)
    print(vicky.health)
    print('hola')