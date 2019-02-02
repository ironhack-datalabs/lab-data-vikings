import unittest
from vikingsClases import Soldier
from vikingsClases import Viking
from vikingsClases import Saxon
from vikingsClases import War
from inspect import signature


class TestSoldier(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.strength = 150
        cls.health = 300
        cls.soldier = Soldier(cls.health, cls.strength)

    def testConstructorSignature(self):
        self.assertEqual(len(signature(Soldier).parameters), 2)

    def testHealth(self):
        self.assertEqual(self.soldier.health, self.health)

    def testStrenght(self):
        self.assertEqual(self.soldier.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.soldier.attack), True)

    def testAttackHasNoParams(self):
        self.assertEqual(len(signature(self.soldier.attack).parameters), 0)

    def testAttackRetunsStrength(self):
        self.assertEqual(self.soldier.attack(), self.strength)

    def testReceivesDamage(self):
        self.assertEqual(callable(self.soldier.receiveDamage), True)

    def testReceivesDamageHasParams(self):
        self.assertEqual(
            len(signature(self.soldier.receiveDamage).parameters), 1)

    def testReceiveDamageReturnNone(self):
        self.assertEqual(self.soldier.receiveDamage(50), None)

    def testCanReceiveDamage(self):
        self.soldier.receiveDamage(50)
        self.assertEqual(self.soldier.health, self.health - 50)


if __name__ == '__main__':
    unittest.main()
    
    
class TestViking(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.name = 'Harald'
        cls.strength = 150
        cls.health = 300
        cls.viking = Viking(cls.name, cls.health, cls.strength)

    def testShouldReciveThreeParams(self):
        self.assertEqual(len(signature(Viking).parameters), 3)

    def testName(self):
        self.assertEqual(self.viking.name, self.name)

    def testHealth(self):
        self.assertEqual(self.viking.health, self.health)

    def testStrenght(self):
        self.assertEqual(self.viking.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.viking.attack), True)

    def testAttackReciveNoParameters(self):
        self.assertEqual(len(signature(self.viking.attack).parameters), 0)

    def testAttackSouldReturnStrength(self):
        self.assertEqual(self.viking.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.viking.receiveDamage), True)

    def testReceiveDamageReciveOneParam(self):
        self.assertEqual(
            len(signature(self.viking.receiveDamage).parameters), 1)

    def testReciveDamageShouldRestHealth(self):
        self.viking.receiveDamage(50)
        self.assertEqual(self.viking.health, self.health - 50)

    def testReciveDamageShouldReturnString50(self):
        self.assertEqual(self.viking.receiveDamage(50), self.name +
                         ' has received 50 points of damage')

    def testReciveDamageShouldReturnString70(self):
        self.assertEqual(self.viking.receiveDamage(70), self.name +
                         ' has received 70 points of damage')

    def testReceiveDamageShouldReturnStringDeath(self):
        self.assertEqual(self.viking.receiveDamage(self.health),
                         self.name + ' has died in act of combat')

    def testBattleCry(self):
        self.assertEqual(callable(self.viking.battleCry), True)

    def testBattleCryReturnString(self):
        self.assertEqual(self.viking.battleCry(), 'Odin Owns You All!')


if __name__ == '__main__':
    unittest.main()
    
class TestSaxon(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.health = 60
        cls.strength = 25
        cls.saxon = Saxon(cls.health, cls.strength)

    def testSaxonShouldReceiveTwoParams(self):
        self.assertEqual(len(signature(Saxon).parameters), 2)

    def testHealth(self):
        self.assertEqual(self.saxon.health, self.health)

    def testStrength(self):
        self.assertEqual(self.saxon.strength, self.strength)

    def testAttack(self):
        self.assertEqual(callable(self.saxon.attack), True)

    def testAttackShouldReceiveNoParams(self):
        self.assertEqual(len(signature(self.saxon.attack).parameters), 0)

    def testAttackREturnStrength(self):
        self.assertEqual(self.saxon.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.saxon.receiveDamage), True)

    def testReceiveDamageShouldReceiveOneParam(self):
        self.assertEqual(
            len(signature(self.saxon.receiveDamage).parameters), 1)

    def testReceiveDamage(self):
        self.saxon.receiveDamage(1)
        self.assertEqual(self.saxon.health, self.health - 1)

    def testReceiveDamageString45(self):
        self.assertEqual(self.saxon.receiveDamage(
            45), 'A Saxon has received 45 points of damage')

    def testReceiveDamageString10(self):
        self.assertEqual(self.saxon.receiveDamage(
            10), 'A Saxon has received 10 points of damage')

    def testReceiveDamageStringDied(self):
        self.assertEqual(self.saxon.receiveDamage(self.health),
                         'A Saxon has died in combat')


if __name__ == '__main__':
    unittest.main()
    
class TestWar(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.war = War()

    def testWarShouldReciveNoParams(self):
        self.assertEqual(len(signature(War).parameters), 0)

    def testVikingArmy(self):
        self.assertEqual(self.war.vikingArmy, [])

    def testSaxonArmy(self):
        self.assertEqual(self.war.saxonArmy, [])


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

        cls.viking = generateViking()
        cls.saxon = generateSaxon()
        cls.war = War()
        cls.war.addSaxon(cls.saxon)
        cls.war.addViking(cls.viking)

    def testAddViking(self):
        self.assertEqual(callable(self.war.addViking), True)

    def testAddVikingShouldReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.addViking).parameters), 1)

    def testAddVikingInList(self):
        self.assertEqual(self.war.vikingArmy, [self.viking])

    def testAddVikingReturnNull(self):
        self.assertEqual(self.war.addViking(self.viking), None)

    def testAddSaxonShouldBeFunction(self):
        self.assertEqual(callable(self.war.addSaxon), True)

    def testAddSaxonReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.addSaxon).parameters), 1)

    def testSaxonArmyReturnEmptyList(self):
        self.assertEqual(self.war.saxonArmy, [self.saxon])

    def testAddSaxonReturnNone(self):
        self.assertEqual(self.war.addSaxon(self.saxon), None)

    def testVikingAttackIsFunction(self):
        self.assertEqual(callable(self.war.vikingAttack), True)

    def testVikingAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.vikingAttack).parameters), 0)

    def testSaxonHealth(self):
        oldHealt = self.saxon.health
        self.war.vikingAttack()
        self.assertEqual(self.saxon.health, oldHealt - self.viking.strength)

    def testVikingAttack(self):
        self.war.vikingAttack()
        self.assertEqual(len(self.war.saxonArmy), 0)

    def testAddSaxon(self):
        print(self.war.__dict__)
        self.assertEqual(self.war.vikingAttack(), 'A Saxon has died in combat')

    def testSaxonAttackIsFunction(self):
        self.assertEqual(callable(self.war.saxonAttack), True)

    def testSaxonAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.saxonAttack).parameters), 0)

    def testVikingHealth(self):
        oldHealt = self.viking.health
        self.war.saxonAttack()
        self.assertEqual(self.viking.health, oldHealt - self.saxon.strength)

    def testVikingArmyList(self):
        for i in range(12):
            if(len(self.war.vikingArmy) == 0):
                break
            self.war.saxonAttack()
        self.assertEqual(len(self.war.vikingArmy), 0)

    def testReturnOfSaxonAttack(self):
        self.assertEqual(self.war.saxonAttack(), self.viking.name +
                         ' has received ' + str(self.saxon.strength) + ' points of damage')

    def testShowStatusShouldIsFunction(self):
        self.assertEqual(callable(self.war.showStatus), True)

    def testShowStatusReceiveNoParams(self):
        self.assertEqual(len(signature(self.war.showStatus).parameters), 0)

    def testShouldReturnStringVikingsWon(self):
        self.war.vikingAttack()
        self.assertEqual(self.war.showStatus(),
                         'Vikings have won the war of the century!')

    def testShouldReturnStringSaxonsWon(self):
        for i in range(12):
            self.war.saxonAttack()
        self.assertEqual(self.war.showStatus(
        ), 'Saxons have fought for their lives and survive another day...')

    def testShouldReturnStringStillFighting(self):
        self.assertEqual(
            self.war.showStatus(), 'Vikings and Saxons are still in the thick of battle.')


if __name__ == '__main__':
    unittest.main()
    