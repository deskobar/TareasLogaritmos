# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import json

def m_visualization():
    exp_fp = open("experimentos/files/exp.json")
    exp = json.load(exp_fp)
    exp_fp.close()
    big_memory_bin = exp["bin"]
    big_memory_fib = exp["fib"]
    for v in big_memory_fib:
        memory_bin = big_memory_bin[v]
        memory_fib = big_memory_fib[v]
        bin_memory_mean = [float(memory_bin[i]["memory_peak_mean"])*0.001024 for i in memory_bin]
        fib_memory_mean = [float(memory_fib[i]["memory_peak_mean"])*0.001024 for i in memory_fib]
        plt.plot(memory_bin.keys(), bin_memory_mean, '--*', label="Montículo Binario")
        plt.plot(memory_fib.keys(), fib_memory_mean, '--*', label="Montículo de Fibonacci")
        plt.title("Peaks de consumo de memoria para el algoritmo de Dijkstra\npara |V| = {} y $\\rho$ variable".format(v))
        plt.xlabel("$\\rho$")
        plt.ylabel("Cantidad de MB")
        plt.yticks(range(0, 4000, 500))
        plt.legend()
        plt.savefig("experimentos/visualizaciones/[M][V={}].png".format(v))
        plt.close()
