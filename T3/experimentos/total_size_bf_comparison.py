from src.utils import get_k, probability_falses_positives
import matplotlib.pyplot as plt
import json
from itertools import cycle
color_cycle = cycle(['g', 'b', 'c', 'm', 'y', 'k'])

fp = open('experimentos/files/results.json', 'r+')
results = json.load(fp)
fp.close()
FACTOR = 4
for big_n in results:
    small_n = int(big_n)//2
    results_n = results[big_n]
    k_values = []
    sizes = []
    x_range = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        k_values.append(current_results['k_value'])
        corrected_value = int(current_results['initial_size_bf_mean']) / 10**FACTOR
        sizes.append(corrected_value)
    color = next(color_cycle)
    plt.plot(x_range, sizes, '--*',  label=f'N = {small_n}', c=color)
plt.title(f"Tamaño del Filtro de Bloom dado distintos N y k = $\\lceil$$\\rho$*ln(2)$\\rceil$")
plt.xlabel('Valores de $\\rho$')
plt.ylabel(f'Tamaño (10^{FACTOR} bytes)')
plt.legend()
plt.savefig(f'experimentos/graph/size/todes.png')
plt.close()
