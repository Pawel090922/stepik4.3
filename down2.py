import unittest

from function2 import silnia

class Testfunction(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(silnia(5),121)

if __name__ == '__main__':
    unittest.main()
