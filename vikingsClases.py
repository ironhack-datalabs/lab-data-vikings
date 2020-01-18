
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
        
    #def attack(self):
     #   super().attack()
    
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0: 
            return "".join([self.name," has received ",str(damage)," points of damage"])
        else:
            return "".join([self.name," has died in act of combat"])
    
    def battleCry(self):
        return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0: 
            return "".join(["A Saxon has received ",str(damage)," points of damage"])
        else:
            return "A Saxon has died in combat"

    pass

# War

import random

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        vikingAttacker = random.choice(self.vikingArmy)
        dmg = vikingAttacker.attack()
        saxonVictim = random.choice(self.saxonArmy)
        saxonVictim.receiveDamage(dmg)
        
        #victimIndex = random.randint(0,sum(len(self.vikingArmy),-1))
        #result = self.saxonArmy[victimIndex].receiveDamage(dmg)
        #if result == "A Saxon has died in combat":
            #saxonArmy.remove(saxonArmy[victimIndex])
        #return result
        pass
    def saxonAttack(self):
        pass
    def showStatus(self):
        pass
    pass
