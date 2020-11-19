import statistics
import time
import numpy as np
from src.generator_base import generator
from src.priorityQueue import BinaryHeap#, FibonacciHeap
from src.otherQueue import aFibonacciHeap as FibonacciHeap
from src.dijkstra_base import dijkstra

MAX = 26
v = 100
super_dict = {}
p_range = [p/10 for p in range(1, 11)]
v_range = range(2, 1003, 100)
"""
FIJAR V Y PROBAR CON DIFERENTES P
"""
def find_p(heap):
    out = {}
    for p in p_range:
        list_k = []
        for i in range(MAX):
            aaah = []
            graph, start = generator(v, p)
            for i in range(3):
                if heap == "fibo":
                    ti = time.time()
                    dijkstra(graph, start, FibonacciHeap(v))
                    tf = time.time()
                else:
                    ti = time.time()
                    dijkstra(graph, start, BinaryHeap(v))
                    tf = time.time()
                dt = tf - ti
                aaah.append(dt)
            list_k.append(statistics.mean(aaah))
        out[p] = {"time_mean": statistics.mean(list_k),
                  "time_std": statistics.stdev(list_k)}
    return out


"""
FIJAR P Y PROBAR CON DIFERENTES V
"""

def find_V(p, heap):
    out = {}
    for v in v_range:
        list_k = []
        for i in range(MAX):
            aaah = []
            graph, start = generator(v, p)
            for i in range(3):
                if heap == "fibo":
                    ti = time.time()
                    dijkstra(graph, start, FibonacciHeap(v))
                    tf = time.time()
                else:
                    ti = time.time()
                    dijkstra(graph, start, BinaryHeap(v))
                    tf = time.time()
                dt = tf - ti
                aaah.append(dt)
            list_k.append(statistics.mean(aaah))
        out[v] = {"time_mean": statistics.mean(list_k),
                  "time_std": statistics.stdev(list_k)}
    return out

