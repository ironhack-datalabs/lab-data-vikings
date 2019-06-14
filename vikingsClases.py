
# Soldier


class Soldier ():
    def _init_(self, health, strenght):
        self.health = health
        self.strenght = strenght

    def _attack(self):
        return (self.strenght)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health - damage


'''
# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass


'''
