
# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.strength = strength
        self.health = health
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return 'Viking {} has received {} points of damage'.format(self.name, damage)
        else:
            return 'Viking {} has died in act of combat'.format(self.name)
    def battleCry(self):
        cry = random.choice(range(4))
        if cry == 0:
            return 'Odin hates you all'
        elif cry == 1:
            return 'We will die killing'
        elif cry == 2:
            return 'Winter is comming for you all'
        elif cry == 3:
            return 'OMG!'


# Saxon


class Saxon(Viking):
    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return 'Saxon {} has received {} points of damage'.format(self.name, damage)
        else:
            return 'Saxon {} has died in combat'.format(self.name)
# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self,viking):
        self.vikingArmy.append(viking)
        print('Viking ', viking.name, 'has joined the army')
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        print('Saxon ', saxon.name, 'has joined the army')
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        print(viking.name, 'attacks ', saxon.name)
        saxon_damage = saxon.receiveDamage(viking.attack())
        self.saxonArmy = [s for s in self.saxonArmy if s.health > 0]
        return saxon_damage
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        print(saxon.name, 'attacks ', viking.name)
        viking_damage = viking.receiveDamage(saxon.attack())
        self.vikingArmy = [v for v in self.vikingArmy if v.health > 0]
        return viking_damage
    
    def showStatus(self):
        random_army = random.choice([self.vikingArmy, self.saxonArmy])
        if len(random_army) != 0:
            random_soldier = random.choice(random_army)
            print(random_soldier.name, ': ',random_soldier.battleCry())
        if not len(self.saxonArmy):
            return 'Vikings have won the war of the century!'
        elif not len(self.vikingArmy):
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'

    def showSurvivors(self):
        print('\nThe survivors are :')
        if len(self.saxonArmy):
            print(*[s.name for s in self.saxonArmy])
        elif len(self.vikingArmy):
            print(*[v.name for v in self.vikingArmy])
