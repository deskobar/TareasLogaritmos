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
    theorical_prob_values = []
    experimental_prob_values = []
    x_range = []
    for m in results_n:
        x_range.append(int(m)/small_n)
        current_results  = results_n[m]
        k_values.append(current_results['k_value'])
        theorical_prob_values.append(current_results['theorical_false_positive_percentage'])
        experimental_prob_values.append(current_results['experimental_false_positives_percentage'])
    plt.plot(x_range, theorical_prob_values, label='teorico')
    plt.plot(x_range, experimental_prob_values, label='experimental')
    plt.title(f"P(FP) dada para n={small_n} inserciones")
    plt.xlabel('Valores de m')
    plt.ylabel('P(FP)')
    plt.legend()
    plt.savefig(f'experimentos/graph/[N={big_n}]lawea.png')
    plt.clf()
    plt.close()
