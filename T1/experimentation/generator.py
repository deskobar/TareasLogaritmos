import random
import os
import sys

MIN = 1
MAX = 10**9
P_PATH = 'P_test.txt'
T_PATH = 'T_test.txt'
TMP_PATH = '.tmp.txt'


def generator(p, t):
    P = open(P_PATH, 'w+')
    TMP = open(TMP_PATH, 'w+')
    for i in range(int(p)):
        p_random = random.randint(MIN, MAX)
        p_string = str(p_random).zfill(9) + '\n'
        P.write(p_string)
    P.close()
    for j in range(int(t)):
        t_random = random.randint(MIN, MAX)
        t_string = str(t_random).zfill(9) + '\n'
        TMP.write(t_string)
    TMP.close()
    os.system('sort ' + TMP_PATH + ' > ' + T_PATH)
    os.system('rm ' + TMP_PATH)
#arg = sys.argv
#generator(arg[1], arg[2])