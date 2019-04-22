# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking
class Viking (Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        elif self.health == 0:
            return "{} has died in act of combat".format(self.name, damage)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        elif self.health <= 0:
            return "A Saxon has died in combat"

# War

class War:
    def __init__(self,):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        a = random.choice(self.saxonArmy)
        b = random.choice(self.vikingArmy)
        result = a.receiveDamage(b.strength)
        if a.health <= 0:
            self.saxonArmy.pop()
        return result

    def saxonAttack(self):
        import random
        a = random.choice(self.vikingArmy)
        b = random.choice(self.saxonArmy)
        result = a.receiveDamage(b.strength)
        if a.health <= 0:
            self.vikingArmy.pop()
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."