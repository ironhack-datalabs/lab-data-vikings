
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return (self.strength)

    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def attack(self):
        super().attack()
        return (self.strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return ("Odin Owns You All!")

# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        super().attack()
        return (self.strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return ("A Saxon has died in combat")

# War


class War():

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.Viking = Viking
        if len(self.vikingArmy) < 10:
            self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        if len(self.saxonArmy) < 10:
            self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        viking_attack = random.choice(self.vikingArmy)
        strength_viking = viking_attack.attack()
        saxon_attack = random.choice(self.saxonArmy)
        saxon_attacked = saxon_attack.receiveDamage(strength_viking)
        if saxon_attacked == "A Saxon has died in combat":
            self.saxonArmy.remove(saxon_attack)
        return saxon_attacked

    def saxonAttack(self):
        import random
        saxon_attack = random.choice(self.saxonArmy)
        strength_saxon = saxon_attack.attack()
        viking_attack = random.choice(self.vikingArmy)
        viking_attacked = viking_attack.receiveDamage(strength_saxon)
        if viking_attack.health <= 0:
            self.vikingArmy.remove(viking_attack)
        return viking_attacked

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
