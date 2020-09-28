import statistics
from generator import generator
from binarySearch import binarySearch
import json

total = {}

for k in range(2, 4):
    tmp = []
    for i in range(k):
        generator("10000", "1000000")
        time = binarySearch("P_test.txt", "T_test.txt")
        tmp.append(time)
    # quiero escribir k=2 - total=sdfs - promedio=x - std=sdfdsf

    total[k] = {"total": sum(tmp), 
                "promedio": statistics.mean(tmp),
                "std": statistics.stdev(tmp)} 

    data = " - ".join(["k=" + str(k), "total=" + str(sum(tmp)), "promedio=" + str(statistics.mean(tmp)), "std=" + str(statistics.stdev(tmp))]) + "\n"
    print(data)
with open('bsearch.json', 'w+') as fp:
    json.dump(total, fp)
fp.close()
