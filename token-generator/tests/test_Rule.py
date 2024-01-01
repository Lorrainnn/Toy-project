from project4 import *
import unittest
class Test_Rule(unittest.TestCase):
    def test_rule(self):

        object1 = Rule(['HowIsBoo', '1 Boo is [Adjective] today'])
        self.assertEqual({Variable('[HowIsBoo]'): [(1, [Terminal('Boo'), Terminal('is'), Variable('[Adjective]'), Terminal('today')])]},
                         object1.process_rule())

    def test_rule2(self):
        object2 = Rule(['HowIsBoo', '1 Boo', '2 [Cathy]'])
        self.assertEqual({Variable('[HowIsBoo]'): [(1, [Terminal('Boo')]), (2, [Variable('[Cathy]')])]},
                         object2.process_rule())

