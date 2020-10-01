import statistics
from generator import generator
from binary_search import binary_search
import json
import time

MIN = 2
MAX = 26
P_LEN = "10000"
P_PATH = "P_test.txt"
T_LEN = "1000000"
T_PATH = "T_test.txt"

current_dict = {}

for k in range(MIN, MAX):
    tmp = []
    for current_k in range(k):
        generator(P_LEN, T_LEN)
        ti = time.time()
        binary_search(P_PATH, T_PATH)
        tf = time.time()
        dt = tf - ti
        tmp.append(dt)
    current_dict[k] = {"current_dict": sum(tmp), 
                       "promedio": statistics.mean(tmp),
                       "std": statistics.stdev(tmp)}

with open('experiment_for_k.json', 'w+') as fp:
    json.dump(current_dict, fp)
fp.close()
