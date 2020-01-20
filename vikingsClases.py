
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.damage=damage
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        super().__init__(health, strength)

    def __init__attack(Soldier):
        return self.strength

    def receiveDamage(self, damage):
        self.damage=damage
        self.health=-(damage)
        if self.health>0:
            return ((str(self.name) + " has received " ((str(self.damage)) + "points of damage")
        else:
            return ((str(self.name) + " has died in act of combat")
    
    def battleCry(self):
        return ("Odin Owns You All!")



# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def __init__atack(Soldier):
        return self.strength

    def receiveDamage(self, damage):
        self.damage=damage
        self.health-=(damage)
        if self.health>0:
            return ("A Saxon has received "((str(self.damage) + "points of damage")
        else:
            return ("A Saxon has died in combat")


# War


class War:
    
