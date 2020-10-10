import matplotlib.pyplot as plt
import math
from utils import B

K_MAX = 10000
P_SIZE = 3*10000
# T = P*k

# linear puro
def o_bl_p(k):
    T_SIZE = P_SIZE * k
    return P_SIZE * T_SIZE

# linear con bsearch
def o_bl_bs_p(k):
    # PTlogT/B
    T_SIZE = P_SIZE * k
    return T_SIZE / B * P_SIZE * math.log(B, 2.0)

# linear con merge
def o_bl_m_p(k):
    #PlogP + T + PT/B
    T_SIZE = P_SIZE * k
    return P_SIZE * math.log(P_SIZE, 2.0) + T_SIZE + T_SIZE * P_SIZE / B

k_range = range(1, 100)
x = []
y_ls_pura = []
y_ls_binary = []
y_ls_merge = []

div_x = 10000
div_y = 100000
for k in k_range:
    x.append(k)
    y_ls_pura.append(o_bl_p(k))
    y_ls_binary.append(o_bl_bs_p(k))
    y_ls_merge.append(o_bl_m_p(k))

plt.plot(x, y_ls_pura, 'r', label='Búsqueda lineal') # plotting t, a separately 
plt.plot(x, y_ls_binary, 'g', label='Búsqueda lineal con búsqueda binaria') # plotting t, a separately 
plt.plot(x, y_ls_merge, 'b', label='Búsqueda lineal con merge') # plotting t, a separately 
plt.title("Total de operaciones en memoria principal teórico para las variaciones de la\n búsqueda lineal en función del valor k=|T|/|P|")
plt.xlabel("Valor de k")
plt.ylabel("Número de operaciones en CPU/RAM")
plt.legend()
plt.savefig("variaciones de busqueda lineal RAM")
plt.show()
