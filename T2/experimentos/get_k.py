import statistics
import time
import numpy as np
from src.generator_base import generator
from src.priorityQueue import BinaryHeap#, FibonacciHeap
from src.otherQueue import aFibonacciHeap as FibonacciHeap
from src.dijkstra_base import dijkstra
import tracemalloc

MAX = 26
v = 100
super_dict = {}
p_range = [p/10 for p in range(1, 11)]
v_range = range(2, 103, 10)
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
        list_memory_current = []
        list_memory_peak = []
        for i in range(MAX):
            aaah = []
            memory_current = []
            memory_peak = []
            graph, start = generator(v, p)
            for i in range(3):
                tracemalloc.start()
                if heap == "fibo":
                    ti = time.time()
                    dijkstra(graph, start, FibonacciHeap(v))
                    tf = time.time()
                else:
                    ti = time.time()
                    dijkstra(graph, start, BinaryHeap(v))
                    tf = time.time()
                dt = tf - ti
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                aaah.append(dt)
                memory_current.append(current)
                memory_peak.append(peak)
            list_k.append(statistics.mean(aaah))
            list_memory_current.append(statistics.mean(memory_current))
            list_memory_peak.append(statistics.mean(memory_peak))
        out[v] = {"time_mean": statistics.mean(list_k),
                  "time_std": statistics.stdev(list_k),
                  "memory_current_mean": statistics.mean(list_memory_current),
                  "memory_current_std": statistics.stdev(list_memory_current),
                  "memory_peak_mean": statistics.mean(list_memory_peak),
                  "memory_peak_std": statistics.stdev(list_memory_peak)}
    return out

