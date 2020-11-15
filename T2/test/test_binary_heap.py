import unittest
from TareasLogaritmos.T2.src.priorityQueue import BinaryHeap
from TareasLogaritmos.T2.src.trees import BMinHeapNode

class BinaryHeapTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = BinaryHeap(20)

    def _assert_equal_nodes(self, node_1, node_2):
        self.assertEqual(node_1.element, node_2.element)
        self.assertEqual(node_1.key, node_2.key)
        self.assertEqual(node_1.pos, node_2.pos)
    
    def _assert_equal_node_arrays(self, n_arr_1, n_arr_2):
        for i in range(len(n_arr_1)):
            self._assert_equal_nodes(n_arr_1[i], n_arr_2[i])
    
    def test_initial_conditions(self):
        self.assertEqual(self.heap.tree, [])
        self.assertEqual(self.heap.n, 0)
        self.assertEqual(self.heap.elements_in_order, [None] * 20)

    def test_insert(self):
        self.heap.insert(1, 5)
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(1, 5, 0)])
        self.assertEqual(self.heap.tree[0], self.heap.elements_in_order[0])
        self.assertEqual(self.heap.n, 1)
        self.heap.insert(10, 3)
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(10, 3, 0), BMinHeapNode(1, 5, 1)])
        self.assertEqual(self.heap.tree[1], self.heap.elements_in_order[0])
        self.assertEqual(self.heap.tree[0], self.heap.elements_in_order[9])
        self.assertEqual(self.heap.n, 2)
        self.heap.insert(15, 7)
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(10, 3, 0), BMinHeapNode(1, 5, 1), BMinHeapNode(15, 7, 2)])
        self.assertEqual(self.heap.tree[1], self.heap.elements_in_order[0])
        self.assertEqual(self.heap.tree[0], self.heap.elements_in_order[9])
        self.assertEqual(self.heap.tree[2], self.heap.elements_in_order[14])
        self.assertEqual(self.heap.n, 3)
        self.heap.insert(2, 4)
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(10, 3, 0), BMinHeapNode(2, 4, 1), BMinHeapNode(15, 7, 2), BMinHeapNode(1, 5, 3)])
        self.assertEqual(self.heap.tree[1], self.heap.elements_in_order[1])
        self.assertEqual(self.heap.tree[0], self.heap.elements_in_order[9])
        self.assertEqual(self.heap.tree[2], self.heap.elements_in_order[14])
        self.assertEqual(self.heap.tree[3], self.heap.elements_in_order[0])
        self.assertEqual(self.heap.n, 4)
    
    def test_decrease_key(self):
        self.heap.insert(1, 5)
        self.heap.insert(10, 3)
        self.heap.insert(15, 7)
        self.heap.insert(-5, 4)
        self.heap.decrease_key(1, 2)
        self.assertEqual(self.heap.tree, [(1, 2), (10, 3), (15, 7), (-5, 4)])
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(1, 2, 0), BMinHeapNode(10, 3, 1), BMinHeapNode(15, 7, 2), BMinHeapNode(2, 4, 3)])
        self.assertEqual(self.heap.tree[0], self.heap.elements_in_order[0])
        self.assertEqual(self.heap.n, 4)
        self.heap.decrease_key(15, 8)
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(1, 2, 0), BMinHeapNode(10, 3, 1), BMinHeapNode(15, 7, 2), BMinHeapNode(2, 4, 3)])
        self.assertEqual(self.heap.n, 4)
    
    def test_extract_min(self):
        self.heap.insert(1, 5)
        self.heap.insert(10, 3)
        self.heap.insert(15, 7)
        self.heap.insert(-5, 4)
        self.heap.decrease_key(1, 2)
        self.heap.extract_min()
        self.assertEqual(self.heap.tree, [(10, 3), (-5, 4), (15, 7)])
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(10, 3, 0), BMinHeapNode(2, 4, 1), BMinHeapNode(15, 7, 2)])
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
