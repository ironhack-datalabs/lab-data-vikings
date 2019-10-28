# Soldier


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


'''
Saxon

A Saxon is a weaker kind of Soldier. Unlike a Viking, a Saxon has no name. Their receiveDamage() method will also be different than the original Soldier version.

Modify the Saxon, constructor function, have it inherit from Soldier and reimplement the receiveDamage() method for Saxon.
inheritance

    Saxon should inherit from Soldier

constructor function

    should receive 2 arguments (health & strength)
    should receive the health property as its 1st argument
    should receive the strength property as its 2nd argument

attack() method

(This method should be inherited from Soldier, no need to reimplement it.)

    should be a function
    should receive 0 arguments
    should return the strength property of the Saxon

receiveDamage() method

(This method needs to be reimplemented for Saxon because the Saxon version needs to have different return values.)

    should be a function
    should receive 1 argument (the damage)
    should remove the received damage from the health property
    if the Saxon is still alive, it should return "A Saxon has received DAMAGE points of damage"
    if the Saxon dies, it should return "A Saxon has died in combat"



'''


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


class War:
    def __init__(self,war):
        self.war = war
        vikingArmy=[]
        saxonArmy=[]

    def addViking(self):
        vikingArmy.append(Viking)
    
    def addSaxon(self):
        saxonArmy.append(Saxon)

    def vikingAttack(self):
        saxonArmy[]
        Saxon.receiveDamage(Saxon,damage)

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