# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import json

def m_visualization():
    bin_fp = open("experimentos/files/exp_bin.json")
    big_bin = json.load(bin_fp)
    bin_fp.close()

    fib_fp = open("experimentos/files/exp_fib.json")
    big_fib = json.load(fib_fp)
    fib_fp.close()
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

def p_visualization():

    

    for v in big_bin_p:
        bin_p = big_bin_p[v]
        fib_p = big_fib_p[v]
        bin_t_mean = [float(bin_p[i]["time_mean"]) for i in bin_p]
        bin_t_std = [float(bin_p[i]["time_std"]) for i in bin_p]
        fib_t_mean = [float(fib_p[i]["time_mean"]) for i in fib_p]
        fib_t_std = [float(fib_p[i]["time_std"]) for i in fib_p]

        plt.errorbar(bin_p.keys(), bin_t_mean, bin_t_std, fmt='--*',label="Montículo Binario")
        plt.errorbar(fib_p.keys(), fib_t_mean, fib_t_std, fmt='--*', label="Montículo de Fibonacci")
        plt.title("Tiempo de ejecución del algoritmo de Dijkstra\nen funcion de $\\rho$ dado |V| = {}".format(v))
        plt.xlabel("$\\rho$")
        plt.ylabel("Tiempo (s)")
        plt.legend()
        plt.savefig("experimentos/visualizaciones/[V={}]_p.png".format(v))
        plt.clf()