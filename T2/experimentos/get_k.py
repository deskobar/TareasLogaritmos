import statistics
import time

MIN = 2
MAX = 5
super_dict = {}
for i in range(3):
    current_dict = {}
    for k in range(MIN, MAX):
        current_dates = []
        for t in range(k):
            ti = time.time()
            #executeDijkstra
            tf = time.time()
            dt = tf - ti
            current_dates.append(dt)
        current_dict[k] = {
            'total_time': sum(current_dates),
            'time_mean': statistics.mean(current_dates),
            'time_std': statistics.stdev(current_dates)
        }
    super_dict[str(i)] = current_dict
print(super_dict)

"""
DICCIONARIO = {
    0: {}
    1: {}
    2: {}
}

"""