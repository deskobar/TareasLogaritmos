from experimentos.get_k import find_p, find_V
from experimentos.p_visualizer import p_visualization
from experimentos.v_visualizer import v_visualization
from experimentos.m_visualizer import m_visualization
import json

MAX_NODES = 1000
v = MAX_NODES
p_range = [p/10 for p in range(1, 11)]

fib_p = find_p("fibo", v, p_range)
with open("experimentos/files/find_p_fib.json", 'w+') as fp:
    json.dump(fib_p, fp)
fp.close()
bin_p = find_p("bin", v, p_range)
with open("experimentos/files/find_p_bin.json", 'w+') as fp:
    json.dump(bin_p, fp)
fp.close()

dict_xd = {}
for i in fib_p.keys():
    current = float(fib_p[i]["time_std"]) + float(bin_p[i]["time_std"])
    dict_xd[float(i)] = current
index = max(sorted(dict_xd.items())[0:3])[0]
print(index)

v_range = list(range(0, MAX_NODES+1, MAX_NODES//10))
v_range[0] = 2
fib_v = find_V(index, "fibo", v_range)
with open("experimentos/files/find_v_fib.json", 'w+') as fp:
    json.dump(fib_v, fp)
fp.close()
bin_v = find_V(index, "bin", v_range)
with open("experimentos/files/find_v_bin.json", 'w+') as fp:
    json.dump(bin_v, fp)
fp.close()

p_visualization(v)
v_visualization()
m_visualization()
