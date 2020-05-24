import unittest
from ..datalayer.basic_math import Basic_Calculator, CustomException


class TestBasicMath(unittest.TestCase):
    def __init__(self):
        print("function called")
        self.basic_calc = Basic_Calculator(num1=5, num2=0)
        print(self.basic_calc.add())

    def test_add(self):
        self.assertEqual(self.basic_calc.add(), 5)


if __name__ == "__main__":
    x = 2
    print(x)