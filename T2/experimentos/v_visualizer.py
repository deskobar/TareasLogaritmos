# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt

# Binary
bin_fp = open("experimentos/files/find_v_bin.json")
bin_v = json.load(bin_fp)
bin_fp.close()
bin_t_mean = [float(bin_v[i]["time_mean"]) for i in bin_v]
bin_t_std = [float(bin_v[i]["time_std"]) for i in bin_v]

# Fibonacci
fib_fp = open("experimentos/files/find_v_fib.json")
fib_v = json.load(fib_fp)
fib_fp.close()
fib_t_mean = [float(fib_v[i]["time_mean"]) for i in fib_v]
fib_t_std = [float(fib_v[i]["time_std"]) for i in fib_v]


plt.errorbar(bin_v.keys(), bin_t_mean, bin_t_std, label="bin")
plt.errorbar(fib_v.keys(), fib_t_mean, fib_t_std, label="fib")
plt.title("Grafico que muestra V en funcion de p dado V = 100")
plt.legend()
plt.savefig("experimentos/visualizaciones/v.png")

min = 1e9
index = -1
for i in fib_v.keys():
    current = float(fib_v[i]["time_std"]) + float(bin_v[i]["time_std"])
    if current < min:
        min = current
        index = i
print(index)
