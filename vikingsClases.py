import random
# Soldier


class Soldier:
    def __init__(self, health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health = self.health - damage

    
# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        Soldier.__init__(self, health, strength)
        self.name = name
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        Soldier.__init__(self, health, strength)

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"
        

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy= []
    
    def addViking(self,vik):
        if isinstance(vik,Viking):
            self.vikingArmy.append(vik)
    
    def addSaxon(self,sax):
        if isinstance(sax,Saxon):
            self.saxonArmy.append(sax)

    def vikingAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        indiceSax = self.saxonArmy.index(sax)
        retorno = sax.receiveDamage(vik.attack())
        if sax.health<1:
            self.saxonArmy.remove(sax)
        else:
            self.saxonArmy[indiceSax] = sax
        return retorno

    def saxonAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        indiceVik = self.vikingArmy.index(vik)
        retorno = vik.receiveDamage(sax.attack())
        if vik.health<1:
            self.vikingArmy.remove(vik)
        else:
            self.vikingArmy[indiceVik] = vik
        return retorno

    def showStatus(self):
        if len(self.saxonArmy)>0 and len(self.vikingArmy)>0:
            return 'Vikings and Saxons are still in the thick of battle.'
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        

