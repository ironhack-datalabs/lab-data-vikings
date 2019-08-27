from random import randrange
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage
        
# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength):
        self.name=name
        self.health=health
        self.strength=strength
        Soldier.__init__(self,self.health,self.strength)
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        if damage>=self.health:
            #self.health=0
            self.health=self.health-damage
            return (self.name + " has died in act of combat")
        else:
            self.health=self.health-damage
            return (self.name + " has received "+str(damage)+" points of damage")
     
    def battleCry(self):
        return ("Odin Owns You All!")


# Saxon
class Saxon(Soldier):
    def __init__(self,health, strength):
        self.health=health
        self.strength=strength
        Soldier.__init__(self,self.health,self.strength)
    
    def receiveDamage(self,damage):
        if damage>=self.health:
            #self.health=0
            self.health=self.health-damage
            return ("A Saxon has died in combat")

        else:
            self.health=self.health-damage
            return ("A Saxon has received "+ str(damage) +" points of damage")
 

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        if (len(self.vikingArmy)>0 and len(self.saxonArmy)>0):
            chosensaxon=randrange(len(self.saxonArmy))
            print("chosen saxon: " + str(chosensaxon))
            chosenviking=randrange(len(self.vikingArmy))
            print("chosen viking: " + str(chosenviking))
           
            if self.vikingArmy[chosenviking].attack() >= self.saxonArmy[chosensaxon].health:
                self.saxonArmy[chosensaxon].receiveDamage(self.vikingArmy[chosenviking].attack())
                self.saxonArmy.remove(self.saxonArmy[chosensaxon])
                return ("A Saxon has died in combat")
            else:
                self.saxonArmy[chosensaxon].receiveDamage(self.vikingArmy[chosenviking].attack())
                return ("A Saxon has received "+ str(self.vikingArmy[chosenviking].attack()) +" points of damage")
                
    def saxonAttack(self):
        if (len(self.vikingArmy)>0 and len(self.saxonArmy)>0):
            chosensaxon=randrange(len(self.saxonArmy))
            print("chosen saxon: " + str(chosensaxon))
            chosenviking=randrange(len(self.vikingArmy))
            print("chosen viking: " + str(chosenviking))
            if (self.saxonArmy[chosensaxon].attack()>=self.vikingArmy[chosenviking].health):
                self.vikingArmy[chosenviking].receiveDamage(self.saxonArmy[chosensaxon].attack())
                self.vikingArmy.remove(self.vikingArmy[chosenviking])
                return (self.vikingArmy[chosenviking].name  + " has died in act of combat")
            else:
                self.vikingArmy[chosenviking].receiveDamage(self.saxonArmy[chosensaxon].attack())
                return (self.vikingArmy[chosenviking].name + " has received "+str(self.saxonArmy[chosensaxon].attack())+" points of damage")

    def showStatus(self):
        if(len(self.saxonArmy)==0):
            return "Vikings have won the war of the century!"
        elif(len(self.vikingArmy)==0):
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."