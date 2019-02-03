import random

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
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            alive_msg = (
                ("{} has received {} points of damage").format(self.name, damage))
            return alive_msg

        elif self.health <= 0:
            dead_msg = (("{} has died in act of combat").format(self.name))
            return dead_msg

    def battleCry(self):
        return ("Odin Owns You All!")


# Saxon

class Saxon(Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            alive_msg = (
                ("A Saxon has received {} points of damage").format(damage))
            return alive_msg

        elif self.health <= 0:
            dead_msg = ("A Saxon has died in combat")
            return dead_msg


# War

class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def vikingAttack(self):
        rnd_saxon = random.choice(self.saxonArmy)
        rnd_viking = random.choice(self.vikingArmy)
        rtn_vik = rnd_saxon.receiveDamage(rnd_viking.strength)
        if rnd_saxon.health <= 0:
            self.saxonArmy.remove(rnd_saxon)
        return rtn_vik

    def saxonAttack(self):
        rnd_saxon = random.choice(self.saxonArmy)
        rnd_viking = random.choice(self.vikingArmy)
        rtn_sax = rnd_viking.receiveDamage(rnd_saxon.strength)
        if rnd_viking.health <= 0:
            self.vikingArmy.remove(rnd_viking)
        return rtn_sax

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return ("Saxons have fought for their lives and survive another day...")
        elif len(self.saxonArmy) == 0:
            return ("Vikings have won the war of the century!")
        elif ((len(self.vikingArmy) > 0) and (len(self.saxonArmy) > 0)):
            return ("Vikings and Saxons are still in the thick of battle.")


# The Undead

class Undead(Soldier):

    def __init__(self, health=5000, strength=2000, anger=1):
        self.health = health
        self.strength = strength
        self.anger = anger

    def attack(self):
        return (super().attack()*self.anger)

    def receiveDamage(self, damage):
        self.health += damage
        if self.health > 0:
            alive_msg = (
                ("The Undead has recovered {} points of damage.").format(damage))
            self.anger += damage
            return alive_msg

        elif self.health <= 0:
            dead_msg = ("The Undead cannot die in combat YOU FOOL.")
            return dead_msg

    def frenzy(self):
        self.strength += random.randint(1, 100)
        return ("The Ragnarok of the undead will put the Valkyries down!")

# The last night: Apocalypse


class Apocalypse:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        self.undeadArmy = []
        self.undead = Undead()

    def addViking(self, vik):
        self.vikingArmy.append(vik)

    def addSaxon(self, sax):
        self.saxonArmy.append(sax)

    def addUndead(self, und):
        self.undeadArmy.append(und)

    def vikingAttack(self):
        rnd_saxon = random.choice(self.saxonArmy)
        rnd_viking = random.choice(self.vikingArmy)
        rtn_vik = rnd_saxon.receiveDamage(rnd_viking.strength)
        if rnd_saxon.health <= 0:
            self.saxonArmy.remove(rnd_saxon)
            self.addUndead(self.undead)
        return rtn_vik

    def saxonAttack(self):
        rnd_saxon = random.choice(self.saxonArmy)
        rnd_viking = random.choice(self.vikingArmy)
        rtn_sax = rnd_viking.receiveDamage(rnd_saxon.strength)
        if rnd_viking.health <= 0:
            self.vikingArmy.remove(rnd_viking)
            self.addUndead(self.undead)
        return rtn_sax

    def undeadAttack(self):
        rnd_saxon = random.choice(self.saxonArmy)
        rnd_viking = random.choice(self.vikingArmy)
        rnd_undead = random.choice(self.undeadArmy)
        rtn_sax = rnd_saxon.receiveDamage(rnd_undead.strength)
        rtn_vik = rnd_viking.receiveDamage(rnd_undead.strength)
        if rnd_viking.health <= 0:
            self.vikingArmy.remove(rnd_viking)
            self.addUndead(self.undead)
            rnd_undead.frenzy()
        if rnd_saxon.health <= 0:
            self.saxonArmy.remove(rnd_saxon)
            self.addUndead(self.undead)
            rnd_undead.frenzy()
        return (rtn_sax + " " + "and" + " " + rtn_vik)

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return ("Vikings now live in Valhalla. The Earth belongs to the Undead.")
        elif len(self.saxonArmy) == 0:
            return ("Saxons now belong to the army of the Undead.")
        elif ((len(self.vikingArmy) > 0) and (len(self.saxonArmy) > 0)):
            return ("Vikings and Saxons are still growing the Undead Army.")
