# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import json

def p_visualization():

    exp_fp = open("experimentos/files/exp.json")
    exp = json.load(exp_fp)
    exp_fp.close()
    big_bin_times = exp["bin"]
    big_fib_times = exp["fib"]
    for v in big_bin_times:
        current_bin_times = big_bin_times[v]
        current_fib_times = big_fib_times[v]

        if int(v) < 1000:
            ylabel = "Tiempo (ms)"
            k = 1000
        else:
            ylabel = "Tiempo (s)"
            k = 1
        bin_t_mean = [float(current_bin_times[i]["time_mean"])*k for i in current_bin_times]
        bin_t_std = [float(current_bin_times[i]["time_std"])*k for i in current_bin_times]
        fib_t_mean = [float(current_fib_times[i]["time_mean"])*k for i in current_fib_times]
        fib_t_std = [float(current_fib_times[i]["time_std"])*k for i in current_fib_times]        
        plt.errorbar(current_bin_times.keys(), bin_t_mean, bin_t_std, fmt='--*',label="Montículo Binario")
        plt.errorbar(current_fib_times.keys(), fib_t_mean, fib_t_std, fmt='--*', label="Montículo de Fibonacci")
        plt.title("Tiempo de ejecución del algoritmo de Dijkstra\nen funcion de $\\rho$ dado |V| = {}".format(v))
        plt.xlabel("$\\rho$")
        
        plt.ylabel(ylabel)
        plt.legend()
        plt.savefig("experimentos/visualizaciones/[P][V={}].png".format(v))
        plt.close()

    
    