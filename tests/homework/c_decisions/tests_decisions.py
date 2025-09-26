import unittest

from src.homework.c_decisions.decisions import numerical_grade_to_letter_grade

def test_numerical_grade_to_letter_grade(self):
    self.assertEqual(numerical_grade_to_letter_grade(95), "A")
    self.assertEqual(numerical_grade_to_letter_grade(85), "b")
    self.assertEqual(numerical_grade_to_letter_grade(75), "C")
    self.assertEqual(numerical_grade_to_letter_grade(65), "D")
    self.assertEqual(numerical_grade_to_letter_grade(50), "F")