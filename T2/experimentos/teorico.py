from math import log
import matplotlib.pyplot as plt

def bin_cost(V, p):
    return p*V**2*log(V, 2) + V*log(V, 2)

def fib_cost(V, p):
    return p*V**2 + V*log(V, 2)

bin_cost_l = []
fib_cost_l = []
p = 1
x_range = list(range(0, 10001, 1000))
x_range[0] = 1
for i in x_range:
    bin_cost_l.append(bin_cost(i, p))
    fib_cost_l.append(fib_cost(i, p))

plt.plot(x_range, bin_cost_l, label="binary")
plt.plot(x_range, fib_cost_l, label="fib")
plt.title("Hola ma!")
plt.legend()
plt.savefig("experimentos/visualizaciones/teorico.png")