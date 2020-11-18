import time
from src.generator_base import generator
from src.priorityQueue import BinaryHeap#, FibonacciHeap
from src.otherQueue import aFibonacciHeap as FibonacciHeap
from src.dijkstra_base import dijkstra

MIN = 2
MAX = 26
v = 90
super_dict = {}
p_range = [p/10 for p in range(1, 11)]
v_range = range(1, 1000, 10)
"""
FIJAR V Y PROBAR CON DIFERENTES P
"""
def find_p_fib():
    fib_dict = {}
    for i in range(3):
        current_fib_dict = {}
        for k in range(MIN, MAX):
            p_values_fibonacci = {}
            for p in p_range:
                graph, start = generator(v, p)
                ti_fibo = time.time()
                dijkstra(graph, start, FibonacciHeap(v))                
                tf_fibo = time.time()
                dt_fibo = tf_fibo - ti_fibo
                p_values_fibonacci[p] = dt_fibo
            current_fib_dict[k] = p_values_fibonacci
        fib_dict[i] = current_fib_dict
    return fib_dict

def find_p_bin():
    bin_dict = {}
    for i in range(3):
        current_bin_dict = {}
        for k in range(MIN, MAX):
            p_values_binary = {}
            for p in p_range:
                graph, start = generator(v, p)
                ti_binary = time.time()
                dijkstra(graph, start, BinaryHeap(v))
                tf_binary = time.time()
                dt_binary = tf_binary - ti_binary
                p_values_binary[p] = dt_binary
            current_bin_dict[k] = p_values_binary
        bin_dict[i] = current_bin_dict
    return bin_dict

"""
FIJAR P Y PROBAR CON DIFERENTES V
"""

def find_V_fib(p):
    fib_dict = {}
    for i in range(3):
        current_fib_dict = {}
        for k in range(MIN, MAX):
            p_values_fibonacci = {}
            for v in v_range:
                graph, start = generator(v, p)
                ti_fibo = time.time()
                dijkstra(graph, start, FibonacciHeap(v))
                tf_fibo = time.time()
                dt_fibo = tf_fibo - ti_fibo
                p_values_fibonacci[p] = dt_fibo
            current_fib_dict[k] = p_values_fibonacci
        fib_dict[i] = current_fib_dict
    return fib_dict

def find_V_bin(p):
    bin_dict = {}
    for i in range(3):
        current_bin_dict = {}
        for k in range(MIN, MAX):
            p_values_binary = {}
            for v in v_range:
                graph, start = generator(v, p)
                ti_binary = time.time()
                dijkstra(graph, start, BinaryHeap(v))
                tf_binary = time.time()
                dt_binary = tf_binary - ti_binary
                p_values_binary[p] = dt_binary
            current_bin_dict[k] = p_values_binary
        bin_dict[i] = current_bin_dict
    return bin_dict

