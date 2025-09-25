import unittest

from src.homework.b_in_proc_out.output import multiply_numbers

class Test_Config(unittest.TestCase):

    def test_multiply_numbers(self):
        self.assertEqual(25, multiply_numbers(5, 5))
        self.assertEqual(49, multiply_numbers(7, 7))

