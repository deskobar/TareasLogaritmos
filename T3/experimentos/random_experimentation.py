from experimentos.file_module import generate_files_and_insert_to_bloom_filter, search_username_in_file
from src.bloom_filter import BloomFilter
from src.utils import get_k, get_correct_list, probability_falses_positives
from objsize import get_deep_size
import time, statistics, json


ITER = 3
N_RANGE = [2000, 5000, 10000, 15000, 20000]

output = {}
for big_n in N_RANGE:
    small_n = big_n / 2
    current_n = {}
    M_RANGE = [small_n/1000, small_n/100, small_n/50, small_n/10, small_n, small_n*2, small_n*3, small_n*4, small_n*5, small_n*6, small_n*7, small_n*8, small_n*9, small_n*10]
    for mxd in M_RANGE:
        m = int(mxd)
        search_times_bf = []
        search_times_fl = []
        initial_size_bf = []
        size_after_insertion_bf = []
        false_positives = [0] * ITER
        disk_access = [0] * ITER
        k = get_k(m, small_n)
        print(f'[STARTED AT] [{time.ctime(time.time())}] n: {big_n}, m: {m}, k: {k}')
        for i in range(ITER):
            bloom_filter = BloomFilter(m, k)
            initial_size_bf.append(get_deep_size(bloom_filter))
            bloom_filter, L_file, universe_file = generate_files_and_insert_to_bloom_filter(bloom_filter, big_n, small_n)
            size_after_insertion_bf.append(get_deep_size(bloom_filter))
            current_time_bf = []
            current_time_fl = []
            with open('experimentos/files/universe_file.txt', 'r') as universe_file:
                total_usernames_list = [w.strip('\n') for w in universe_file.readlines()]
                for username_query in total_usernames_list:
                    ti_bf = time.time()
                    username_might_be_in_file = bloom_filter.check(username_query)
                    tf_bf = time.time()
                    dt_bf = tf_bf - ti_bf
                    current_time_bf.append(dt_bf)
                    if username_might_be_in_file == 1:
                        disk_access[i] += 1
                        ti_fl = time.time()
                        username_in_file = search_username_in_file(username_query, 'experimentos/files/L_file.txt')
                        tf_fl = time.time() 
                        dt_fl = (tf_fl - ti_fl) * 19 
                        current_time_fl.append(dt_fl)
                        if username_in_file is None:
                            false_positives[i] += 1
            universe_file.close()
            search_times_fl.append(statistics.mean(get_correct_list(current_time_fl)))
            search_times_bf.append(statistics.mean(current_time_bf))
        print(f'[FINISHED] [{time.ctime(time.time())}] n: {big_n}, m: {m}, k: {k}')       
        mean_false_positives = statistics.mean(false_positives)
        mean_disk_access = statistics.mean(disk_access)
        current_n[m] = {
            'k_value': k,
            'm_value': m,
            'search_time_bf_total': sum(search_times_bf),
            'search_time_bf_mean': statistics.mean(search_times_bf),
            'search_time_bf_std': statistics.stdev(search_times_bf),
            'search_time_fl_total': sum(search_times_fl),
            'search_time_fl_mean': statistics.mean(search_times_fl),
            'search_time_fl_std': statistics.stdev(search_times_fl),
            'false_positives_total': sum(false_positives),
            'false_positives_mean': mean_false_positives,
            'false_positives_std': statistics.stdev(false_positives),
            'disk_access_total': sum(disk_access),
            'disk_access_mean': mean_disk_access,
            'disk_access_std': statistics.stdev(disk_access),
            'experimental_false_positives_percentage': mean_false_positives / (big_n - small_n) * 100.0,
            'theorical_false_positive_percentage': probability_falses_positives(m, small_n) * 100,
            'initial_size_bf_total': sum(initial_size_bf),
            'initial_size_bf_mean': statistics.mean(initial_size_bf),
            'initial_size_bf_std': statistics.stdev(initial_size_bf),
            'size_after_insertion_bf_total': sum(size_after_insertion_bf),
            'size_after_insertion_bf_mean': statistics.mean(size_after_insertion_bf),
            'size_after_insertion_bf_std': statistics.stdev(size_after_insertion_bf)
        }
    
    output[big_n] = current_n
    json_file = open('experimentos/files/new_results.json', 'w')
    json.dump(output, json_file)
    json_file.close()