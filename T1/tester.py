import statistics
from generator import generator
from binary_search import binary_search
import json
import time

N   = 3
MIN = 2
MAX = 26

final_dict = {}
for i in range(N):
    current_dict = {}
    for k in range(MIN, MAX):
        tmp = []
        for current_k in range(k):
            generator("10000", "1000000")
            ti = time.time()
            binary_search("P_test.txt", "T_test.txt")
            tf = time.time()
            dt = tf - ti
            tmp.append(dt)
        current_dict[k] = {"current_dict": sum(tmp), 
                           "promedio": statistics.mean(tmp),
                           "std": statistics.stdev(tmp)}
    final_dict[str(i)] = current_dict 

with open('exp_bsearch.json', 'w+') as fp:
    json.dump(final_dict, fp)
fp.close()
