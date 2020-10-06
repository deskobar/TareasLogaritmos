import statistics
from experimentation.generator import generator
from algorithms_implementation.binary_search import binary_search
from algorithms_implementation.linear_search import linear_search
from algorithms_implementation.indexed_search import indexed_search
from algorithms_implementation.linear_search_plus_binary import linear_search_plus_binary
from algorithms_implementation.linear_search_plus_merge import linear_search_plus_merge
import json
import time

MIN = 2
MAX = 26
P_LEN = '10000'
P_PATH = 'P_test.txt'
T_LEN = '1000000'
T_PATH = 'T_test.txt'

current_dict = {}
algorithms = [binary_search, linear_search, indexed_search, linear_search_plus_binary, linear_search_plus_merge]

for algorithm in algorithms:
    for k in range(MIN, MAX):
        memory_accesses_tmp = []
        time_tmp = []
        for current_k in range(k):
            generator(P_LEN, T_LEN)
            ti = time.time()
            memory_accesses = algorithm(P_PATH, T_PATH)
            tf = time.time()
            dt = tf - ti
            memory_accesses_tmp.append(memory_accesses)
            time_tmp.append(dt)
        current_dict[k] = {
            'I/Os_sum': sum(memory_accesses_tmp),
            'I/Os_mean': statistics.mean(memory_accesses_tmp),
            'I/Os_std': statistics.stdev(memory_accesses_tmp),
            'time_sum': sum(time_tmp), 
            'time_mean': statistics.mean(time_tmp),
            'time_std': statistics.stdev(time_tmp),
        }
        msg = '[K = {}] DONE'.format(str(k))
        print(msg)
    file_name = 'experiment_for_k_{}.json'.format(algorithm)
    with open(file_name, 'w+') as fp:
        json.dump(current_dict, fp)
    fp.close()
