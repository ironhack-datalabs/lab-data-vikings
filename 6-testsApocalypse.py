import unittest
from vikingsClases import Apocalypse
from vikingsClases import Viking
from vikingsClases import Saxon
from vikingsClases import Undead
from inspect import signature


class TestApocalypse(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.apocal = Apocalypse()

    def testWarShouldReciveNoParams(self):
        self.assertEqual(len(signature(Apocalypse).parameters), 0)

    def testVikingArmy(self):
        self.assertEqual(self.apocal.vikingArmy, [])

    def testSaxonArmy(self):
        self.assertEqual(self.apocal.saxonArmy, [])

    def testUndeadArmy(self):
        self.assertEqual(self.apocal.undeadArmy, [])


class TestWar2(unittest.TestCase):

    @classmethod
    def setUp(cls):
        def generateViking():
            cls.name = 'Harald'
            cls.strength = 150
            cls.health = 300
            return Viking(cls.name, cls.health, cls.strength)

        def generateSaxon():
            cls.health = 60
            cls.strength = 25
            return Saxon(cls.health, cls.strength)

        def generateUndead():
            cls.health = 5000
            cls.strength = 2000
            cls.anger = 1
            return Undead(cls.health, cls.strength, cls.anger)

        cls.viking = generateViking()
        cls.saxon = generateSaxon()
        cls.undead = generateUndead()
        cls.apocal = Apocalypse()
        cls.apocal.addSaxon(cls.saxon)
        cls.apocal.addViking(cls.viking)
        cls.apocal.addUndead(cls.undead)

    def testAddViking(self):
        self.assertEqual(callable(self.apocal.addViking), True)

    def testAddVikingShouldReceiveOneParam(self):
        self.assertEqual(len(signature(self.apocal.addViking).parameters), 1)

    def testAddVikingInList(self):
        self.assertEqual(self.apocal.vikingArmy, [self.viking])

    def testAddVikingReturnNull(self):
        self.assertEqual(self.apocal.addViking(self.viking), None)

    def testAddSaxonShouldBeFunction(self):
        self.assertEqual(callable(self.apocal.addSaxon), True)

    def testAddSaxonReceiveOneParam(self):
        self.assertEqual(len(signature(self.apocal.addSaxon).parameters), 1)

    def testSaxonArmyReturnEmptyList(self):
        self.assertEqual(self.apocal.saxonArmy, [self.saxon])

    def testAddSaxonReturnNone(self):
        self.assertEqual(self.apocal.addSaxon(self.saxon), None)

    def testAddUndeadIsAFunction(self):
        self.assertEqual(callable(self.apocal.addUndead), True)

    def testAddUndeadOnlyOneParam(self):
        self.assertEqual(len(signature(self.apocal.addUndead).parameters), 1)

    def testUndeadArmyEmptyList(self):
        self.assertEqual(self.apocal.undeadArmy, [self.undead])

    def testAddUndeadReturnNone(self):
        self.assertEqual(self.apocal.addUndead(self.undead), None)

    def testVikingAttackIsFunction(self):
        self.assertEqual(callable(self.apocal.vikingAttack), True)

    def testVikingAttackReceiveNoParam(self):
        self.assertEqual(
            len(signature(self.apocal.vikingAttack).parameters), 0)

    def testSaxonHealth(self):
        oldHealt = self.saxon.health
        self.apocal.vikingAttack()
        self.assertEqual(self.saxon.health, oldHealt - self.viking.strength)

    def testVikingAttack(self):
        self.apocal.vikingAttack()
        self.assertEqual(len(self.apocal.saxonArmy), 0)

    def testRaiseUndeadVikingAttack(self):
        self.apocal.vikingAttack()
        self.assertEqual(len(self.apocal.undeadArmy), 2)

    def testAddSaxon(self):
        print(self.apocal.__dict__)
        self.assertEqual(self.apocal.vikingAttack(),
                         'A Saxon has died in combat')

    def testSaxonAttackIsFunction(self):
        self.assertEqual(callable(self.apocal.saxonAttack), True)

    def testSaxonAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.apocal.saxonAttack).parameters), 0)

    def testVikingHealth(self):
        oldHealt = self.viking.health
        self.apocal.saxonAttack()
        self.assertEqual(self.viking.health, oldHealt - self.saxon.strength)

    def testVikingArmyList(self):
        for i in range(12):
            if(len(self.apocal.vikingArmy) == 0):
                break
            self.apocal.saxonAttack()
        self.assertEqual(len(self.apocal.vikingArmy), 0)

    def testUndeadArmyList(self):
        for i in range(12):
            if(len(self.apocal.vikingArmy) == 0):
                break
            self.apocal.saxonAttack()
        self.assertEqual(len(self.apocal.undeadArmy), 2)

    def testReturnOfSaxonAttack(self):
        self.assertEqual(self.apocal.saxonAttack(), self.viking.name +
                         ' has received ' + str(self.saxon.strength) + ' points of damage')

    def testUndeadAttackIsFunction(self):
        self.assertEqual(callable(self.apocal.undeadAttack), True)

    def testUndeadAttackReceiveNoParam(self):
        self.assertEqual(
            len(signature(self.apocal.undeadAttack).parameters), 0)

    def testUndeadAttackToViking(self):
        self.apocal.undeadAttack()
        self.assertEqual(len(self.apocal.vikingArmy), 0)

    def testUndeadAttackToSaxon(self):
        self.apocal.undeadAttack()
        self.assertEqual(len(self.apocal.saxonArmy), 0)

    def testGrowUndeadArmyToThree(self):
        self.apocal.undeadAttack()
        self.assertEqual(len(self.apocal.undeadArmy), 3)

    def testUndeadAttackReturnOutput(self):
        self.assertEqual(self.apocal.undeadAttack(),
                         "A Saxon has died in combat" + " and " + '{} has died in act of combat'.format(self.viking.name))

    def testShowStatusShouldIsFunction(self):
        self.assertEqual(callable(self.apocal.showStatus), True)

    def testShowStatusReceiveNoParams(self):
        self.assertEqual(len(signature(self.apocal.showStatus).parameters), 0)

    def testShouldReturnStringVikingsDied(self):
        self.apocal.vikingAttack()
        self.assertEqual(self.apocal.showStatus(),
                         "Saxons now belong to the army of the Undead.")

    def testShouldReturnStringSaxonsDied(self):
        for i in range(12):
            self.apocal.saxonAttack()
        self.assertEqual(self.apocal.showStatus(
        ), "Vikings now live in Valhalla. The Earth belongs to the Undead.")

    def testShouldReturnStringStillFighting(self):
        self.assertEqual(
            self.apocal.showStatus(), "Vikings and Saxons are still growing the Undead Army.")


if __name__ == '__main__':
    unittest.main()
