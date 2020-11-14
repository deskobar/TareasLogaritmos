import unittest
from src.dijkstra_base import dijkstra
from src.priorityQueue import BinaryHeap, FibonacciHeap 
from src.generator_base import generator
import random

class ConsistenciaTestCase(unittest.TestCase):

    def test_case_consistencia2(self):
        for i in range(2, 100):
            p = random.random()
            graph, start = generator(i, p)
            bin_dij = dijkstra(graph, start, BinaryHeap(i))
            fib_dij = dijkstra(graph, start, FibonacciHeap(i))
            self.assertEqual(bin_dij, fib_dij)
    
    def test_case_aguanta(self):
        nodos = 10000
        p = 1
        graph, start = generator(nodos, p)
        bin_dij = dijkstra(graph, start, BinaryHeap(nodos))
        fib_dij = dijkstra(graph, start, FibonacciHeap(nodos))
        self.assertEqual(bin_dij, fib_dij)
    
if __name__ == "__main__":
    unittest.main()