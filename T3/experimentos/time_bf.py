from src.utils import get_k, probability_falses_positives
import matplotlib.pyplot as plt
import json

fp = open('experimentos/files/results.json', 'r+')
results = json.load(fp)
fp.close()

for big_n in results:
    small_n = int(big_n)//2
    results_n = results[big_n]
    times_bf = []
    x_range = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        times_bf.append(current_results['search_time_bf_mean'])
    plt.plot(x_range, times_bf, label='Tiempo de búsqueda en BF')
    plt.title(f"Tiempo para n={small_n} inserciones")
    plt.xlabel('Valores de $\\rho$')
    plt.ylabel('Tiempo (s)')
    plt.legend()
    plt.savefig(f'experimentos/graph/time_bf/{small_n}.png')
    plt.clf()
    plt.close()
