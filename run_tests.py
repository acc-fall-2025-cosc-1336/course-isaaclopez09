import unittest
'''
the file in /tests/homework/d_repetitions
has the test functions
'''

from tests.homework.e_functions import tests_functions

suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner(verbosity=2).run(suite)
