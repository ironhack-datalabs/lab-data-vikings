# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health == 0:
            return "{} has died in act of combat".format(self.name)

        else:
            return "{} has received {} points of damage".format(self.name, damage)

    def battleCry(self):
        return "Odin Owns You All!"

    pass


# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health == 0:
            return "A Saxon has died in combat"

        else:
            return "A Saxon has received {} points of damage".format(damage)

    pass


# War


class War:
    pass
