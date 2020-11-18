from experimentos.get_k import find_p_bin, find_p_fib
import json

fib_cases = find_p_fib()
with open("experimentos/files/find_p_fib.json", 'w+') as fp:
    json.dump(fib_cases, fp)
fp.close()
print(fib_cases)
bin_cases = find_p_bin()
with open("experimentos/files/find_p_bin.json", 'w+') as fp:
    json.dump(bin_cases, fp)
fp.close()
print(bin_cases)


