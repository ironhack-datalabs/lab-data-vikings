# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage 
        
class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name=name
        self.health=health
        self.strength=strength

    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return "{} has received {} points of damage".format(self.name,damage)
        else:
            return "{} has died in act of combat".format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"




# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength

    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"
    pass

# War


class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(viking):
        sxn=random.choice(saxonArmy)
        vkg=random.choice(vikingArmy)
        receiveDamage(sxn,Damage=vkg.strngth)
        if sxn.health<0:
            saxonArmy.remove(sxn)
        return receiveDamage(sxn,Damage=vkg.strngth)
    
    def saxonAttack(viking):
        vkg=random.choice(vikingArmy)
        sxn=random.choice(saxonArmy)
        if vkg.health<0:
            vikingArmy.remove(vkg)
        return receiveDamage(vkg,Damage=sxn.strngth)
    
    def showStatus(war):
        if saxonArmy==[]:
            return "Saxons have fought for their lives and survive another day..."
        elif vikingArmy==[]:
            return "Vikings and Saxons are still in the thick of battle."
        else:
            return "Vikings and Saxons are still in the thick of battle.."


    '''
#### `vikingAttack()` method

A `Saxon` (chosen at random) has their `receiveDamage()` method called with the damage equal to the `strength` of a `Viking` (also chosen at random). 
This should only perform a single attack and the `Saxon` doesn't get to attack back.

- should be a function
- should receive **0 arguments**
- should make a `Saxon` `receiveDamage()` equal to the `strength` of a `Viking`
- should remove dead saxons from the army
- should return **result of calling `receiveDamage()` of a `Saxon`** with the `strength` of a `Viking`

#### `saxonAttack()` method

The `Saxon` version of `vikingAttack()`. A `Viking` receives the damage equal to the `strength` of a `Saxon`.

- should be a function
- should receive **0 arguments**
- should make a `Viking` `receiveDamage()` equal to the `strength` of a `Saxon`
- should remove dead vikings from the army
- should return **result of calling `receiveDamage()` of a `Viking`** with the `strength` of a `Saxon`
    '''



    pass