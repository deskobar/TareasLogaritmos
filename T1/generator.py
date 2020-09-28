import random
import os
import sys

P_PATH = "P_test.txt"
T_PATH = "T_test.txt"
T_PATH_tmp = ".tmp.txt"

def generator(p, t):
    P = open(P_PATH, "w+")
    T = open(T_PATH_tmp, "w+")
    for i in range(int(p)):
        p_random = random.randint(1, 10**7)
        p_string = str(p_random).zfill(9) + '\n'
        P.write(p_string)
    P.close()
    for j in range(int(t)):
        t_random = random.randint(1, 10**7)
        t_string = str(t_random).zfill(9) + '\n'
        T.write(t_string)
    T.close()
    os.system('sort ' + T_PATH_tmp + ' > ' + T_PATH)
    os.system("rm " + T_PATH_tmp)
    
arg = sys.argv
generator(arg[1], arg[2])