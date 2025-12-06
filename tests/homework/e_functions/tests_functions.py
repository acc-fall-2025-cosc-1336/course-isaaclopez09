import unittest 

from src.homework.e_functions.value_return import get_federal_tax, get_fica_tax, get_gross_pay

class Test_get_gross_pay(unittest.TestCase):
    def test_get_gross_pay(self):
        self.assertEqual(get_gross_pay(40,10), 400)
        self.assertEqual(get_gross_pay(45,10), 475)
        self.assertEqual(get_gross_pay(30,10), 300)

class Test_get_fica_tax(unittest.TestCase):
    def test_get_fica_tax(self):
        self.assertEqual(get_fica_tax(400), (400*.0765))
        self.assertEqual(get_fica_tax(475), (475*.0765))
        self.assertEqual(get_fica_tax(300), 22.95)

class Test_get_federal_tax(unittest.TestCase):
    def test_get_federal_tax(self):
        self.assertEqual(get_federal_tax(400), 32)
        self.assertEqual(get_federal_tax(475), 38)
        self.assertEqual(get_federal_tax(300), 24)