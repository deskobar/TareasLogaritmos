import random
import os
import sys
import time 

P_PATH = "P_test.txt"
T_PATH = "T_test.txt"
T_PATH_tmp = ".tmp.txt"

MIN = 1
MAX = 10**9

def generator(p, t):
    ti = time.time()
    print("[*] GENERATING FILES STARTED")
    P = open(P_PATH, "w+")
    T = open(T_PATH_tmp, "w+")
    for i in range(int(p)):
        p_random = random.randint(MIN, MAX)
        p_string = str(p_random).zfill(9) + '\n'
        P.write(p_string)
    P.close()
    for j in range(int(t)):
        t_random = random.randint(MIN, MAX)
        t_string = str(t_random).zfill(9) + '\n'
        T.write(t_string)
    T.close()
    os.system('sort ' + T_PATH_tmp + ' > ' + T_PATH)
    os.system("rm " + T_PATH_tmp)
    print("[*] FILES GENERATED SUCCESSFULLY")
    print("[*] TIME ELAPSED: " + str(time.time() - ti) + " (s)")
arg = sys.argv
generator(arg[1], arg[2])