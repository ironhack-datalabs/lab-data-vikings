import unittest
from vikingsClases import *
from inspect import signature


class MyTest(unittest.TestCase):

    def testViking(self):
        name = 'Harald'
        strength = 150
        health = 300
        viking = Viking(name, strength, health)
        # should inherit from Soldier
        self.assertEqual(len(signature(Viking).parameters), 3)
        self.assertEqual(viking.name, name)
        self.assertEqual(viking.health, health)
        self.assertEqual(viking.strength, strength)
        self.assertEqual(callable(viking.attack), True)
        self.assertEqual(len(signature(viking.attack).parameters), 0)
        self.assertEqual(viking.attack(), strength)
        self.assertEqual(callable(viking.receiveDamage), True)
        self.assertEqual(len(signature(viking.receiveDamage).parameters), 1)
        viking.receiveDamage(50)
        self.assertEqual(viking.health, health - 50)
        self.assertEqual(viking.receiveDamage(50), name +
                         ' has received 50 points of damage')
        self.assertEqual(viking.receiveDamage(70), name +
                         ' has received 70 points of damage')
        self.assertEqual(viking.receiveDamage(health),
                         name + ' has died in act of combat')
        self.assertEqual(callable(viking.battleCry), True)
        self.assertEqual(viking.battleCry(), 'Odin Owns You All!')

    def testSaxon(self):
        health = 60
        strength = 25

        saxon = Saxon(health, strength)
        # should inherit from Soldier
        self.assertEqual(len(signature(Saxon).parameters), 2)
        self.assertEqual(saxon.health, health)
        self.assertEqual(saxon.strength, strength)
        self.assertEqual(callable(saxon.attack), True)
        self.assertEqual(len(signature(saxon.attack).parameters), 0)
        self.assertEqual(saxon.attack(), strength)
        self.assertEqual(callable(saxon.receiveDamage), True)
        self.assertEqual(len(signature(saxon.receiveDamage).parameters), 1)
        saxon.receiveDamage(1)
        self.assertEqual(saxon.health, health - 1)
        self.assertEqual(saxon.receiveDamage(
            45), 'A Saxon has received 45 points of damage')
        self.assertEqual(saxon.receiveDamage(
            10), 'A Saxon has received 10 points of damage')
        self.assertEqual(saxon.receiveDamage(health),
                         'A Saxon has died in combat')

    def testWar(self):
        def generateViking():
            name = 'Harald'
            strength = 150
            health = 300
            return Viking(name, health, strength)

        def generateSaxon():
            healt = 60
            strength = 25

            return Saxon(healt, strength)

        viking = generateViking()
        saxon = generateSaxon()
        war = War()

        self.assertEqual(len(signature(War).parameters), 0)
        self.assertEqual(war.vikingArmy, [])
        self.assertEqual(war.saxonArmy, [])
        self.assertEqual(callable(war.addViking), True)
        self.assertEqual(len(signature(war.addViking).parameters), 1)
        war.addViking(viking)
        self.assertEqual(war.vikingArmy, [viking])
        self.assertEqual(war.addViking(viking), None)
        self.assertEqual(callable(war.addSaxon), True)
        self.assertEqual(len(signature(war.addSaxon).parameters), 1)
        self.assertEqual(war.saxonArmy, [])
        self.assertEqual(war.addSaxon(saxon), None)

        war.addViking(viking)
        war.addSaxon(saxon)

        self.assertEqual(callable(war.vikingAttack), True)
        self.assertEqual(len(signature(war.vikingAttack).parameters), 0)

        oldHealt = saxon.health
        war.vikingAttack()
        self.assertEqual(saxon.health, oldHealt - viking.strength)

        war.vikingAttack()
        self.assertEqual(len(war.saxonArmy), 0)
        war.addSaxon(saxon)
        self.assertEqual(war.vikingAttack(), 'A Saxon has died in combat')
        self.assertEqual(callable(war.saxonAttack), True)
        self.assertEqual(len(signature(war.saxonAttack).parameters), 0)

        oldHealt = viking.health
        war.addViking(viking)
        war.addSaxon(saxon)
        war.saxonAttack()
        self.assertEqual(viking.health, oldHealt - saxon.strength)

        for i in range(8):
            war.saxonAttack()
        self.assertEqual(len(war.vikingArmy), 0)

        viking = generateViking()
        war.addViking(viking)
        war.addSaxon(saxon)
        self.assertEqual(war.saxonAttack(), viking.name +
                         ' has received ' + str(saxon.strength) + ' points of damage')

        self.assertEqual(callable(war.showStatus), True)
        self.assertEqual(len(signature(war.showStatus).parameters), 0)
        for i in range(2):
            war.vikingAttack()
        self.assertEqual(war.showStatus(),
                         'Vikings have won the war of the century!')

        viking = generateViking()
        war.addViking(viking)
        war.addSaxon(saxon)
        for i in range(11):
            war.saxonAttack()
        self.assertEqual(war.showStatus(
        ), 'Saxons have fought for their lives and survive another day...')
        war.addViking(viking)
        self.assertEqual(
            war.showStatus(), 'Vikings and Saxons are still in the thick of battle.')


if __name__ == '__main__':
    unittest.main()
