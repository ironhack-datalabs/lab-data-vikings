from random import randint
# Soldier


class Soldier():
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health-=damage


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        super(Viking,self).__init__(health,strength)
        self.name=name
    def receiveDamage(self,damage):
        super(Viking,self).receiveDamage(damage)
        if self.health>0:
            return self.name + " has received "+ str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
  

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super(Saxon,self).__init__(health,strength)
    def receiveDamage(self,damage):
        super(Saxon,self).receiveDamage(damage)
        if self.health>0:
            return "A Saxon has received "+ str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
# War


class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        s = self.saxonArmy[randint(0,len(self.saxonArmy)-1)]
        v = self.vikingArmy[randint(0,len(self.vikingArmy)-1)]
        str = s.receiveDamage(v.attack())
        if "died" in str:
            self.saxonArmy.remove(s)
        return str
    def saxonAttack(self):
        s = self.saxonArmy[randint(0,len(self.saxonArmy)-1)]
        v = self.vikingArmy[randint(0,len(self.vikingArmy)-1)]
        str = v.receiveDamage(s.attack())
        if "died" in str:
            self.vikingArmy.remove(v)
        return str
    def showStatus(self):
        if not len(self.saxonArmy):
            return "Vikings have won the war of the century!"
        elif not len(self.vikingArmy):
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


        
    
