# -*- coding: UTF-8 -*-
from src.dijkstra_base import dijkstra
from src.priorityQueue import BinaryHeap, FibonacciHeap
import sys

def dijkstra_controller():
    graph = {}
    vertices, aristas = list(map(int, input().split()))
    for i in range(vertices):
        graph[i+1] = {}
    for i in range(aristas):
        u, v, s = list(map(int, input().split()))
        graph[u][v] = s
        graph[v][u] = s
    print(graph)
    start = int(input())
    if sys.argv[1] == "FibonacciHeap":
        queue = FibonacciHeap(vertices)
    else:
        queue = BinaryHeap(vertices)
    print(dijkstra(graph, start, queue))
     
dijkstra_controller()

"""
Input 
6 10
1 2 2
1 6 8
1 3 1
2 3 6
2 5 3
2 6 5
3 4 2
3 5 4
4 5 7
5 6 1
1
"""