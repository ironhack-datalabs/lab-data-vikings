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

        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
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

        cuernos = random.randint(0, len(self.vikingArmy)-1)
        espada = random.randint(0, len(self.saxonArmy)-1)

        cuernos_attack = self.saxonArmy[espada].receiveDamage(
            self.vikingArmy[cuernos].attack())
        for cuernos_attack in saxonArmy:
            if self.health(saxon) <= 0:
                self.saxonArmy.remove(espada)
        return cuernos_attack


'''
    def saxonAttack(self):

    def showStatus(self):
        if vikingArmy == []:
            return "Vikings have won the war of the century!"
        elif saxonArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

 # return {"receiveDamage(Saxon)": int(random.random()+100), "strength(Viking)": int(random.random()*100)}
        # for i in vikingArmy:
         #   if receiveDamage(Saxon) <= 0:
          #      self.vikingArmy.pop(i)
'''
