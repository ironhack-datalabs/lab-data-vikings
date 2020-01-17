import random as rd

# Soldier
class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
         self.health -= damage

    def __repr__(self):
        return f"[SOLDIER] health: {self.health}, strength: {self.strength}"

# Viking
class Viking(Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        super().attack()
        return f"{self.name} has received {damage} points of damage" \
            if int(self.health) > 0 else f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

    def __repr__(self):
        return f"[VIKING] name: {self.name}, health: {0 if self.health <= 0 else self.health}, strength: {self.strength}"


# Saxon
class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        super().attack()
        return f"A Saxon has received {damage} points of damage" if self.health > 0 else f"A Saxon has died in combat"

    def __repr__(self):
        return f"[SAXON] health: {self.health}, strength: {self.strength}"

# War
class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def randomSoldier(self, army):
        return rd.randint(0, len(army)) - 1

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking = self.vikingArmy[self.randomSoldier(self.vikingArmy)]
        saxon = self.saxonArmy[self.randomSoldier(self.saxonArmy)]
        resultado = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return resultado

    def saxonAttack(self):
        viking = self.vikingArmy[self.randomSoldier(self.vikingArmy)]
        saxon = self.saxonArmy[self.randomSoldier(self.saxonArmy)]
        resultado = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return resultado

    def showStatus(self):
        return "Vikings have won the war of the century!" if len(self.saxonArmy) == 0 \
            else "Saxons have fought for their lives and survive another day..." \
            if len(self.vikingArmy) == 0 else "Vikings and Saxons are still in the thick of battle."

    def __repr__(self):
        return f"vikingArmy: {len(self.vikingArmy)} \nsaxonArmy: {len(self.saxonArmy)}"

"""
#Creo que esto es una Batalla muy simple

war = War()
war.addSaxon(Saxon(5, 5))
war.addViking(Viking("Messi", 6, 6))
print(war.saxonAttack())
print(war)
print(war.showStatus())
"""
