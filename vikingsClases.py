import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health = self.health - damage
        result = ""
        if self.health > 0:
            result = self.name + " has received " + \
                str(damage) + " points of damage"
        else:
            result = self.name + " has died in act of combat"
        return result

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health = self.health - damage
        result = ""
        if self.health > 0:
            result = "A Saxon has received " + \
                str(damage) + " points of damage"
        else:
            result = "A Saxon has died in combat"
        return result


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking1):
        self.vikingArmy.append(viking1)

    def addSaxon(self, saxon1):
        self.saxonArmy.append(saxon1)

    def vikingAttack(self):
        saxon1 = random.choice(self.saxonArmy)
        viking1 = random.choice(self.vikingArmy)
        result = saxon1.receiveDamage(viking1.strength)
        #    self.saxonArmy.remove[saxon1]
        if saxon1.health <= 0:
            for i, o in enumerate(self.saxonArmy):
                if o.strength == saxon1.strength and o.health == saxon1.health:
                    del self.saxonArmy[i]
                    break
        return result

    def saxonAttack(self):
        saxon1 = random.choice(self.saxonArmy)
        viking1 = random.choice(self.vikingArmy)
        result = viking1.receiveDamage(saxon1.strength)
        if viking1.health <= 0:
            for i, o in enumerate(self.vikingArmy):
                if o.strength == viking1.strength and o.health == viking1.health:
                    del self.vikingArmy[i]
                    break
        #    self.vikingArmy.remove[viking1]
        return result

    def showStatus(self):
        result = ""
        if len(self.vikingArmy) == 0:
            result = "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            result = "Vikings have won the war of the century!"
        else:
            result = "Vikings and Saxons are still in the thick of battle."
        return result
