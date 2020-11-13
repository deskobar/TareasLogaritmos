import unittest
from src.dijkstra_base import dijkstra
from src.priorityQueue import BinaryHeap  # , FibonacciHeap
from src.utils import graph_to_dict

"""
Input/output robado de:
        https://codeforces.com/problemset/problem/545/E
        https://codeforces.com/contest/20/problem/C
"""


class DijkstraTestCase(unittest.TestCase):

    def setUp(self):
        self.base_start, self.base_graph = 1, graph_to_dict(
            "6 10 1 2 2 1 6 8 1 3 1 2 3 6 2 5 3 2 6 5 3 4 2 3 5 4 4 5 7 5 6 1")
        self.tc_1_start, self.tc_1_graph = 1, graph_to_dict(
            "5 6 1 2 2 2 5 5 2 3 4 1 4 1 4 3 3 3 5 1")
        self.tc_2_start, self.tc_2_graph = 3, graph_to_dict(
            "3 3 1 2 1 2 3 1 1 3 2")
        self.binary_heap = BinaryHeap()
        # self.fibonacci_heap = FibonacciHeap()

    def test_base_dijkstra_binary(self):
        resultado = dijkstra(
            self.base_graph, self.base_start, self.binary_heap)
        self.assertEqual(resultado, "0 2 1 3 5 6")

    def test_case_1_dijkstra_binary(self):
        resultado = dijkstra(
            self.tc_1_graph, self.tc_1_start, self.binary_heap)
        self.assertEqual(resultado, "0 2 4 1 5")

    def test_case_2_dijkstra_binary(self):
        resultado = dijkstra(
            self.tc_2_graph, self.tc_2_start, self.binary_heap)
        self.assertEqual(dijkstra(resultado, "2 1 0")

if __name__ == "__main__":
    unittest.main()