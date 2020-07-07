import unittest
import pytest

from calc_version_two import Functions

        
class Calc_Test(unittest.TestCase):

    a = Functions()

    def test_sqrt(self):
        self.assertEqual(self.a.find_sqrt(16), 4)

    def test_find_ceil(self):
        self.assertEqual(self.a.find_ceil(99.78967), 100)