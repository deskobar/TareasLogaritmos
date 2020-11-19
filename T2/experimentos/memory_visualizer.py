# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt

# Binary
bin_fp = open("experimentos/files/find_v_bin.json")
bin_v = json.load(bin_fp)
bin_fp.close()
bin_memory_mean = [float(bin_v[i]["memory_peak_mean"]) for i in bin_v]
bin_memory_std = [float(bin_v[i]["memory_peak_std"]) for i in bin_v]

# Fibonacci
fib_fp = open("experimentos/files/find_v_fib.json")
fib_v = json.load(fib_fp)
fib_fp.close()
fib_memory_mean = [float(fib_v[i]["memory_peak_mean"]) for i in fib_v]
fib_memory_std = [float(fib_v[i]["memory_peak_std"]) for i in fib_v]


plt.errorbar(bin_v.keys(), bin_memory_mean, bin_memory_std, label="bin")
plt.errorbar(fib_v.keys(), fib_memory_mean, fib_memory_std, label="fib")
plt.title("Grafico que muestra el consumo de memoria en funcion de V dado p")
plt.legend()
plt.savefig("experimentos/visualizaciones/memory.png")

