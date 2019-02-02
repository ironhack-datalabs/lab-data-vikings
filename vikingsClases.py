
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    
    def receiveDamage(damage):`
        self.health = self.health - damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):`
        self.health = self.health - damage
        if self.health > 0: 
            return "{} has received {} points of damage".format(self.name, self.damage)
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
    
    def receiveDamage(self, damage):`
        self.health = self.health - damage
        if self.health > 0: 
            return "A Saxon has received {} points of damage".format(self.damage)
            
        else:
            return "A Saxon has died in combat"
       


# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        saxonArmy.append(Saxon)   

    def vikingAttack(self):
        attacked_sax = random.choice(saxonArmy).receiveDamage(random.choice(VikinArmy.strength))
        return 
        attacker_vik = random.choice(VikinArmy)
        attack_result = attacked_sax.receiveDamage(attacker_vik.strength)
        if attacked_sax.health =< 0:
            saxonArmy.remove(attacked_sax)
        return attack_result
'''
A `Saxon` (chosen at random) has their `receiveDamage()` method called with the damage equal to the `strength` of a `Viking` 
(also chosen at random). 
This should only perform a single attack and the `Saxon` doesn't get to attack back.

- should be a function
- should receive **0 arguments**
- should make a `Saxon` `receiveDamage()` equal to the `strength` of a `Viking`
- should remove dead saxons from the army
- should return **result of calling `receiveDamage()` of a `Saxon`** with the `strength` of a `Viking`
'''



