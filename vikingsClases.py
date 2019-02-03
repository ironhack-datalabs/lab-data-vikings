
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
        super().__init__(self, health, strength)
        self.name = name

    def attack(self):
        super().attack(self)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            alive_msg = (
                "{} has received {} points of damage".format(self.name, damage))
            return alive_msg
        elif self.health == 0:
            dead_msg = ("{} has died in act of combat".format(self.name))
            return dead_msg

    def battleCry():
        return ("Odin Owns You All!")


# Saxon


class Saxon:
    pass

# War


class War:
    pass
