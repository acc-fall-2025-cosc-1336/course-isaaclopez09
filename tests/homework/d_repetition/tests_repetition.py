import unittest 

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_get_factorial(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(get_factorial(0), 1)
        self.assertEqual(get_factorial(3), 6)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(-1), "Factorial is not defined for negative numbers.")


class Test_sum_odd_numbers(unittest.TestCase):
    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_number(3), 4)
        self.assertEqual(sum_odd_number(10), 25)
        


        
