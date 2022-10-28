import unittest

from function import suma3

class Testfunction(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma3(2,3,5),10)

if __name__ == '__main__':
    unittest.main()