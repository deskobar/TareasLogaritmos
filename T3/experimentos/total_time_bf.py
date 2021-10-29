from src.utils import get_k, probability_falses_positives
import matplotlib.pyplot as plt
import json
from itertools import cycle
color_cycle = cycle(['g', 'b', 'c', 'm', 'y', 'k'])

fp = open('experimentos/files/results.json', 'r+')
results = json.load(fp)
fp.close()

FACTOR = 5
for big_n in results:
    small_n = int(big_n)//2
    results_n = results[big_n]
    times_bf = []
    x_range = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        corrected_time = float(current_results['search_time_bf_mean']) * 10**FACTOR
        times_bf.append(corrected_time)
    color = next(color_cycle)
    plt.plot(x_range, times_bf, '--*', label=f'N = {small_n}', c=color)
plt.title(f"Tiempo de búsqueda promedio en memoria para el\nFiltro de Bloom para N inserciones y 2N queries")
plt.xlabel('Valores de $\\rho$')
plt.ylabel(f'Tiempo (10^-{FACTOR} s)')
plt.legend()
plt.savefig(f'experimentos/graph/time_bf/todes.png')
plt.clf()
plt.close()
