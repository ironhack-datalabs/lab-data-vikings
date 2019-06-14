
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = health - damage


"""


#### `attack()` method

- should be a function
- should receive **0 arguments**
- should return **the `strength` property of the `Soldier`**

#### `receiveDamage()` method

- should be a function
- should receive **1 argument** (the damage)
- should remove the received damage from the `health` property
- **shouldn't return** anything
# Viking
"""


class Viking:
    pass

# Saxon


class Saxon:
    pass

# War


class War:
    pass
