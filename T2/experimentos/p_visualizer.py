# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt

# Binary
bin_fp = open("experimentos/files/find_p_bin.json")
bin_p = json.load(bin_fp)
bin_fp.close()
bin_t_mean = [float(bin_p[i]["time_mean"]) for i in bin_p]
bin_t_std = [float(bin_p[i]["time_std"]) for i in bin_p]

# Fibonacci
fib_fp = open("experimentos/files/find_p_fib.json")
fib_p = json.load(fib_fp)
fib_fp.close()
fib_t_mean = [float(fib_p[i]["time_mean"]) for i in fib_p]
fib_t_std = [float(fib_p[i]["time_std"]) for i in fib_p]


plt.errorbar(bin_p.keys(), bin_t_mean, bin_t_std, label="bin")
plt.errorbar(fib_p.keys(), fib_t_mean, fib_t_std, label="fib")
plt.title("Grafico que muestra t en funcion de P dado V=100")
plt.legend()
plt.savefig("experimentos/visualizaciones/p.png")

min = 1e9
index = -1
for i in fib_p.keys():
    current = float(fib_p[i]["time_std"]) + float(bin_p[i]["time_std"])
    if current < min:
        min = current
        index = i
print(index)
