import unittest
from datalayer import Basic_Calculator, CustomException


class TestBasicMath(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.basic_calc = Basic_Calculator(num1=5, num2=5)

    def test_add(self):
        self.assertEqual(self.basic_calc.add(), 10)

    def test_divide(self):
        self.assertEqual(self.basic_calc.divide, 1)
