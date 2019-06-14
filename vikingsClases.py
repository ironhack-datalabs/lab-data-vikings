# Soldier


class Soldier:
    def __init__(self, health, strength):

        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name


class Viking (Soldier):

    def __init__(self, name, health, strength):

        super(Viking, self).__init__(health, strength)

        self.name = name

    def receiveDamage(self, damage):

        self.damage = damage

        self.health -= damage

        if self.health > 0:

            return "{} has received {} points of damage".format(self.name, damage)

        else:

            return "{} has died in act of combat".format(self.name)

    def battleCry(self):

        return "Viva la virgen de la Macarena"


class Saxon(Soldier):
    def __init__(self, receiveDamage, health, strength):
        super(Saxon, self).__init__(health, strength)
        self.receiveDamage



    pass


class War:
    pass
