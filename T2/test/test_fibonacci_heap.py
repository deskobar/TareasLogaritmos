import unittest
from src.priorityQueue import FibonacciHeap
from src.trees import BinomNode
'''
class FibonacciHeapTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = FibonacciHeap(20)

    def _assert_equal_trees(self, tree_1, tree_2):
        self._assert_equal_nodes(tree_1, tree_2)
        for i in range(len(tree_1.children)):
            self._assert_equal_trees(tree_1.children[i], tree_2.children[i])
    
    def _assert_equal_nodes(self, node_1, node_2):
        self.assertEqual(node_1.element, node_2.element)
        self.assertEqual(node_1.key, node_2.key)
        self.assertEqual(node_1.degree, node_2.degree)
    
    def _assert_equal_heaps(self, heap_1, heap_2):
        self.assertEqual(heap_1.queue_length, heap_2.queue_length)
        self.assertEqual(heap_1.min_element, heap_2.min_element)
        self.assertEqual(heap_1.min_key, heap_2.min_key)
        self.assertEqual(heap_1.min_pos, heap_2.min_pos)
        self.assertEqual(heap_1.current_elements, heap_2.current_elements)
        for i in len(heap_1.queue):
            self._assert_equal_trees(heap_1.queue[i], heap_2.queue[i])
        for i in len(heap_1.elements_in_order):
            self._assert_equal_nodes(heap_1.elements_in_order[i], heap_2.elements_in_order[i])
    
    def test_initial_conditions(self):
        self.assertEqual(self.heap.queue, [])
        self.assertEqual(self.heap.queue_length, 0)
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
        self.heap.insert(2, 4)
        self.heap.decrease_key(1, 2)
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
        self.heap.insert(2, 4)
        self.heap.decrease_key(1, 2)
        self.heap.extract_min()
        self._assert_equal_node_arrays(self.heap.tree, [BMinHeapNode(10, 3, 0), BMinHeapNode(2, 4, 1), BMinHeapNode(15, 7, 2)])
        self.assertEqual(self.heap.n, 3)

    def test_empty(self):
        self.heap.insert(10, 3)
        self.heap.insert(2, 4)
        self.heap.insert(15, 7)
        for _i in range(3):
            print("value of n is: " + str(self.heap.n))
            self.assertFalse(self.heap.empty())
            self.heap.extract_min()
        self.assertTrue(self.heap.empty())

if __name__ == "__main__":
    unittest.main()
'''