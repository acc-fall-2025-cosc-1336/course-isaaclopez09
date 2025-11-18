import unittest

from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement


class Test_get_hamming_distance(unittest.TestCase):
    def test_get_hamming_distance(self):
        dna1 = "GAGCCTACTAACGGGAT"
        dna2 = "CATCGTAATGACGGCCT"
        self.assertEqual(get_hamming_distance(dna1, dna2), 7)

class Test_get_dna_complement(unittest.TestCase):
    def test_get_dna_complement(self):
        dna = "AAAACCCGGT"
        self.assertEqual(get_dna_complement(dna), "ACCGGGTTTT")

