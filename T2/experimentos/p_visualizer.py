# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from src.utils import get_bin_p, get_fib_p

def p_visualization(V):

    bin_p = get_bin_p()
    fib_p = get_fib_p()

    bin_t_mean = [float(bin_p[i]["time_mean"]) for i in bin_p]
    bin_t_std = [float(bin_p[i]["time_std"]) for i in bin_p]
    fib_t_mean = [float(fib_p[i]["time_mean"]) for i in fib_p]
    fib_t_std = [float(fib_p[i]["time_std"]) for i in fib_p]

    plt.errorbar(bin_p.keys(), bin_t_mean, bin_t_std, fmt='--^',label="bin")
    plt.errorbar(fib_p.keys(), fib_t_mean, fib_t_std, fmt='--^', label="fib")
    plt.title("Tiempo de ejecución del algoritmo de Dijkstra\nen funcion de $\\rho$ dado |V| = {}".format(V))
    plt.xlabel("$\\rho$")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.savefig("experimentos/visualizaciones/p.png")
    plt.clf()