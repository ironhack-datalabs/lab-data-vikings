
print("hello")


# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health 
        self.strength=strength

    def attack(self):
        return self.strength # propiedad de la clase por lo tanto hay que ponerle self.
    
    def receiveDamage(self,damage):
        self.health -= damage 


# Viking


class Viking (Soldier): #Since inherits from Soldier you need to use Soldier as property
    def __init__(self, name, health, strenght):
        super().__init__(health,strenght) # no hace falta referirlo otra vez a soldier otro método sería solder.__init__()
        self.name= name #llamar a super y poner entre paréntesis las propiedades de Soldier que quieras utilizar

    def receiveDamage(self,damage):
        self.health -= damage # estos dos damages vikings y soldiers no están relacionados
        if self.health>0:
            return "{} has received {} points of damage".format(self.name, damage)
        elif self.health<= 0:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strenght):
        super().__init__(health, strenght)
        
    def receiveDamage (self, damage):
        self.health -= damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        elif self.health<= 0:
            return "A Saxon has died in combat"



# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self,Viking): #Viking es un objeto
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        saxon= random.choice(self.saxonArmy) 
        viking= random.choice(self.vikingArmy)

        y=saxon.receiveDamage(viking.attack())

        if saxon.health<=0:
            self.saxonArmy.remove(saxon)
        return y
        
    def saxonAttack(self):
        saxon= random.choice(self.saxonArmy) 
        viking= random.choice(self.vikingArmy)

        x=viking.receiveDamage(saxon.attack())

        if viking.health<=0:
            self.vikingArmy.remove(viking)
        return x
        
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

        

            

