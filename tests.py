import unittest
from vikingsClases import * 

class MyTest(unittest.TestCase):

  strength = 150
  health = 300
  soldier = Soldier(health, strength)

  def test(self):
    strength = 150
    health = 300
    soldier = Soldier(health, strength)
    # Soldier should recive 2 arguments
    self.assertEqual(soldier.health, health)
    self.assertEqual(soldier.strength, strength)
    #self.assertEqual(type(soldier.attack), method)
    #soldier attack should recive 0 arguments
    self.soldier.attack()


if __name__ == '__main__':
    unittest.main()