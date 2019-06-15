# Soldier
import random

class Soldier():
	def __init__(self, health, strength):
		self.health = health
		self.strength = strength


	def attack(self):
		return self.strength



	def receiveDamage(self, damage):
		#if self.health < 0:
			self.health = self.health-damage


  

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
    	super(Viking, self).__init__(health, strength)
    	self.name = name
    	
    def receiveDamage(self, damage):
    	self.health = self.health-damage
    	if self.health > 0:
    		return "{} has received {} points of damage".format(self.name, damage)
    	else:
    		return "{} has died in act of combat".format(self.name)


    def battleCry(self):
    	return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health-damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War


class War():
    def __init__(self):
        self.vikingArmy=[]

        self.saxonArmy=[]
 
    def addViking(self, Viking):
        self.Viking = Viking
        self.vikingArmy.append(Viking)        


    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        self.saxonArmy.append(Saxon)        
        


    def vikingAttack(self):        
        s = random.choice(self.saxonArmy) 
        v = random.choice(self.vikingArmy)
        vik_attack = s.receiveDamage(v.attack())
        if s.health <= 0:

            self.saxonArmy.remove(s)

        return vik_attack

    def saxonAttack(self):
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        sax_attack = v.receiveDamage(s.attack())
        if v.health <= 0:

            self.vikingArmy.remove(v)

        return sax_attack


    def showStatus(self):
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) >=1 & len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."