# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import json

def p_visualization():

    exp_fp = open("experimentos/files/exp.json")
    exp = json.load(exp_fp)
    exp_fp.close()
    big_bin_p = exp["bin"]
    big_fib_p = exp["fib"]
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
        plt.savefig("experimentos/visualizaciones/[P][V={}].png".format(v))
        plt.close()

    
    