# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health=self.health-damage 
     
'''
attack() method

    should be a function
    should receive 0 arguments
    should return the strength property of the Soldier

receiveDamage() method

    should be a function
    should receive 1 argument (the damage)
    should remove the received damage from the health property
    shouldn't return anything

 '''
# Viking


class Viking:
    def __init__(self,name,strength,health):
        self.name = 'Harald'
        self.strength = strength
        self.health = health
    pass

'''
inheritance

    Viking should inherit from Soldier

constructor function

    should receive 3 arguments (name, health & strength)
    should receive the name property as its 1st argument
    should receive the health property as its 2nd argument
    should receive the strength property as its 3rd argument

attack() method

(This method should be inherited from Soldier, no need to reimplement it.)

    should be a function
    should receive 0 arguments
    should return the strength property of the Viking

receiveDamage() method

(This method needs to be reimplemented for Viking because the Viking version needs to have different return values.)

    should be a function
    should receive 1 argument (the damage)
    should remove the received damage from the health property
    if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
    if the Viking dies, it should return "NAME has died in act of combat"

battleCry() method

Learn more about battle cries.

    should be a function
    should receive 0 arguments
    should return "Odin Owns You All!"

'''


# Saxon


class Saxon:
    def __init__(self,strength,health):
        self.strength = strength
        self.health = health

    pass

# War


class War:
    def __init__(self,war):
        self.war = war
        
    pass