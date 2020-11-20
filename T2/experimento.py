from experimentos.exp_base import exp
import json

MAX_NODES = 1000
v = MAX_NODES
v_range = [10, 25, 50, 100, 250, 500, 1000, 2500, 5000]
p_range = [p/10 for p in range(1, 11)]

fib_dict = exp("fibo", v_range, p_range)
with open("experimentos/files/exp_fib.json", 'w+') as fp:
    json.dump(fib_dict, fp)
fp.close()

bin_dict = exp("fibo", v_range, p_range)
with open("experimentos/files/exp_bin.json", 'w+') as fp:
    json.dump(bin_dict, fp)
fp.close()

