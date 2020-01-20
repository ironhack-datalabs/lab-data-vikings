
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
        result = saxonVictim.receiveDamage(dmg)
        if saxonVictim.health <= 0:
            self.saxonArmy.remove(saxonVictim)
        return result
        
        #victimIndex = random.randint(0,sum(len(self.vikingArmy),-1))
        #result = self.saxonArmy[victimIndex].receiveDamage(dmg)
        #if result == "A Saxon has died in combat":
            #saxonArmy.remove(saxonArmy[victimIndex])
        #return result
        pass
    def saxonAttack(self):
        saxonAttacker = random.choice(self.saxonArmy)
        dmg = saxonAttacker.attack()
        vikingVictim = random.choice(self.vikingArmy)
        result = vikingVictim.receiveDamage(dmg)
        if vikingVictim.health <= 0:
            self.vikingArmy.remove(vikingVictim)
        return result

        pass
    def showStatus(self):
        if self.saxonArmy == []: return "Vikings have won the war of the century!"
        elif self.vikingArmy == []: return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
    
