import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_dictionary(unittest.TestCase):
    def test_add_inventory(self):
        widgets = {}
        add_inventory(widgets, "Widget1", 10)
        self.assertEqual(widgets["Widget1"], 10)
        add_inventory(widgets, "Widget1", 25)   
        self.assertEqual(widgets["Widget1"], 35)    
        add_inventory(widgets, "Widget1", -10)   
        self.assertEqual(widgets["Widget1"], 25)    


    def test_remove_inventory_widget(self):
        widgets = {}
        add_inventory(widgets, "widget1", 15)
        add_inventory(widgets, "widget2", 20)
        remove_inventory_widget(widgets, "widget1")
        self.assertEqual(len(widgets),1)
        self.assertEqual(widgets["widget2"], 20)