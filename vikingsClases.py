import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health 
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    #Aquí si hacemos init porque los parámetros de entrada cambian al poner name
    def __init__(self, name, health, strength):
        #Soldier.__init__(self,health,strength)
        super().__init__(health,strength)
        self.name = name

    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    #No hace falta hacer el init porque lo hereda directamente
    #def __init__(self, health, strength):
        #super().__init__(health,strength)
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        fight = saxon.receiveDamage(viking.attack())

        #[self.saxonArmy.remove(sax) for sax in self.saxonArmy if sax.health <= 0]
        # Se puede hacer de las dos formas, pero en el list comprehension recorres toda la lista
        #  y en el if solo quitas al soldado elegido en el momento
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return fight

    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        fight = viking.receiveDamage(saxon.attack())
        [self.vikingArmy.remove(vik) for vik in self.vikingArmy if vik.health <= 0]
        return fight

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
