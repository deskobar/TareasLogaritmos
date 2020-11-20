# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import json

def m_visualization():
    exp_fp = open("experimentos/files/exp.json")
    exp = json.load(exp_fp)
    exp_fp.close()
    big_bin = exp["bin"]
    big_fib = exp["fib"]
    for v in big_fib:
        bin_v = big_bin[v]
        fib_v = big_fib[v]
        bin_memory_mean = [float(bin_v[i]["memory_peak_mean"])*0.001024 for i in bin_v]
        fib_memory_mean = [float(fib_v[i]["memory_peak_mean"])*0.001024 for i in fib_v]
        plt.plot(bin_v.keys(), bin_memory_mean, '--*', label="Montículo Binario")
        plt.plot(fib_v.keys(), fib_memory_mean, '--*', label="Montículo de Fibonacci")
        plt.title("Peaks de consumo de memoria para el algoritmo de Dijkstra\npara |V| = {} y $\\rho$ variable".format(v))
        plt.xlabel("$\\rho$")
        plt.ylabel("Cantidad de MB")
        plt.legend()
        plt.savefig("experimentos/visualizaciones/[M][V={}].png".format(v))
        plt.close()
