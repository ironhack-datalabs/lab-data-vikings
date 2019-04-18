
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return '{} has received {} points of damage'.format(self.name, damage)
        else:
            return '{} has died in act of combat'.format(self.name)

    def battleCry(self):
        return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return 'A Saxon has received {} points of damage'.format(damage)
        else:
            return 'A Saxon has died in combat'

    

# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random
        i_v = random.randint(0,len(self.vikingArmy)-1)
        i_s = random.randint(0,len(self.saxonArmy)-1)
        self.saxonArmy[i_s].health = self.saxonArmy[i_s].health - self.vikingArmy[i_v].attack

    def saxonAttack(self):
        pass

    def showStatus(self):
        pass
