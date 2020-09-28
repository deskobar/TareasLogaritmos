import statistics
from generator import generator
from binarySearch import binarySearch

for k in range(2, 4):
    tmp = []
    # f = open("resultados/binarySearch/k=" + str(k) + ".txt", "w+")
    for i in range(k):
        generator("10000", "1000000")
        time = binarySearch("P_test.txt", "T_test.txt")
        tmp.append(time)
    # quiero escribir k=2 - total=sdfs - promedio=x - std=sdfdsf

    data = " - ".join(["k=" + str(k), "total=" + str(sum(tmp)), "promedio=" + str(statistics.mean(tmp)), "std=" + str(statistics.stdev(tmp))]) + "\n"
    print(data)
    # f.write(data)
# f.close()
"""
data = " - ".join(["k=" + str(k),"promedio=" + str(average), "std=" + str(std)])
print(data)
spliteado = data.split(" - ")
k = spliteado[0].strip("k=")
total = spliteado[1].strip("total=")
promedio = spliteado[2].strip("promedio=")
std = spliteado[3].strip("std=")
print(k)
print(promedio)
print(std)
"""