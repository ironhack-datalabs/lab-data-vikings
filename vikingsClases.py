
# Soldier
import random


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(Viking, self).__init__(health, strength)
        self.name = name
        self.health = health

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        super(Viking, self).receiveDamage(damage)
        if self.health > 0:
            return "{} has received {} points of damage" .format(self.name, self.damage)
        elif self.health <= 0:
            return "{} has died in act of combat" .format(self.name)

    def battleCry(self):
        return "Odin Owns You All!"

    # Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super(Saxon, self).__init__(health, strength)
# attack lo hereda de soldados. Definimos health y strength en el super porque si que son valores que tenemos que editar

    def receiveDamage(self, damage):
        self.health -= damage
        self.damage = damage
        if self.health > 0:
            return "A Saxon has received {} points of damage" .format(self.damage)
        elif self.health <= 0:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking1):
        self.vikingArmy.append(Viking1)

    def addSaxon(self, Saxon1):
        self.saxonArmy.append(Saxon1)

    def vikingAttack(self):
        srandom = random.choice(self.saxonArmy)
        vrandom = random.choice(self.vikingArmy)
        vattack = srandom.receiveDamage(vrandom.attack())
        if srandom.health <= 0:
            self.saxonArmy.remove(srandom)
        return vattack


"""
# `saxonAttack()` method

The `Saxon` version of `vikingAttack()`. A `Viking` receives the damage equal to the 
`strength` of a `Saxon`.

- should be a function
- should receive **0 arguments**
- should make a `Viking` `receiveDamage()` equal to the `strength` of a `Saxon`
- should remove dead vikings from the army
- should return **result of calling `receiveDamage()` of a `Viking`** with the 
`strength` of a `Saxon`


# `vikingAttack()` method

A `Saxon` (chosen at random) has their `receiveDamage()` 
method called with the damage equal to the `strength` 
of a `Viking` (also chosen at random). 
This should only perform a single attack and the `Saxon` doesn't get to attack back.

- should be a function
- should receive **0 arguments**
- should make a `Saxon` `receiveDamage()` equal to the `strength` of a `Viking`
- should remove dead saxons from the army
- should return **result of calling `receiveDamage()` of a `Saxon`** with the `strength` of a `Viking`
# (BONUS) War

Modify the `War` constructor and add 5 methods to its prototype:

- `addViking()`
- `addSaxon()`
- `vikingAttack()`
- `saxonAttack()`
- `showStatus()`

# constructor function

When we first create a `War`, the armies should be empty. We will add soldiers to the armies later.

- should receive **0 arguments**
- should assign an empty array to the **`vikingArmy` property**
- should assign an empty array to the **`saxonArmy` property**

# `addViking()` method

Adds 1 `Viking` to the `vikingArmy`. If you want a 10 `Viking` army, you need to call this 10 times.

- should be a function
- should receive **1 argument** (a `Viking` object)
- should add the received `Viking` to the army
- **shouldn't return** anything

# `addSaxon()` method

The `Saxon` version of `addViking()`.

- should be a function
- should receive **1 argument** (a `Saxon` object)
- should add the received `Saxon` to the army
- **shouldn't return** anything

# `vikingAttack()` method

A `Saxon` (chosen at random) has their `receiveDamage()` method called with the damage equal to the `strength` 
of a `Viking` (also chosen at random). This should only perform a single attack and the `Saxon` doesn't get to attack back.

- should be a function
- should receive **0 arguments**
- should make a `Saxon` `receiveDamage()` equal to the `strength` of a `Viking`
- should remove dead saxons from the army
- should return **result of calling `receiveDamage()` of a `Saxon`** with the `strength` of a `Viking`

# `saxonAttack()` method

The `Saxon` version of `vikingAttack()`. A `Viking` receives the damage equal to the `strength` of a `Saxon`.

- should be a function
- should receive **0 arguments**
- should make a `Viking` `receiveDamage()` equal to the `strength` of a `Saxon`
- should remove dead vikings from the army
- should return **result of calling `receiveDamage()` of a `Viking`** with the `strength` of a `Saxon`

# `showStatus()` method

Returns the current status of the `War` based on the size of the armies.

- should be a function
- should receive **0 arguments**
- **if the `Saxon` array is empty**, should return _**"Vikings have won the war of the century!"**_
- **if the `Viking` array is empty**, should return _**"Saxons have fought for their lives and survive another day..."**_
- **if there are at least 1 `Viking` and 1 `Saxon`**, should return _**"Vikings and Saxons are still in the thick of battle."**_

# Deliverables

- REQUIRED: `vikingsClases.py` modified with your solution to the challenge question.

# Resources

- https://docs.python.org/3/library/unittest.html
- https://www.python-course.eu/python3_inheritance.php

# Additional Challenge for the Nerds

You can try to make your own tests for your code by creating another test file.

"""
