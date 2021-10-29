from src.utils import get_k, probability_falses_positives
import matplotlib.pyplot as plt
import json

fp = open('experimentos/files/results.json', 'r+')
results = json.load(fp)
fp.close()

for big_n in results:
    small_n = int(big_n)//2
    results_n = results[big_n]
    times_fl = []
    x_range = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        times_fl.append(current_results['search_time_fl_mean'])
    plt.plot(x_range, times_fl, label='experimental')
    plt.title(f"Tiempo para n={small_n} inserciones")
    plt.xlabel('Valores de $\\rho$')
    plt.ylabel('Tiempo (s)')
    plt.legend()
    plt.savefig(f'experimentos/graph/time_fl/{small_n}.png')
    plt.clf()
    plt.close()
