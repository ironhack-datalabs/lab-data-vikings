import random
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0: 
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0: 
            return "A Saxon has received {} points of damage".format(damage)
            
        else:
            return "A Saxon has died in combat"
       


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)   

    def vikingAttack(self):
        attacked_sax = random.choice(self.saxonArmy)
        attacker_vik = random.choice(self.vikingArmy)
        vik_attack_result = attacked_sax.receiveDamage(attacker_vik.strength)
        if attacked_sax.health <= 0:
            self.saxonArmy.remove(attacked_sax)
        return vik_attack_result

    def saxonAttack(self):
        attacked_vik = random.choice(self.vikingArmy)
        attacker_sax = random.choice(self.saxonArmy)
        sax_attack_result = attacked_vik.receiveDamage(attacker_sax.strength)
        if attacked_vik.health <= 0:
            self.vikingArmy.remove(attacked_vik)
        return sax_attack_result
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy ) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1  and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

'''
Returns the current status of the `War` based on the size of the armies.

- should be a function
- should receive **0 arguments**
- **if the `Saxon` array is empty**, should return _**"Vikings have won the war of the century!"**_
- **if the `Viking` array is empty**, should return _**"Saxons have fought for their lives and survive another day..."**_
- **if there are at least 1 `Viking` and 1 `Saxon`**, should return _**"Vikings and Saxons are still in the thick of battle."**_
'''


