
# Soldier


import random


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
        self.health = self.health-damage
        if self.health > 0:
            return (str(self.name)+' has received '+str(damage)+' points of damage')
        else:
            return (str(self.name)+' has died in act of combat')

    def battleCry(self):
        return 'Odin Owns You All!'
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0:
            return ('A Saxon has received '+str(damage)+' points of damage')
        else:
            return 'A Saxon has died in combat'


# War


class War(Soldier):
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        ran_sax = random.choice(self.saxonArmy)
        ran_vik = random.choice(self.vikingArmy)
        vik_att = ran_vik.attack()
        dam_sax = ran_sax.receiveDamage(vik_att)
        if 0 >= ran_sax.health:
            self.saxonArmy.remove(ran_sax)
        return dam_sax

    def saxonAttack(self):
        ran_sax = random.choice(self.saxonArmy)
        ran_vik = random.choice(self.vikingArmy)
        san_att = ran_sax.attack()
        dam_vik = ran_vik.receiveDamage(san_att)
        if 0 >= ran_vik.health:
            self.vikingArmy.remove(ran_vik)
        return dam_vik

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
