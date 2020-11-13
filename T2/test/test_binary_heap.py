import unittest
from src.priorityQueue import BinaryHeap

class BinaryHeapTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = BinaryHeap()
    
    def test_default(self):
        self.assertEqual(self.heap.tree, [])
        self.assertEqual(self.heap.n, 0)

    def test_insert(self):
        self.heap.insert(1, 5)
        self.assertEqual(self.heap.tree, [(1, 5)])
        self.assertEqual(self.heap.n, 1)
        self.heap.insert(10, 3)
        self.assertEqual(self.heap.tree, [(10, 3), (1, 5)])
        self.assertEqual(self.heap.n, 2)
        self.heap.insert(15, 7)
        self.assertEqual(self.heap.tree, [(10, 3), (1, 5), (15, 7)])
        self.assertEqual(self.heap.n, 3)
        self.heap.insert(-5, 4)
        self.assertEqual(self.heap.tree, [(10, 3), (-5, 4), (15, 7), (1, 5)])
        self.assertEqual(self.heap.n, 4)
    
    def test_decrease_key(self):
        self.heap.insert(1, 5)
        self.heap.insert(10, 3)
        self.heap.insert(15, 7)
        self.heap.insert(-5, 4)
        self.heap.decrease_key(1, 2)
        self.assertEqual(self.heap.tree, [(1, 2), (10, 3), (15, 7), (-5, 4)])
        self.assertEqual(self.heap.n, 4)
        self.heap.decrease_key(15, 8)
        self.assertEqual(self.heap.tree, [(1, 2), (10, 3), (15, 7), (-5, 4)])
        self.assertEqual(self.heap.n, 4)
    
    def test_extract_min(self):
        self.heap.insert(1, 5)
        self.heap.insert(10, 3)
        self.heap.insert(15, 7)
        self.heap.insert(-5, 4)
        self.heap.decrease_key(1, 2)
        self.heap.extract_min()
        self.assertEqual(self.heap.tree, [(10, 3), (-5, 4), (15, 7)])
        self.assertEqual(self.heap.n, 3)

    def test_empty(self):
        self.heap.insert(10, 3)
        self.heap.insert(-5, 4)
        self.heap.insert(15, 7)
        for _i in range(3):
            print("value of n is: " + str(self.heap.n))
            self.assertFalse(self.heap.empty())
            self.heap.extract_min()
        self.assertTrue(self.heap.empty())

if __name__ == "__main__":
    unittest.main()
