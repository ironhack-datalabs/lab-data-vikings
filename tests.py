import unittest
from viking import * 

class TestStringMethods(unittest.TestCase):

  strength = 150
  health = 300

  soldier = Soldier(health, strength)

  def constructor_function(self):
    self.assertEqual(Soldier.length, 2)
    self.assertEqual(soldier.health, helath)
    self.assertEqual(soldier.strenght, strenght)
  
  def attack_method(self):
    self.assertEqual(typeof (soldier.attack), function)


if __name__ == '__main__':
    unittest.main()