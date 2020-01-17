import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage
# Viking


class Viking(Soldier):
    def __init__(self,name, health, strength):
        self.name = name
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return self.name+" has received "+str(damage)+" points of damage"
        else :
            return self.name+" has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in combat"
# War   
class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        viking_attack = random.choice(self.vikingArmy)
        strength_viking = viking_attack.attack()
        saxon_atacado = random.choice(self.saxonArmy)
        saxon_atacado2 = saxon_atacado.receiveDamage(strength_viking)
        if saxon_atacado2 == "A Saxon has died in combat" :
            self.saxonArmy.remove(saxon_atacado)
        return saxon_atacado2
    def saxonAttack(self):
        saxon_attack = random.choice(self.saxonArmy)
        strength_saxon = saxon_attack.attack()
        viking_atacado = random.choice(self.vikingArmy)
        viking_atacado2 = viking_atacado.receiveDamage(strength_saxon)
        if "has died in act of combat"  in viking_atacado2 :
            self.vikingArmy.remove(viking_atacado)
        return viking_atacado2
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
