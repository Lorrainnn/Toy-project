from project4 import *
import unittest

class Test_Symbol(unittest.TestCase):

    def test_Variable(self):
        object1 = Variable('apple')
        object2 = Terminal('pear')
        object3 = Variable('apple')
        object4 = Variable('pear')

        self.assertTrue(object1 != object2)
        self.assertTrue(object1 != object4)
        self.assertTrue(hash(object1) == hash(object3))

    def test_Terminal(self):
        object1 = Terminal('sheep')
        object2 = Terminal('wolf')
        object3 = Variable('tiger')
        self.assertEqual(hash('wolf'), hash(object2))
        self.assertEqual('sheep', object1.get_value())
        self.assertNotEqual(object1, object3)