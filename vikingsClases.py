
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage


# Viking


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
