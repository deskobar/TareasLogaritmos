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
MAX = 10
#P_LEN = '10000'
P_PATH = 'input_files/P.txt'
T_LEN = '1000000'
T_PATH = 'input_files/T.txt'
P_LENS = [10, 100, 1000, 100000] # '10000' ya fue evaluado
current_dict = {}
#algorithms = [binary_search, linear_search, indexed_search, linear_search_plus_binary, linear_search_plus_merge]
algorithms = [linear_search]
for P_LEN in P_LENS:
    for algorithm in algorithms:
        input_tmp = []
        output_tmp = []
        time_tmp = []
        for current_k in range(MAX):
            generator(P_LEN, T_LEN)
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
            msg = '[{}][K = {}] DONE'.format(algorithm.__name__.upper(), str(current_k).zfill(2))
            print(msg)
        file_name = 'output_exp/[#rep={}][P={}] {}.json'.format(str(10), P_LEN, algorithm.__name__)
        with open(file_name, 'w+') as fp:
            json.dump(current_dict, fp)
        fp.close()
