import matplotlib.pyplot as plt
from src.utils import probability_falses_positives
from itertools import cycle
color_cycle = cycle(['g', 'b', 'c', 'm', 'y', 'k'])


small_n = 10000
results_n = [small_n/1e3] + [small_n*i*10/small_n for i in range(1, small_n+1)]
k_values = []
theorical_prob_values = []
x_range = []
for mxd in results_n:
    m = mxd
    x_range.append(int(m)/small_n)
    theorical = probability_falses_positives(m, small_n)
    theorical_prob_values.append(theorical)
color = next(color_cycle)
plt.plot(x_range, theorical_prob_values, c=color)
plt.title(f"Probabilidad teórico de falsos positivos\npara N = {small_n} dado $\\rho$ = m/N")
plt.xlabel('Valores de $\\rho$')
plt.ylabel('P(FP)')
#plt.legend()
plt.savefig(f'experimentos/graph/prob/lado_derecho.png')
plt.clf()
plt.close()
