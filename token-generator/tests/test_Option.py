from project4 import *
import unittest

class Test_Option(unittest.TestCase):
    def test_option_func(self):
        object = Options(('3', ['happy', '[iceberg]']))
        self.assertEqual((3,[Terminal('happy'), Variable('[iceberg]')]), object.process_option())
