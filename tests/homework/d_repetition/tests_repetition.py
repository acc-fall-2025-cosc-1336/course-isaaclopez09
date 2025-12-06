import unittest 

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_Config(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(get_factorial(0), 1)
        self.assertEqual(get_factorial(3), 6)
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(-1), "Factorial is not defined for negative numbers.")



    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(3), 4)
        self.assertEqual(sum_odd_numbers(10), 25)
        


        
