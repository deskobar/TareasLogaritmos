from src.utils import get_k, probability_falses_positives
import matplotlib.pyplot as plt
import json
from itertools import cycle
color_cycle = cycle(['g', 'b', 'c', 'm', 'y', 'k'])
marker_cycle = cycle(['v', '^', '<', '>', '8', 'p'])

fp = open('experimentos/files/results.json', 'r+')
results = json.load(fp)
fp.close()

for big_n in results:
    small_n = int(big_n)//2
    results_n = results[big_n]
    more_m = [small_n/1e3] + [small_n*i*10/small_n for i in range(1, small_n+1)]
    k_values = []
    experimental_prob_values = []
    theorical_prob_values = []
    x_range = []
    more_p = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        k_values.append(current_results['k_value'])
        experimental = int(current_results['false_positives_mean'])/(int(big_n)  - small_n)
        experimental_prob_values.append(experimental)    
    for m in more_m:
        more_p.append(m/small_n)
        current_theorical_fp = probability_falses_positives(m, small_n)
        theorical_prob_values.append(current_theorical_fp)
    color = next(color_cycle)
    marker = next(marker_cycle)
    plt.plot(more_p, theorical_prob_values, alpha=0.4, c=color)
    plt.plot(x_range, experimental_prob_values, '*',  label=f'N = {small_n}', c=color, alpha=0.4, marker=marker)
plt.title(f"Probabilidad experimental de falsos positivos\n para N inserciones y 2N queries")
plt.xlabel('Valores de $\\rho$')
plt.ylabel('P(FP)')
plt.legend()
plt.savefig(f'experimentos/graph/prob/todes_experimental.png')
plt.clf()
plt.close()
