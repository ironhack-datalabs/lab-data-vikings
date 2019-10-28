
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
            return (self.name + " has received " + str(damage) + " points of damage")
        else:
            return (self.name + " has died in act of combat")
    
    def battleCry(self):
        return ("Odin Owns You All!")

# Saxon

class Saxon(Soldier):

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return ("A Saxon has received " + str(damage) + " points of damage")
        else:
            return ("A Saxon has died in combat")

# War

import random
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        SaxonPeleon = random.choice(self.saxonArmy)
        VikingoPeleon = random.choice(self.vikingArmy)
        # result = Saxon.receiveDamage(SaxonPeleon, Viking.attack(VikingoPeleon)) # solución poco ortodoxa: self se refiere a si mismo.
        result = SaxonPeleon.receiveDamage(VikingoPeleon.attack())
        if SaxonPeleon.health <= 0:
            self.saxonArmy.remove(SaxonPeleon)
        return result

    def saxonAttack(self):
        SaxonPeleon = random.choice(self.saxonArmy)
        VikingoPeleon = random.choice(self.vikingArmy)
        # result = Viking.receiveDamage(VikingoPeleon, Saxon.attack(SaxonPeleon))
        result = VikingoPeleon.receiveDamage(SaxonPeleon.attack())
        if VikingoPeleon.health <= 0:
            self.vikingArmy.remove(VikingoPeleon)
        return result

    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            return ("Vikings have won the war of the century!")
        if len(self.vikingArmy) <= 0:
            return ("Saxons have fought for their lives and survive another day...")
        else:
            return ("Vikings and Saxons are still in the thick of battle.")
