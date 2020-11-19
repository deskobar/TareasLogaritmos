import unittest
from src.priorityQueue import FibonacciHeap
from src.trees import BinomNode

class TestBinomNode(unittest.TestCase):

    def setUp(self):
        self.node_1 = BinomNode(1, 10)
        self.node_2 = BinomNode(2, 9)
        self.node_3 = BinomNode(3, 8)
        self.node_4 = BinomNode(4, 7)

    def test_default(self):
        self.assertEqual(self.node_1.element, 1)
        self.assertEqual(self.node_1.key, 10)
        self.assertEqual(self.node_1.left, None)
        self.assertEqual(self.node_1.right, None)
        self.assertEqual(self.node_1.parent, None)
        self.assertEqual(self.node_1.child, None)
        self.assertEqual(self.node_1.element, 1)
        self.assertEqual(self.node_.key, 10)
        self.assertEqual(self.node_2.left, None)
        self.assertEqual(self.node_2.right, None)
        self.assertEqual(self.node_2.parent, None)
        self.assertEqual(self.node_2.child, None)
        self.assertEqual(self.node_3.element, 1)
        self.assertEqual(self.node_3.key, 10)
        self.assertEqual(self.node_3.left, None)
        self.assertEqual(self.node_3.right, None)
        self.assertEqual(self.node_3.parent, None)
        self.assertEqual(self.node_3.child, None)
        self.assertEqual(self.node_4.element, 1)
        self.assertEqual(self.node_4.key, 10)
        self.assertEqual(self.node_4.left, None)
        self.assertEqual(self.node_4.right, None)
        self.assertEqual(self.node_4.parent, None)
        self.assertEqual(self.node_4.child, None)
    
    def test_append_node(self):
        self.node_1.append_node(self.node_2)
        self.assertEqual(self.node_1.right, self.node_2)
        self.assertEqual(self.node_2.left, self.node_1)
        self.node_1.append_node(self.node_3)
        self.assertEqual(self.node_1.right, self.node_3)
        self.assertEqual(self.node_3.left, self.node_1)
        self.assertEqual(self.node_3.right, self.node_2)
        self.assertEqual(self.node_2.left, self.node_3)

    def test_isolate(self):
        self.node_1.append_node(self.node_2)
        self.node_1.append_node(self.node_3)
        self.node_1.append_node(self.node_4)
        self.node_4.isolate()
        self.assertEqual(self.node_1.right, self.node_3)
        self.assertEqual(self.node_3.left, self.node_1)
        self.assertEqual(self.node_3.right, self.node_2)
        self.assertEqual(self.node_2.left, self.node_3)
        self.assertEqual(self.node_4.right, None)
        self.assertEqual(self.node_4.left, None)
