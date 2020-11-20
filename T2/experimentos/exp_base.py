import statistics
import time
from src.generator_base import generator
from src.priorityQueue import BinaryHeap, FibonacciHeap
from src.dijkstra_base import dijkstra
import tracemalloc


def exp(heap, v_range, p_range):
    """
    FIJAR P Y PROBAR CON DIFERENTES V
    """
    out = {}
    for v in v_range:
        current_v = {}
        for p in p_range:
            list_k = []
            list_memory_current = []
            list_memory_peak = []
            for i in range(3):
                graph, start = generator(v, p)
                if heap == "fibo":
                    tracemalloc.start()
                    ti = time.time()
                    dijkstra(graph, start, FibonacciHeap(v))
                    tf = time.time()
                    current, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                else:
                    tracemalloc.start()
                    ti = time.time()
                    dijkstra(graph, start, BinaryHeap(v))
                    tf = time.time()
                    current, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                dt = tf - ti
                list_k.append(dt)
                list_memory_current.append(current)
                list_memory_peak.append(peak)
            current_v[p] = {"time_mean": statistics.mean(list_k),
                            "time_std": statistics.stdev(list_k),
                            "memory_current_mean": statistics.mean(list_memory_current),
                            "memory_current_std": statistics.stdev(list_memory_current),
                            "memory_peak_mean": statistics.mean(list_memory_peak),
                            "memory_peak_std": statistics.stdev(list_memory_peak)}
        out[v] = current_v
    return out
