import matplotlib.pyplot as plt
import json
import statistics

fp = open('output_exp/final_experiment_for_k_binary_search_n_3.json')
data = json.load(fp)
fp.close()
n_range = list(range(3))
k_range = list(range(2,26))
playable_io_total = []
playable_io_mean = []
playable_io_std = []
playable_t_total = []
playable_t_mean = []
playable_t_std = []
for k in list(range(2,26)):
    current_io_total = []
    current_io_mean = []
    current_io_std = []
    current_t_total = []
    current_t_mean = []
    current_t_std = []
    for n in list(range(3)):
        print(n)
        my_dict = data[str(n)][str(k)]
        current_io_total.append(my_dict["I/Os_sum"])
        current_io_mean.append(my_dict["I/Os_mean"])
        current_io_std.append(my_dict["I/Os_std"])
        current_t_total.append(my_dict["time_sum"])
        current_t_mean.append(my_dict["time_mean"])
        current_t_std.append(my_dict["time_std"])
    print("LINE = {} STD = {}".format(current_io_total, statistics.stdev(current_io_total)))
    playable_io_total.append(statistics.mean(current_io_total))
    playable_io_mean.append(statistics.mean(current_io_mean))
    playable_io_std.append(statistics.mean(current_io_std))
    playable_t_total.append(statistics.mean(current_t_total))
    playable_t_mean.append(statistics.mean(current_t_mean))
    playable_t_std.append(statistics.mean(current_t_std))
"""
plt.errorbar(k_range, playable_io_mean, playable_io_std, fmt='o', color='black', ecolor='lightgray')
plt.title("Cantidad de I/Os para los k experimentos de Búsqueda Binaria")
plt.xlabel("Cantidad k de repeticiones del experimento")
plt.ylabel("Promedio I/Os")
#plt.savefig("visualizations/std_para_new_k")
plt.show()
"""
plt.plot(k_range, playable_t_std)
plt.show()
#print(playable_io_total)
