from experimentos.exp_base import exp
import json
import time

v_range = [10, 50, 100, 500, 1000, 5000, 10000]
p_range = [p/10 for p in range(0, 11)]

print("[*****] EXPERIMENT STARTED AT {} [*****]".format(time.ctime(time.time())))
experiment_dictionary = exp(v_range, p_range)
with open("experimentos/files/exp.json", 'w+') as fp:
    json.dump(experiment_dictionary, fp)
fp.close()
print("[*****] EXPERIMENT FINISHED AT {} [*****]".format(time.ctime(time.time())))

