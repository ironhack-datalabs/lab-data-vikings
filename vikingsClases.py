
import random

# Soldier


class Soldier():
    def __init__(self, health, strength):
       self.health = health #valor de la variable
       self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength) #Por corrección de Felipe cojo
                                            #los args del padre que se repiten

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        return "{} has died in act of combat".format(self.name)


    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    #def __init__(self, health, strength):

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        return "A Saxon has died in combat"


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
        vikingo = random.choice(self.vikingArmy)
        sajon = random.choice(self.saxonArmy)
        ataqueVikingo = vikingo.attack()
        daño = sajon.receiveDamage(ataqueVikingo)
        if sajon.health <= 0:
            self.saxonArmy.remove(sajon)
        return daño


    def saxonAttack(self):
        vikingo = random.choice(self.vikingArmy)
        sajon = random.choice(self.saxonArmy)
        ataqueSajon = sajon.attack()
        daño = vikingo.receiveDamage(ataqueSajon)
        if vikingo.health <= 0:
            self.vikingArmy.remove(vikingo)
        return daño

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
    

