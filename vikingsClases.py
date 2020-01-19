
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
        self.name = name
        super().__init__(health, strength)

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        print('HOLA K ASE vikingo dañado ', self.health)
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        print('HOLA K ASE saxon dañado ', self.health)
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
        print('Se va a crear un Viking: ', len(self.vikingArmy))
        self.vikingArmy.append(Viking)
        print('Creado un Viking: ', len(self.vikingArmy))

    def addSaxon(self, Saxon):
        print('Se va a crear un Saxon: ', len(self.saxonArmy))
        self.saxonArmy.append(Saxon)
        print('Creado un Saxon: ', len(self.saxonArmy))

    def vikingAttack(self):
        import random
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.saxonArmy)
        randomSaxon.receiveDamage(randomViking.strength)

        if randomSaxon.health <= 0:
            print('Se va a eliminar saxon', randomSaxon.health)
            print('Longitud saxonArmy antes: ', len(self.saxonArmy))
            self.saxonArmy.remove(randomSaxon)
            print('ELIMINADO saxon')
            print('Longitud saxonArmy después: ', len(self.saxonArmy))

    def saxonAttack(self):
        import random
        randomViking = random.choice(self.vikingArmy)
        randomSaxon = random.choice(self.saxonArmy)
        randomViking.receiveDamage(randomSaxon.strength)

        if randomViking.health <= 0:
            print('Se va a eliminar al vikingo', randomViking.health)
            print('Longitud vikingArmy antes: ', len(self.vikingArmy))
            self.vikingArmy.remove(randomViking)
            print('Vikingo eliminado')
            print('Longitud vikingArmy después: ', len(self.vikingArmy))

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
