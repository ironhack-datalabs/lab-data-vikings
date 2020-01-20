
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

        return self.strength

    def receiveDamage(self, damage):

        self.health -= damage

        return ("%s has received %s points of damage" % (self.name, damage) if self.health > 0 else "%s has died in act of combat" % (self.name))

    def battleCry(self):

        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):

    def __init__(self, health, strength):

        super().__init__(health, strength)

    def attack(self):

        return self.strength

    def receiveDamage(self, damage):

        super().receiveDamage(damage)

        return ("A Saxon has received %s points of damage" % (damage) if self.health > 0 else "A Saxon has died in combat")


# War


class War:

    def __init__(self):

        self.vikingArmy = []

        self.saxonArmy = []

    def addViking(self, Viking):

        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):

        self.saxonArmy.append(Saxon)

    def saxonAttack(self):

        Vikingo = self.vikingArmy[random.randint(0, len(self.vikingArmy)-1)]

        Sajon = self.saxonArmy[random.randint(0, len(self.saxonArmy)-1)]

        Battle = Vikingo.receiveDamage(Sajon.attack())

        if Vikingo.health <= 0:

            self.vikingArmy.remove(Vikingo)

        return Battle

    def vikingAttack(self):

        Vikingo = self.vikingArmy[random.randint(0, len(self.vikingArmy)-1)]

        Sajon = self.saxonArmy[random.randint(0, len(self.saxonArmy)-1)]

        Battle = Sajon.receiveDamage(Vikingo.attack())

        if Sajon.health <= 0:

            self.saxonArmy.remove(Sajon)

            

        return Battle

    def showStatus(self):

        if self.saxonArmy == []:

            return "Vikings have won the war of the century!"

        elif self.vikingArmy == []:

            return "Saxons have fought for their lives and survive another day..."

        else:
            return "Vikings and Saxons are still in the thick of battle."


def Viking_generator():

    name_viking = "".join([chr(random.randint(97, 122)) for e in range(5)])

    health_viking = random.randint(0, 900)

    strength_viking = random.randint(0, 450)

    Viking_generated = Viking(name_viking, health_viking, strength_viking)

    return Viking_generated


def Saxon_generator():

    health_saxon = random.randint(0, 900)

    strength_saxon = random.randint(0, 450)

    Saxon_generated = Saxon(health_saxon, strength_saxon)

    return Saxon_generated


def battle(size):

    IronWar = War()

    for e in range(size):

        IronWar.addViking(Viking_generator())

    for e in range(size):

        IronWar.addSaxon(Saxon_generator())

    while IronWar.vikingArmy and IronWar.saxonArmy:

        print(IronWar.saxonAttack())

        if IronWar.vikingArmy and IronWar.saxonArmy:

            print(IronWar.vikingAttack())

    print(IronWar.showStatus())


print(battle(6))

