# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength

        
       
        '''
attack() method

    should be a function
    should receive 0 arguments
    should return the strength property of the Soldier '''

''' receiveDamage() method

    should be a function
    should receive 1 argument (the damage)
    should remove the received damage from the health property
    shouldn't return anything

        '''

    pass



# Viking


class Viking:
    def __init__(self,name,strength,health):
        self.name = 'Harald'
        self.strength = strength
        self.health = health
    pass

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