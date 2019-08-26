
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
    
    
    def attack(self):
        return self.strength


    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        elif self.health <= 0:
            return "{} has died in act of combat".format(self.name)
        

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)


    def attack(self):
        return self.strength


    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        elif self.health <= 0:
            return "A Saxon has died in combat"
        



# War


class War:
    def __init__(self):
        Soldier.__init__(self, health, strength)
        self.vikingArmy = []
        self.saxonArmy = []


# War métodos

    def addViking(self, Viking):
        for i in range(1, Viking):
            self.vikingArmyl.append(i)

    def addSaxon(self, Saxon):
        for i in range(1, Saxon):
            self.saxonArmy.append(i)

    def vikingAttack(self,):
        pass
    def saxonAttack(self,):
        pass
    def showStatus(self,):
        pass