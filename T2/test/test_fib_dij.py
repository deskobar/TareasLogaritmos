import unittest
from src.dijkstra_base import dijkstra
from src.otherQueue import aFibonacciHeap
from src.utils import graph_to_dict

"""
Input/output robado de:
        https://codeforces.com/problemset/problem/545/E
        https://codeforces.com/contest/20/problem/C
"""


class FibDijTestCase(unittest.TestCase):

    def setUp(self):
        self.base_start, self.base_graph = 1, graph_to_dict(
            "6 10 1 2 2 1 6 8 1 3 1 2 3 6 2 5 3 2 6 5 3 4 2 3 5 4 4 5 7 5 6 1")
        self.tc_1_start, self.tc_1_graph = 1, graph_to_dict(
            "5 6 1 2 2 2 5 5 2 3 4 1 4 1 4 3 3 3 5 1")
        self.tc_2_start, self.tc_2_graph = 3, graph_to_dict(
            "3 3 1 2 1 2 3 1 1 3 2")
        self.tc_3_start, self.tc_3_graph = 7, graph_to_dict(
            "10 9 1 2 583038406 2 3 624346256 3 4 53912901 4 5 28792708 5 6 885781087 6 7 289571756 7 8 11214701 8 9 593731365 9 10 797523118")

    def test_case_aaah(self):
        resultado = dijkstra(
            self.base_graph, self.base_start, aFibonacciHeap(6))
        self.assertEqual(resultado, "0 2 1 3 5 6")

    def test_case_aaaaaaaah(self):
        resultado = dijkstra(
            self.tc_1_graph, self.tc_1_start, aFibonacciHeap(5))
        self.assertEqual(resultado, "0 2 4 1 5")

    def test_case_aaaaha(self):
        resultado = dijkstra(
            self.tc_2_graph, self.tc_2_start, aFibonacciHeap(3))
        self.assertEqual(resultado, "2 1 0")

    def test_case_aaaaaaaaaaahxd(self):
        resultado = dijkstra(
            self.tc_3_graph, self.tc_3_start, aFibonacciHeap(10))
        self.assertEqual(resultado, "2465443114 1882404708 1258058452 1204145551 1175352843 289571756 0 11214701 604946066 1402469184")
     

if __name__ == "__main__":
    unittest.main()
