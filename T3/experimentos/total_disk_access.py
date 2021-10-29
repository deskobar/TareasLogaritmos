from src.utils import get_theorical_disk_access
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
    experimental_disk_acces = []
    x_range = []
    theorical_disk_access = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        corrected_experimental_disk_access = int(current_results['disk_access_mean']) / 10**FACTOR
        experimental_disk_acces.append(corrected_experimental_disk_access)
    more_m = [small_n/1e3] + [small_n*i*10/small_n for i in range(1, small_n+1)]
    more_p = []
    for m in more_m:
        more_p.append(m/small_n)
        current_theorical_disk_access = get_theorical_disk_access(int(m), small_n, int(big_n))
        corrected_theorical_disk_access = current_theorical_disk_access / 10**FACTOR
        theorical_disk_access.append(corrected_theorical_disk_access)
    color = next(color_cycle)
    plt.plot(more_p, theorical_disk_access, label=f'N = {small_n}', c=color)
    plt.plot(x_range, experimental_disk_acces, '*', c=color)


plt.title(f"Cantidad experimental de accesos a disco contrastada\n con la teoría para N inserciones y 2N queries")
plt.xlabel('Valores de $\\rho$')
plt.ylabel(f'# de accesos (10^{FACTOR})')
plt.legend()
plt.savefig(f'experimentos/graph/disk_access/todes.png')
plt.clf()
plt.close()
