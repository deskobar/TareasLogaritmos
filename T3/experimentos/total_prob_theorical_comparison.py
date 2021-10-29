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
    k_values = []
    theorical_prob_values = []
    x_range = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        theorical = int(current_results['theorical_false_positive_percentage'])/100
        theorical_prob_values.append(theorical)
    color = next(color_cycle)
    marker = next(marker_cycle)
    plt.plot(x_range, theorical_prob_values, '*', label=f'N = {small_n}', c=color, alpha=0.4, marker=marker)
plt.title(f"Probabilidad teórico de falsos positivos\n para N inserciones y 2N queries")
plt.xlabel('Valores de $\\rho$')
plt.ylabel('P(FP)')
plt.legend()
plt.savefig(f'experimentos/graph/prob/todes_theorical.png')
plt.clf()
plt.close()
