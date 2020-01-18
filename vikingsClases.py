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
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else: 
            return self.name + " has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else: 
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        ranS = random.choice(self.saxonArmy)
        ranV = random.choice(self.vikingArmy)
        fight = ranS.receiveDamage(ranV.strength)
        if ranS.health <= 0:
            self.saxonArmy.remove(ranS)
        return fight
     
    def saxonAttack(self):
        import random
        ranS = random.choice(self.saxonArmy)
        ranV = random.choice(self.vikingArmy)
        fight = ranV.receiveDamage(ranS.strength)
        if ranV.health <= 0:
            self.vikingArmy.remove(ranV)
        return fight

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."