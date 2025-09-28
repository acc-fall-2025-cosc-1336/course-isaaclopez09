import unittest
'''
the file in /tests/homework/c_decisions
has the test functions
'''

from tests.homework.c_decisions import tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
unittest.TextTestRunner(verbosity=2).run(suite)
