import statistics
import time
from src.generator_base import generator
from src.priorityQueue import BinaryHeap, FibonacciHeap
from src.dijkstra_base import dijkstra
import tracemalloc


def exp(v_range, p_range):
    """
    FIJAR P Y PROBAR CON DIFERENTES V
    """
    out = {"fib": {}, "bin": {}}
    for v in v_range:
        fib_current_v = {}
        bin_current_v = {}
        for p in p_range:
            fib_list_k = []
            fib_list_memory_current = []
            fib_list_memory_peak = []
            bin_list_k = []
            bin_list_memory_current = []
            bin_list_memory_peak = []
            for i in range(3):
                graph, start = generator(v, p)

                tracemalloc.start()
                fib_ti = time.time()
                dijkstra(graph, start, FibonacciHeap(v))
                fib_tf = time.time()
                fib_current, fib_peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                tracemalloc.start()
                bin_ti = time.time()
                dijkstra(graph, start, BinaryHeap(v))
                bin_tf = time.time()
                bin_current, bin_peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                bin_dt = bin_tf - bin_ti

                bin_list_k.append(bin_dt)
                bin_list_memory_current.append(bin_current)
                bin_list_memory_peak.append(bin_peak)

                
                
                fib_dt = fib_tf - fib_ti
                fib_list_k.append(fib_dt)
                fib_list_memory_current.append(fib_current)
                fib_list_memory_peak.append(fib_peak)
                

            fib_current_v[p] = {"time_mean": statistics.mean(fib_list_k),
                                "time_std": statistics.stdev(fib_list_k),
                                "memory_current_mean": statistics.mean(fib_list_memory_current),
                                "memory_current_std": statistics.stdev(fib_list_memory_current),
                                "memory_peak_mean": statistics.mean(fib_list_memory_peak),
                                "memory_peak_std": statistics.stdev(fib_list_memory_peak)}
            bin_current_v[p] = {"time_mean": statistics.mean(bin_list_k),
                                "time_std": statistics.stdev(bin_list_k),
                                "memory_current_mean": statistics.mean(bin_list_memory_current),
                                "memory_current_std": statistics.stdev(bin_list_memory_current),
                                "memory_peak_mean": statistics.mean(bin_list_memory_peak),
                                "memory_peak_std": statistics.stdev(bin_list_memory_peak)}
            print("[{}][V = {}][p = {}]".format(time.ctime(time.time()), v, p))
        out["fib"][v] = fib_current_v
        out["bin"][v] = bin_current_v
    return out
