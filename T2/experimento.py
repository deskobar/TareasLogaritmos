from experimentos.exp_base import exp
import json

MAX_NODES = 1000
v = MAX_NODES
v_range = [10000]
p_range = [p/10 for p in range(0, 11)]

fib_dict = exp(v_range, p_range)
with open("experimentos/files/exp.json", 'w+') as fp:
    json.dump(fib_dict, fp)
fp.close()

