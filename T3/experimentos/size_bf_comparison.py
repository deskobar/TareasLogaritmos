from src.utils import get_k, probability_falses_positives
import matplotlib.pyplot as plt
import json

fp = open('experimentos/files/results.json', 'r+')
results = json.load(fp)
fp.close()

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
        sizes.append(current_results['initial_size_bf_mean'])
    plt.scatter(x_range, sizes, label='Tamaño del BF')#, s=[50*k for k in sizes])
    plt.title(f"Sizes del Bloom Filter dado m y n={small_n} inserciones, k teórico")
    plt.xlabel('Valores de $\\rho$')
    plt.ylabel('Tamaño del Bloom Filter (Bytes)')
    plt.legend()
    plt.savefig(f'experimentos/graph/[N={big_n}]sizes.png')
    plt.close()
