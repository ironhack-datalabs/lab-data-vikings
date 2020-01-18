
# Soldier


class Soldier:
    def __init__(self, health, strength):

        self.health = health

        self.strength = strength

    def attack(self):

        return self.strength

    def receiveDamage(self, damage):

        ouch = self.health - damage

        self.health = ouch



# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):

        super().__init__(health, strength)

        self.name = name

    def attack(self):

        return self.strength

    def receiveDamage(self, damage):

        self.health -= damage

        if self.health > 0:
            return "%s has received %s points of damage" % (self.name, damage)

        else:
            return "%s has died in act of combat" % (self.name)

    def battleCry(self):

        return "Odin Owns You All!"

   
# Saxon

class Saxon(Soldier):

    def __init__(self,health,strength):

        super().__init__(health, strength)
        

    def attack(self):
        
        return self.strength
    

    def receiveDamage(self,damage):
        
        super().receiveDamage(damage)

        if self.health > 0:

            return "A Saxon has received %s points of damage" %(damage)

        else:

            return "A Saxon has died in combat"

            

# War