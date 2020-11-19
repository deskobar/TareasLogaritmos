import json
import matplotlib.pyplot as plt
import statistics

fib_fp = open("experimentos/files/find_p_fib.json")
fib_p = json.load(fib_fp)
fib_fp.close()

fib_big = []
for x in fib_p:
    time = []
    for i in fib_p[x]:
        current_time = []
        for p in fib_p[x][i]:
            current_time.append(fib_p[x][i][p])
        pair_time = statistics.mean(current_time), statistics.stdev(current_time)
        time.append(pair_time)
    fib_big.append(time)

fib_mean = []
fib_std  = []
for i in range(24):
    mean_time = (fib_big[0][i][0] + fib_big[1][i][0] + fib_big[2][i][0])/3
    std_time  = (fib_big[0][i][1] + fib_big[1][i][1] + fib_big[2][i][1])/3
    fib_mean.append(mean_time)
    fib_std.append(std_time)
min_std = min(fib_std)
print(fib_std.index(min_std) + 2)
plt.errorbar(range(2, 26), fib_mean, fib_std, fmt='o', color='black', ecolor='lightgray')
plt.title("Errorbar dij fib para k=3, la wea entre 2, 26 y V = 100")
plt.savefig("experimentos/visualizaciones/errorbar_dij_fib.png")
plt.clf()
plt.plot(range(2, 26), fib_std)
plt.title("STD fib")
plt.savefig("experimentos/visualizaciones/std_dij_fib.png")