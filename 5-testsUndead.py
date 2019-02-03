import unittest
from vikingsClases import Undead
from inspect import signature


class TestUndead(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.strength = 2000
        cls.health = 5000
        cls.anger = 1
        cls.undead = Undead(cls.health, cls.strength, cls.anger)

    def testConstructorSignature(self):
        self.assertEqual(len(signature(Undead).parameters), 3)

    def testHealth(self):
        self.assertEqual(self.undead.health, self.health)

    def testStrenght(self):
        self.assertEqual(self.undead.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.undead.attack), True)

    def testAttackHasNoParams(self):
        self.assertEqual(len(signature(self.undead.attack).parameters), 0)

    def testAttackRetunsStrength(self):
        self.assertEqual(self.undead.attack(),
                         (self.strength)*self.undead.anger)

    def testReceivesDamage(self):
        self.assertEqual(callable(self.undead.receiveDamage), True)

    def testReceivesDamageHasParams(self):
        self.assertEqual(
            len(signature(self.undead.receiveDamage).parameters), 1)

    def testReceiveDamageReturnNone(self):
        self.assertEqual(self.undead.receiveDamage(
            50), "The Undead has recovered 50 points of damage.")

    def testCanReceiveDamage(self):
        self.undead.receiveDamage(50)
        self.assertEqual(self.undead.health, self.health + 50)

    def testFrenzy(self):
        self.assertEqual(callable(self.undead.frenzy), True)

    def testFrenzyScreamsTheShitOutOfTheUndead(self):
        self.assertEqual(self.undead.frenzy(
        ), "The Ragnarok of the undead will put the Valkyries down!")

    def testFrenzyIncreasesUndeadStrength(self):
        self.undead.frenzy()
        self.assertGreater(self.undead.strength, self.strength)


if __name__ == '__main__':
    unittest.main()
