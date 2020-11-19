from experimentos.get_k import find_p, find_V
import json

fib_p = find_p("fibo")
with open("experimentos/files/find_p_fib.json", 'w+') as fp:
    json.dump(fib_p, fp)
fp.close()
bin_p = find_p("bin")
with open("experimentos/files/find_p_bin.json", 'w+') as fp:
    json.dump(bin_p, fp)
fp.close()

min = 1e9
index = -1
for i in fib_p.keys():
    current = float(fib_p[i]["time_std"]) + float(bin_p[i]["time_std"])
    if current < min:
        min = current
        index = float(i)
print(index)

fib_v = find_V(index, "fibo")
with open("experimentos/files/find_v_fib.json", 'w+') as fp:
    json.dump(fib_v, fp)
fp.close()
bin_v = find_V(index, "bin")
with open("experimentos/files/find_v_bin.json", 'w+') as fp:
    json.dump(bin_v, fp)
fp.close()