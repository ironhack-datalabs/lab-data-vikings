
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

    def __init__(self, name, health, strength):

        super().__init__(health, strength)

        self.name = name

    def attack(self):

        return self.strength

    def receiveDamage(self, damage):

        self.health -= damage

        return ("%s has received %s points of damage" % (self.name, damage) if self.health > 0 else "%s has died in act of combat" % (self.name))

    

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

        return ("A Saxon has received %s points of damage" %(damage) if self.health > 0 else "A Saxon has died in combat")



# War