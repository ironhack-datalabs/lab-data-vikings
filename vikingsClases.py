
# Soldier


class Soldier:
    def __init__(self,health,strength):
     self.health = health
     self.strength = strength

    def attack(self): 
        return self.strength
        
    def receiveDamage(self,damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name = name

    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health >0:
            return ("{} has received {} points of damage" .format(self.name, damage))
        else:
            return ("{} has died in act of combat".format(self.name))
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health >0:
            return ("A Saxon has received {} points of damage" .format(damage))
        else:
            return ("A Saxon has died in combat")
# Wars
import random
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self,Viking):
        self.vikingArmy.append(Viking) 
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)  
    def vikingAttack(self):
        vik1 = random.choice(self.vikingArmy)
        sax1 = random.choice(self.saxonArmy)
        solution = sax1.receiveDamage(vik1.strength)
        if sax1.health <= 0:
            self.saxonArmy.remove(sax1)
        return solution
    def saxonAttack(self):
        vik2 = random.choice(self.vikingArmy)
        sax2 = random.choice(self.saxonArmy)
        solution = vik2.receiveDamage(sax2.strength)
        if vik2.health <= 0:
            self.vikingArmy.remove(vik2)
        return solution
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)!=0 and len(self.vikingArmy) != 0:
              return "Vikings and Saxons are still in the thick of battle."
