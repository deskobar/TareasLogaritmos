import unittest
from priorityQueue import BinaryHeap

class BinaryHeapTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = BinaryHeap()
    
    def test_default(self):
        self.assertEqual(self.heap.tree, [])
        self.assertEqual(self.heap.n, 0)
        self.assertEqual(self.heap.)

    def test_insert(self):
        self.heap.insert(1, 5)