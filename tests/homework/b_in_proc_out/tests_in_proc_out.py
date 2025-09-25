import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.b_in_proc_out.output import get_sales_tax, get_tip_ammount

class Test_Config(unittest.TestCase):

    def test_get_sales_tax(self):
        #test that the function get_number returns 1
        self.assertEqual(6.75, get_sales_tax(100))
        self.assertEqual(13.5, get_sales_tax(200))
    
    def test_get_tip_ammount(self):
        #test that the function get_number returns 2
        self.assertEqual(20, get_tip_ammount(100, .2))
        self.assertEqual(40, get_tip_ammount(200, .2))