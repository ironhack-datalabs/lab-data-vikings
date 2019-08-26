
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = 0
        self.strength = 0

    def attack():
        return self.strength

    def receiveDamage(damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = 'VikingName'
        Soldier.__init__(self, health, strength)

    def receiveDamage(damage)
      self.health -= damage
       if self.health > 0:
            print('{} has received {} points of damage'.format(self.name, damage))
        elif self.health <= 0:
            print('{} has died in act of combat'.format(self.name))

    def battleCry():




    # Saxon


class Saxon:
    pass

# War


class War:
    pass
