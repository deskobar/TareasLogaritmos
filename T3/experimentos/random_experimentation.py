"""
Metodo:

1. Recibo entero n, inserto los strings tanto a un fb como a un archivo L
2. Programar un módulo que busca en el archivo L; las palabras que pasan el filtro
3. Para buscar use grep
4. Entonces me debo fijar un N grande, decir cuanto será n < N (en primera instancia n = N/2)
"""
import sys
from src.bloom_filter import BloomFilter
from math import log, ceil
import json
import time
import statistics
import tracemalloc
from experimentos.file_module import generate_files_and_bloom_filter, search_username_in_file

ITER = 3
N_RANGE = [100000]

def get_m(n, p):
    m = -n * log(p) / log(2)**2
    return m

def get_k(m, n):
    k = m * log(2) / n
    return k

output = {}
for big_n in N_RANGE:
    small_n = big_n / 2
    current_n = {}
    for prob in range(1, 11):
        p = prob / 10
        search_total_time_bf = []
        search_mean_time_bf = []
        search_std_time_bf = []
        search_total_time_fl = []
        search_mean_time_fl = []
        search_std_time_fl = []
        total_false_positives = []
        total_disk_access = []
        for i in range(ITER):
            m = ceil(get_m(small_n, p))
            k = ceil(get_k(m, big_n))
            bloom_filter, L_file, universe_file = generate_files_and_bloom_filter(m, k, big_n, small_n)
            false_positives = 0
            disk_access = 0
            search_times_bf = []
            search_times_fl = []
            with open('universe_file.txt', 'r') as universe_file:
                total_usernames_list = universe_file.readlines()
                for username_query in total_usernames_list:
                    ti_bf = time.time()
                    username_might_be_in_file = bloom_filter.check(username_query)
                    tf_bf = time.time()
                    dt_bf = tf_bf - ti_bf
                    search_times_bf.append(dt_bf)
                    print('big n: {}, prob: {}, iteration: {}'.format(big_n, p, i))
                    if username_might_be_in_file:
                        disk_access += 1
                        ti_fl = time.time()
                        username_in_file = search_username_in_file(username_query, L_file)
                        tf_fl = time.time()
                        dt_fl = tf_fl - ti_fl
                        search_times_fl.append(dt_fl)
                        if not username_in_file:
                            false_positives += 1
            universe_file.close()
            search_total_time_bf.append(sum(search_times_bf))
            search_mean_time_bf.append(statistics.mean(search_times_bf))
            search_std_time_bf.append(statistics.stdev(search_times_bf))
            search_total_time_fl.append(sum(search_times_fl))
            search_mean_time_fl.append(statistics.mean(search_times_fl))
            search_std_time_fl.append(statistics.stdev(search_times_fl))
            total_false_positives.append(false_positives)
            total_disk_access.append(disk_access)
        current_n[p] = {
            'search_total_time_bf': statistics.mean(search_total_time_bf),
            'search_mean_time_bf': statistics.mean(search_mean_time_bf),
            'search_std_time_bf': statistics.mean(search_std_time_bf),
            'search_total_time_fl': statistics.mean(search_total_time_fl),
            'search_mean_time_fl': statistics.mean(search_mean_time_fl),
            'search_std_time_fl': statistics.mean(search_std_time_fl),
            'false_positives': statistics.mean(total_false_positives),
            'disk_access': statistics.mean(total_disk_access)
        }
    output[big_n] = current_n
                
with open('results.json', 'w') as json_file:
    json.dump(output, json_file)
json_file.close()