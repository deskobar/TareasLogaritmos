from math import log
import matplotlib.pyplot as plt

def bin_cost(V, p):
    return (V-1)*(1+1/2*p*(V-2))*log(V, 2)

def fib_cost(V, p):
    return V*log(V, 2) + (V - 1)*(1 + p/2*(V-2))

bin_cost_l = []
fib_cost_l = []
p = 1
x_range = range(10000000, 100000000000)
for i in x_range:
    bin_cost_l.append(bin_cost(i, p))
    fib_cost_l.append(fib_cost(i, p))

plt.plot(x_range, bin_cost_l, label="binary")
plt.plot(x_range, fib_cost_l, label="fib")
plt.legend()
plt.savefig("experimentos/visualizaciones/teorico.png")