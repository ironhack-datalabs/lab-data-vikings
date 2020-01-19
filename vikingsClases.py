import random

# Soldier
#Modify the Soldier constructor function and add 2 methods to its prototype: attack(), and receiveDamage().
class Soldier:
    
    #should receive 2 arguments (health & strength)
    #should receive the health property as its 1st argument
    #should receive the strength property as its 2nd argument
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack (self):
        #should be a function
        #should receive 0 arguments
        #should return the strength property of the Soldier
        return self.strength
 
    def receiveDamage (self,damage):
        #should be a function
        #should receive 1 argument (the damage)
        #should remove the received damage from the health property
        #shouldn't return anything
        
        new_health = self.health - damage
        self.health = new_health
    
    
    
# Viking
#A Viking is a Soldier with an additional property, their name. 
#They also have a different receiveDamage() method and new method, battleCry().

#Viking should inherit from Soldier
class Viking(Soldier):
    
    #should receive 3 arguments (name, health & strength)
    def __init__ (self,name,health,strength):
        self.name = name
        super().__init__(health,strength)
    
    #Attack() method should be inherited from Soldier, no need to reimplement it.
    
    def receiveDamage (self,damage):
    #This method needs to be reimplemented for Viking because the Viking version needs to have different return values.

    #should be a function
    #should receive 1 argument (the damage)
    #should remove the received damage from the health property
    #if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
    #if the Viking dies, it should return "NAME has died in act of combat"
        
        self.health -= damage
        mensaje = ""
        if self.health > 0:
            mensaje = str(self.name)+" has received "+str(damage)+" points of damage"
        else:
            mensaje = str(self.name)+" has died in act of combat"
        return mensaje
    
    def battleCry (self):
    #should be a function
    #should receive 0 arguments
    #should return "Odin Owns You All!"
        
        frase = "Odin Owns You All!"
        return frase

    
    
    
# Saxon


class Saxon(Soldier):
    
    def __init__ (self,health,strength):
        super().__init__(health,strength)
    
    def receiveDamage (self, damage):
        self.health -= damage
        string = ""
        if self.health > 0:
            string = "A Saxon has received "+str(damage)+" points of damage"
        else:
            string = "A Saxon has died in combat"
        return string


# War


class War:
    
    def __init__ (self):
        
        #should receive 0 arguments
        #should assign an empty array to the vikingArmy property
        #should assign an empty array to the saxonArmy property
        
        self.vikingArmy = []
        self.saxonArmy = []
        
        
    def addViking (self, Viking):
        #Adds 1 Viking to the vikingArmy. If you want a 10 Viking army, you need to call this 10 times.

        #should be a function
        #should receive 1 argument (a Viking object)
        #should add the received Viking to the army
        #shouldn't return anything
            
        self.vikingArmy.append(Viking)
        
        
    def addSaxon (self, Saxon):

        #should be a function
        #should receive 1 argument (a Saxon object)
        #should add the received Saxon to the army
        #shouldn't return anything
        
        self.saxonArmy.append(Saxon)
        
        
    def vikingAttack (self):
        #A Saxon (chosen at random) has their receiveDamage() method called with the damage 
        #equal to the strength of a Viking (also chosen at random). 
        #This should only perform a single attack and the Saxon doesn't get to attack back.

        #should be a function
        #should receive 0 arguments
        #should make a Saxon receiveDamage() equal to the strength of a Viking
        #should remove dead saxons from the army
        #should return result of calling receiveDamage() of a Saxon with the strength of a Viking

        
        vik = random.randint(0,len(self.vikingArmy) - 1)
        sax = random.randint(0,len(self.saxonArmy) - 1)
        
        vik_attack = self.saxonArmy[sax].receiveDamage(self.vikingArmy[vik].attack())
        
        self.saxonArmy = [n for n in self.saxonArmy if n.health > 0]
        
        return vik_attack
    
    
    def saxonAttack (self):
        
        #The Saxon version of vikingAttack(). A Viking receives the damage equal to the strength of a Saxon.

        #should be a function
        #should receive 0 arguments
        #should make a Viking receiveDamage() equal to the strength of a Saxon
        #should remove dead vikings from the army
        #should return result of calling receiveDamage() of a Viking with the strength of a Saxon
        
        #vik = random.choice(self.vikingArmy)
        #sax = random.choice(self.saxonArmy)
        
        vik = random.randint(0,len(self.vikingArmy) - 1)
        sax = random.randint(0,len(self.saxonArmy) - 1)
        
        sax_attack = self.vikingArmy[vik].receiveDamage(self.saxonArmy[sax].attack())
        
        self.vikingArmy = [n for n in self.vikingArmy if n.health > 0]
        
        return sax_attack
    
    
    def showStatus (self):
        
        #Returns the current status of the War based on the size of the armies.

        #should be a function
        #should receive 0 arguments
        #if the Saxon array is empty, should return "Vikings have won the war of the century!"
        #if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
        #if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
        
        status = ""
        
        if len(self.saxonArmy) == 0:
            status = "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            status = "Saxons have fought for their lives and survive another day..."
        else:
            status = "Vikings and Saxons are still in the thick of battle."
            
        return status
    










