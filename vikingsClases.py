
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health=self.health-damage

# Viking

class Viking:
    def __init__(name, self,health,strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health=self.health - damage
        if self.health > 0:
            return ("{} has received {} points of damage".format(self.name,damage))
        else:
            return ("{} has died in act of combat".format(self.name))

# Saxon


class Saxon:
    pass

# War


class War:
    pass
