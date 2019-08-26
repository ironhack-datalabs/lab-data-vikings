
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage=0):
        # This will probably need to be changed in the future due to over complicating the function
        if self.health > 0:
            if (self.health - damage) <= 0:
                self.health = 0
            else:
                self.health -= damage
        else:
            0


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage=0):
        if (self.health - damage) <= 0:
            self.health = 0
            return self.name + " has died in act of combat"
        else:
            self.health -= damage
            return self.name + " has received " + str(damage) + " points of damage"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage=0):
        if (self.health - damage) <= 0:
            self.health = 0
            return "A Saxon has died in combat"
        else:
            self.health -= damage
            return "A Saxon has received " + str(damage) + " points of damage"


# War

class War:
    pass
