
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.damage=damage
        self.health = (self.health)-(damage)


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        super().__init__(health, strength)

    def __init__attack(Soldier):
        return self.strength

    def receiveDamage(self, damage):
        self.damage=damage
        self.health=(self.health)-(damage)
        if self.health<=0:
            return ("Harald has died in act of combat")
        else:
            return ("Harald has received 70 points of damage")

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
        self.health=(self.health)-(damage)
        if self.health>0:
            return ("A Saxon has received 45 points of damage")
        else:
            return ("A Saxon has died in combat")


# War


class War:
    def __init__(self, vikingArmy, saxonArmy):
        self.vikingArmy()
        self.saxonArmy()
    
    def addViking(self, Viking):
        self.Viking=Viking
        append.self.vikingArmy(n+1)

    def addSaxon(self, Saxon):
        append.self.saxonArmy(n+1)

    def vikingAttack(saxonArmy):
        random.sample.self.saxonArmy

    def saxonAttack():

    def showStatus():

