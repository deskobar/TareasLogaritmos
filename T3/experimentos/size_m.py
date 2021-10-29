from src.utils import get_k, probability_falses_positives
import matplotlib.pyplot as plt

N = 1000
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
plt.savefig("experimentos/graph/theorical.png")
plt.close()