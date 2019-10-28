
import random
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
        self.name = name
        super().__init__(health, strength)

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
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        elif self.health <= 0:
            return "A Saxon has died in combat"

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
        attacked_saxon = random.choice(self.saxonArmy)
        attacker_viking = random.choice(self.vikingArmy)

        x = attacked_saxon.receiveDamage(attacker_viking.attack())

        if attacked_saxon.health <= 0:
            self.saxonArmy.remove(attacked_saxon)
        return x
    
    def saxonAttack(self):
        attacked_viking = random.choice(self.vikingArmy)
        attacker_saxon = random.choice(self.saxonArmy)

        y = attacked_viking.receiveDamage(attacker_saxon.attack())

        if attacked_viking.health <= 0:
            self.vikingArmy.remove(attacked_viking)
        return y
    
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"

        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        
        elif (len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0):
            return "Vikings and Saxons are still in the thick of battle."
