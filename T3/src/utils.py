import random
import string
from subprocess import PIPE, run
from math import ceil, log

def generate_random_string(length):
    letters = string.ascii_lowercase
    resulting_string = ''.join(random.choice(letters) for i in range(length))
    return resulting_string

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout.strip('\n')

def get_m(n, p):
    m = ceil(-n * log(p) / (log(2)**2))
    return m

def get_k(m, n):
    k = ceil((m/n) * log(2))
    return k

def probability_falses_positives(m, n):
    k = ceil(get_k(m, n))
    p = (1 - (1 - 1/m)**(k*n))**k
    return p

def get_correct_list(l):
    if len(l) == 0:
        return [0, 0]
    if len(l) == 1:
        return l * 2
    return l