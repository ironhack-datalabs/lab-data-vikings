import random
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
        super(Viking, self).__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        super(Viking, self).receiveDamage(damage)
        if self.health > 0:
            return(f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def receiveDamage(self, damage):
        super(Saxon, self).receiveDamage(damage)
        if self.health > 0:
            return(f"A Saxon has received {damage} points of damage")
        else:
            return(f"A Saxon has died in combat")

# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        v = random.choice(range(len(self.vikingArmy)))
        s = random.choice(range(len(self.saxonArmy)))
        resultado = self.saxonArmy[s].receiveDamage(
            self.vikingArmy[v].attack())
        if self.saxonArmy[s].health <= 0:
            self.saxonArmy.pop(s)
        return resultado

    def saxonAttack(self):
        v = random.choice(range(len(self.vikingArmy)))
        s = random.choice(range(len(self.saxonArmy)))
        resultado = self.vikingArmy[v].receiveDamage(
            self.saxonArmy[s].attack())
        if self.vikingArmy[v].health <= 0:
            self.vikingArmy.pop(v)
        return resultado

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."

# like a boss
