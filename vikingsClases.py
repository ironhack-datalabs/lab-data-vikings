
# Soldier


class Soldier(object):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

    pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return str(self.name) + ' has died in act of combat'
        else:
            return str(self.name) + ' has received ' + str(damage) + ' points of damage'

    def battleCry(self):
        return "Odin Owns You All!"

    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
