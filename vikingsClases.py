import random
# Soldier


class Soldier:

    def __init__(self, health=0 , strength=0):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health-=damage

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health=0 , strength=0):
        Soldier.__init__(self, health, strength)
        self.name=name
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return self.name+" has received "+str(damage)+" points of damage"
        else:
            return self.name+" has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health>0:
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War:
    
    def __init__(self):
        self.vikingArmy=list()
        self.saxonArmy=list()

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        saxon_num=random.randint(0,len(self.saxonArmy)-1)
        result=self.saxonArmy[saxon_num].receiveDamage(self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)].strength)
        if self.saxonArmy[saxon_num].health<=0:
            self.saxonArmy.pop(saxon_num)
        return result
    
    def saxonAttack(self):
        viking_num=random.randint(0,len(self.vikingArmy)-1)
        result=self.vikingArmy[viking_num].receiveDamage(self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)].strength)
        if self.vikingArmy[viking_num].health<=0:
            self.vikingArmy.pop(viking_num)
        return result

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
             return "Saxons have fought for their lives and survive another day..."
        else: return "Vikings and Saxons are still in the thick of battle."
    

