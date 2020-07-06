import pytest
import unittest

from calc import Calc


class Calc_Test2(unittest.TestCase):

    simple_calc_two = Calc()

    def test_remainder(self):
        #self.assertTrue(self.simple_calc_two.remainder(9,9), )
        self.assertEqual(self.simple_calc_two.remainder(9, 9), 0)
    
