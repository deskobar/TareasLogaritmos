import json
import matplotlib.pyplot as plt
import statistics

bin_fp = open("experimentos/files/find_p_bin.json")
bin_p = json.load(bin_fp)
bin_fp.close()

bin_big = []
for x in bin_p:
    time = []
    for i in bin_p[x]:
        current_time = []
        for p in bin_p[x][i]:
            current_time.append(bin_p[x][i][p])
        pair_time = statistics.mean(current_time), statistics.stdev(current_time)
        time.append(pair_time)
    bin_big.append(time)

bin_mean = []
bin_std  = []
for i in range(24):
    mean_time = statistics.mean([bin_big[0][i][0], bin_big[1][i][0], bin_big[2][i][0]])
    std_time = statistics.mean([bin_big[0][i][1], bin_big[1][i][1], bin_big[2][i][1]])
    bin_mean.append(mean_time)
    bin_std.append(std_time)
min_std = min(bin_std)
print(bin_std.index(min_std) + 2)
plt.errorbar(range(2, 26), bin_mean, bin_std, fmt='o', color='black', ecolor='lightgray')
plt.title("Errorbar dij bin para k=3, la wea entre 2, 26 y V = 100")
plt.savefig("experimentos/visualizaciones/errorbar_dij_bin.png")
