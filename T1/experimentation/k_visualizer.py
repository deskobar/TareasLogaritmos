import matplotlib.pyplot as plt
import json

fp = open('output_exp/experiment_for_k_binary_search.json')
data = json.load(fp)
fp.close()

k_range = list(range(2,26))
io_total = []
io_mean = []
io_std = []
t_total = []
t_mean = []
t_std = []
for k in k_range:
    current_dict = data[str(k)]
    io_total.append(current_dict["I/Os_sum"])
    io_mean.append(current_dict["I/Os_mean"])
    io_std.append(current_dict["I/Os_std"])
    t_total.append(current_dict["time_sum"])
    t_mean.append(current_dict["time_mean"])
    t_std.append(current_dict["time_std"])

plt.errorbar(k_range, io_mean, io_std, fmt='o', color='black', ecolor='lightgray')
plt.title("Cantidad de I/Os para los k experimentos de Búsqueda Binaria")
plt.xlabel("Cantidad k de repeticiones del experimento")
plt.ylabel("Promedio I/Os")
plt.savefig("visualizations/std_para_k")
plt.show()