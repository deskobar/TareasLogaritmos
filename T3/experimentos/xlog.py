import matplotlib.pyplot as plt
from math import log, ceil

N = 1000

def m_size(p):
    m = -N*log(p)/log(2)**2
    return m

def get_k(m, n):
    k = m*log(2)/n
    return k

def probability_falses_positives(m, n):
    k = ceil(get_k(m, n))
    p = (1 - (1 - 1/m)**(k*n))**k
    return p

"""
Dado un N fijo, veamos como se comportará la probabilidad en función de m
"""

BASE = 1000

probability_output = []
idk = []
m_range = range(1, 10*BASE)
for i in m_range:
    probability_output.append(probability_falses_positives(i, BASE))
    idk.append((1/2)**get_k(i, BASE))

plt.plot(m_range, probability_output, color='r')
plt.plot(m_range, idk, color='b')
plt.title(f"P(FP) dado N={BASE}")
plt.xlabel("Valores de M")
plt.ylabel("P(FP)")
plt.savefig("hola")
plt.close()