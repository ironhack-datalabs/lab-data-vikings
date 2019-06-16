
# Soldier


class Soldier():
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health=self.health-damage
# Viking


class Viking(Soldier):
    #def __init__(self, name, health, strength):
        #self.name=name
        #self.health=health
        #self.strength=strength
    def __init__(self,name,health,strength):
        super(Viking, self).__init__(health,strength)
        self.name=name
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super(Saxon, self).__init__(health,strength)
    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War

from random import shuffle
class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        # elegir saxon al azar
        # elegir al azar un vikingo
        sa=self.saxonArmy[randint(0,len(self.saxonArmy)-1)
        va=self.vikingArmy[randint(0,len(self.vikingArmy)-1)
        string= sa.receiveDamage(va.attack())
        if "died" in string:
            self.saxonArmy.remove(sa)
        return string
    def saxonAttack(self):
        sa=self.saxonArmy[randint(0,len(self.saxonArmy)-1)
        va=self.vikingArmy[randint(0,len(self.vikingArmy)-1)
        string= va.receiveDamage(sa.attack())
        if "died" in string:
            self.vikingArmy.remove(va)
        return string

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            "Vikings and Saxons are still in the thick of battle."
