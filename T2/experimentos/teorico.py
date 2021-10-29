from math import log
import matplotlib.pyplot as plt

def bin_cost(V, p):
    return p*V**2*log(V, 2) + V*log(V, 2)

def fib_cost(V, p):
    return p*V**2 + V*log(V, 2)

v_range = [10, 50, 100, 500, 1000, 5000, 7500, 10000]
p_range = [p/10 for p in range(0, 11)]

for v in v_range:
    bin_cost_l = []
    fib_cost_l = []
    for p in p_range: 
        bin_cost_l.append(bin_cost(v, p))
        fib_cost_l.append(fib_cost(v, p))
    plt.plot(p_range, bin_cost_l, label="Montículo binario")
    plt.plot(p_range, fib_cost_l, label="Montículo de Fibonacci")
    plt.title("Proyección teórica de los costos para el algoritmo de Dijkstra\ndado |V| = {} y $\\rho$ variable".format(v))
    plt.xlabel("$\\rho$")
    plt.ylabel("")
    plt.legend()
    plt.savefig("experimentos/visualizaciones/teoria/[T][V={}].png".format(v))
    plt.close()

