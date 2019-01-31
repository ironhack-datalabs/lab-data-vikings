import unittest
from vikingsClases import * 

class MyTest(unittest.TestCase):

  def testSoldier(self):
    strength = 150
    health = 300
    soldier = Soldier(health, strength)

    # Soldier should recive 2 arguments
    self.assertEqual(soldier.health, health)
    self.assertEqual(soldier.strength, strength)
    #self.assertEqual(type(soldier.attack), method)
    #soldier attack should recive 0 arguments
    self.assertEqual(soldier.attack(), strength)
    #soldier recive damage should be function
    #should receive 1 argument (the damage)
    soldier.receiveDamage(50)
    self.assertEqual(soldier.health, health - 50)
    self.assertEqual(soldier.receiveDamage(50), None)

  def testViking(self):
    name = 'Harald'
    strenght = 150
    health = 300
    viking = Viking(name, strenght, health)
    # should inherit from Soldier
    # should recive 3 arguments
    self.assertEqual(viking.name, name)
    self.assertEqual(viking.health, health)
    self.assertEqual(viking.strength, strenght)
    # attack method should be a function
    # should recive 0 arguments
    self.assertEqual(viking.attack(), strenght)
    # recive damage should be a function
    # should recive one argument
    viking.receiveDamage(50)
    self.assertEqual(viking.health, health - 50)
    self.assertEqual(viking.receiveDamage(50), name + ' has received 50 points of damage')
    self.assertEqual(viking.receiveDamage(70), name + ' has received 70 points of damage')
    self.assertEqual(viking.receiveDamage(health), name + ' has died in act of combat')
    # viking battle cry should be a function
    #self.assertEqual(viking.battleCry(), 'Odins Owns You All!')

  def testSaxon(self):
    health = 60
    strenght = 25

    saxon = Saxon(health, strenght)
    # should inherit from Soldier
    # should receive 2 arguments (health & strength)
    self.assertEqual(saxon.health, health)
    self.assertEqual(saxon.strength, strenght)
    # attack should be a function
    self.assertEqual(saxon.attack(), strenght)
    # recive damage should be a function
    # recive dammage should recive one argument



if __name__ == '__main__':
    unittest.main()