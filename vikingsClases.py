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
        if(self.health > 0):
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
            return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength): 
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if(self.health > 0):
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
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.vikingArmy)
        damage = randomSaxon.receiveDamage(randomViking.strength)
        if randomSaxon.health <= 0:
            self.saxonArmy.remove(randomSaxon)
        return damage

    def saxonAttack(self):
        import random
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.vikingArmy)
        damage = randomViking.receiveDamage(randomSaxon.strength)
        if randomViking.health <= 0:
            self.vikingArmy.remove(randomViking)
        return damage

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."