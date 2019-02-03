# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        health = self.health - damage


# Viking
class Viking(Soldier):
    def _init_(self, name, health, strength):
        #super()._init_(self, health, strength)
        Person._init_(self, health, strength)
        self.name = name

    def attack(self):
        return Person.attack()

    def receiveDamage(self, damage):
        health = self.health - damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        # return self.strength
        return super().attack()

    def receiveDamage(self, damage):
        health = self.health - damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

