import statistics
from experimentation.generator import generator
from algorithms.binary_search import binary_search
from algorithms.linear_search import linear_search
from algorithms.indexed_search import indexed_search
from algorithms.linear_search_plus_binary import linear_search_plus_binary
from algorithms.linear_search_plus_merge import linear_search_plus_merge
import json
import time

"""
SE DEBE LLAMAR DESDE T1 DE LA SIGUIENTE FORMA
python -m experimentation.tester P.txt T.txt
"""
MIN = 2
MAX = 26
N = 3
P_LEN = '10000'
P_PATH = 'input_files/P.txt'
T_LEN = '1000000'
T_PATH = 'input_files/T.txt'

algorithms = [binary_search]
final_dict = {}
for n in range(N):
    current_dict = {}
    for algorithm in algorithms:
        for k in range(MIN, MAX):
            input_tmp = []
            output_tmp = []
            io_tmp = []
            time_tmp = []
            for current_k in range(k):
                generator(P_LEN, T_LEN)
                ti = time.time()
                reads, writes = algorithm(P_PATH, T_PATH)
                tf = time.time()
                dt = tf - ti
                input_tmp.append(reads)
                output_tmp.append(writes)
                io_tmp.append(reads+writes)
                time_tmp.append(dt)
            current_dict[k] = {
                'Input_sum': sum(input_tmp),
                'Input_mean': statistics.mean(input_tmp),
                'Input_sted': statistics.stdev(input_tmp),
                'Output_sum': sum(output_tmp),
                'Output_mean': statistics.mean(output_tmp),
                'Output_std': statistics.stdev(output_tmp), 
                'I/Os_sum': sum(io_tmp),
                'I/Os_mean': statistics.mean(io_tmp),
                'I/Os_std': statistics.stdev(io_tmp),
                'time_sum': sum(time_tmp), 
                'time_mean': statistics.mean(time_tmp),
                'time_std': statistics.stdev(time_tmp),
            }
            msg = '[N = {}][{}][K = {}] DONE'.format(n, algorithm.__name__.upper(), str(k))
            print(msg)
    final_dict[str(n)] = current_dict
file_name = 'output_exp/final_experiment_for_k_{}_n_{}.json'.format(algorithm.__name__, N)
with open(file_name, 'w+') as fp:
    json.dump(final_dict, fp)
fp.close()
