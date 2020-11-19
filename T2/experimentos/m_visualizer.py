# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from src.utils import get_bin_v, get_fib_v, get_min_p

def m_visualization():
    
    bin_v = get_bin_v()
    fib_v = get_fib_v()
    p = get_min_p()
    bin_memory_mean = [float(bin_v[i]["memory_peak_mean"])*0.001024 for i in bin_v]
    fib_memory_mean = [float(fib_v[i]["memory_peak_mean"])*0.001024 for i in fib_v]
    plt.plot(bin_v.keys(), bin_memory_mean, '--*', label="bin")
    plt.plot(fib_v.keys(), fib_memory_mean, '--*', label="fib")
    plt.title("Peaks de consumo de memoria para el algoritmo de Dijkstra\npara |V| variable y $\\rho$={}".format(p))
    plt.xlabel("|V|")
    plt.ylabel("Cantidad de MB")
    plt.legend()
    plt.savefig("experimentos/visualizaciones/memory.png")
    plt.clf()

