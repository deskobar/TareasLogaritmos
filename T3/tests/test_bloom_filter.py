import unittest
from src.bloom_filter import BloomFilter

class BloomFilterTestCase(unittest.TestCase):

    def setUp(self):
        self.bloom_filter = BloomFilter(247, 5)
        self.words = ['hola', 'como', 'estan', 'holis']
        self.bloom_filter.insert_list(self.words)

    def test_initial_conditions(self):
        for word in self.words:
            self.assertEqual(self.bloom_filter.check(word), 1)
    
    def test_word_i_know_not_in(self):
        self.assertEqual(self.bloom_filter.check("xd"), 0)
