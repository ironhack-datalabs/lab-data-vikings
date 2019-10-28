
# Soldier
class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking
class Viking (Soldier):
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name


    def receiveDamage (self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return ("{} has received {} points of damage".format(self.name, damage))
        else:
            return ("{} has died in act of combat".format(self.name))
        
    def battleCry (self):
        return ("Odin Owns You All!")


# Saxon
class Saxon (Soldier):
    def receiveDamage (self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return ("A Saxon has received {} points of damage".format(damage))
        else:
            return ("A Saxon has died in combat")


# War
import random
class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking (self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon (self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack (self):
        rd_Saxon = random.choice(self.saxonArmy)
        rd_Viking = random.choice(self.vikingArmy)
        v_attack = rd_Saxon.receiveDamage(rd_Viking.attack())
        if rd_Saxon.health <= 0:
            self.saxonArmy.remove (rd_Saxon)
        return v_attack
        
    def saxonAttack (self):
        rd_Saxon = random.choice(self.saxonArmy)
        rd_Viking = random.choice(self.vikingArmy)
        s_attack = rd_Viking.receiveDamage(rd_Saxon.attack())
        if rd_Viking.health <= 0:
            self.vikingArmy.remove (rd_Viking)
        return s_attack

    def showStatus (self):
        if self.saxonArmy == []:
            return ("Vikings have won the war of the century!")
        elif self.vikingArmy == []:
            return ("Saxons have fought for their lives and survive another day...")
        else:
            return ("Vikings and Saxons are still in the thick of battle.")


