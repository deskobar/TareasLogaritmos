import statistics
from experimentation.generator import generator
from algorithms.binary_search import binary_search
from algorithms.linear_search import linear_search
from algorithms.indexed_search import indexed_search
from algorithms.linear_search_plus_binary import linear_search_plus_binary
from algorithms.linear_search_plus_merge import linear_search_plus_merge
from datetime import datetime
import json
import time

"""
SE DEBE LLAMAR DESDE T1 DE LA SIGUIENTE FORMA
python -m experimentation.tester P.txt T.txt
"""
MAX = 14
#P_LEN = '10000'
P_PATH = 'input_files/P.txt'
T_PATH = 'input_files/T.txt'
P_LEN = 10000
T_LENS = [10**6, 10**7, 1.12*10**7, 1.15*10**7, 1.18*10**7, 1.5*10**7]
T_LENS.sort()
#algorithms = [binary_search, linear_search, indexed_search, linear_search_plus_binary, linear_search_plus_merge]

# done: binary, indexed, linear_binary
algorithms = [linear_search]
for algorithm in algorithms:
    algorithm_dict = {}
    for T_LEN in T_LENS:    
        input_tmp = []
        output_tmp = []
        time_tmp = []
        current_dict = {}
        for current_k in range(MAX):
            generator(P_LEN, int(T_LEN))
            ti = time.time()
            reads, writes = algorithm(P_PATH, T_PATH)
            tf = time.time()
            dt = tf - ti
            input_tmp.append(reads)
            output_tmp.append(writes)
            time_tmp.append(dt)
            current_dict[current_k] = {
                'Input': reads,
                'Output': writes,
                'I/Os': reads+writes,
                'time': dt  
            }
            # [19.00.12][LINEAR_SEARCH][10**9][K=10]
            msg = '[{}][{}][{}][K={}] DONE'.format(datetime.now().time(), algorithm.__name__.upper(), T_LEN, current_k)
            print(msg)
        algorithm_dict[int(T_LEN)] = current_dict
    # quiero que se guarde como nombre algoritmo        
    file_name = 'output_exp/{}.json'.format(algorithm.__name__)
    with open(file_name, 'w+') as fp:
        json.dump(algorithm_dict, fp)
    fp.close()

"""
Quiero que se guarde asi:
nombre algoritmo = {valor de T: {input, output, i/o, time}}
"""