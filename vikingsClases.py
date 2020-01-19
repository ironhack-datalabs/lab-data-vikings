
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
    def __init__(self,name,health,strength):
        self.name = name
        super().__init__(health,strength)
        print(name,health,strength)

    def attack(self):
        return super().attack()
        

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
        




# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
        print(health,strength)
    
    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"

  

# War


class War:
    def __init__(self):
       self.vikingArmy = []
       self.saxonArmy  = []
    
    def addViking(self,viking):
        self.vikingArmy.append(viking)
        pass

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        pass
    
    def vikingAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)
        result = s.receiveDamage(v.attack())
        if s.health <= 0:
           self.saxonArmy.remove(s)
        return result
        
    
    def saxonAttack(self):
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)
        result = v.receiveDamage(s.attack())
        if v.health <= 0:
            self.vikingArmy.remove(v)
        return result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."
        else:
            return("Another bloody round starts")


#Batalla



war = War()
saxonNumber = int(input("The Saxons army is composed by these number of soldiers:"))

for s in range(0,saxonNumber):
  saxon = Saxon(random.randint(0,100), random.randint(0,100))
  war.addSaxon(saxon)

vikingNumber = int(input("The Vikings army is composed by these number of soldiers:"))

for v in range(0, vikingNumber):
  viking = Viking("Viking " + str(v), random.randint(0,100), random.randint(0,100))
  war.addViking(viking)


while len(war.saxonArmy) != 0 and len(war.vikingArmy) != 0 :
  try:
    print(war.saxonAttack())
    print(war.vikingAttack())
  except:
    print(war.showStatus())
  else:
    print(war.showStatus())


