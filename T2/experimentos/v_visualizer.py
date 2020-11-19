# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from src.utils import get_bin_v, get_fib_v, get_min_p

def v_visualization():

    bin_v = get_bin_v()
    fib_v = get_fib_v()
    p = get_min_p()
    bin_t_mean = [float(bin_v[i]["time_mean"]) for i in bin_v]
    bin_t_std = [float(bin_v[i]["time_std"]) for i in bin_v]
    fib_t_mean = [float(fib_v[i]["time_mean"]) for i in fib_v]
    fib_t_std = [float(fib_v[i]["time_std"]) for i in fib_v]

    plt.errorbar(bin_v.keys(), bin_t_mean, bin_t_std, label="bin")
    plt.errorbar(fib_v.keys(), fib_t_mean, fib_t_std, label="fib")
    plt.title("Tiempos de ejecución del algoritmo de Dijkstra\nen funcion de |V| variable y $\\rho$ = {}".format(p))
    plt.xlabel("|V|")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.savefig("experimentos/visualizaciones/v.png")
    plt.clf()

