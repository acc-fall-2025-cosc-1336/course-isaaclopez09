import unittest
'''
the file in /tests/homework/d_repetitions
has the test functions
'''

from tests.homework.d_repetition.tests_repetition import get_factorial, sum_odd_numbers

suite = unittest.TestLoader().loadTestsFromModule(get_factorial)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromModule(sum_odd_numbers)
unittest.TextTestRunner(verbosity=2).run(suite)
