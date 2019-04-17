
# Soldier


class Soldier:
    def __init__(self, health, strenght):
        self.health = health
        self.strenght = strenght

    def attack(self):
        return self.strenght
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strenght):
        self.name = name
        self.health = health
        self.strenght = strenght

    def super().receiveDamage(self, damage):
        self.health -= damage
        if health <= 0:
            print(name,'has died in act of combat')
        else:
            print(name,'has received',damage,'points of damage')

    def battleCry(self):
        print('Odin Owns You All!')

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strenght):
        self.health = health
        self.strenght = strenght

    def super().receiveDamage(self, damage):
        self.health -= damage
        if health <= 0:
            print('A Saxon has died in combat')
        else:
            print('A Saxon has received',damage,'points of damage')   

# War


class War:
    pass
