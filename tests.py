import unittest
from viking import * 

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(hola(), 'hola')


if __name__ == '__main__':
    unittest.main()