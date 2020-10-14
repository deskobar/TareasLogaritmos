import matplotlib.pyplot as plt
import math
from utils import B

K_MAX = 10000
P_SIZE = 10000

# O(P*log2(T))
def o_bs_s(k):
    lg = math.log(P_SIZE*k, 2.0)
    return P_SIZE*lg

# O(T/k)
def o_bl_s(k):
    return P_SIZE*k/B

# O(B + T/500)
def o_bi_s(k):
    l = P_SIZE
    r = P_SIZE*k/B
    return l + r

# O(P*log2(T))
def o_bs_s_t(t):
    lg = math.log(t, 2.0)
    return P_SIZE*lg

# O(T/k)
def o_bl_s_t(t):
    return t/B

# O(B + T/500)
def o_bi_s_t(t):
    l = P_SIZE
    r = t/B
    return l + r

k_range = range(1000, 1500)
x = []
y_bs = []
y_bl = []
y_bi = []

xi = 3
yi = 5
div_x = 10**xi
div_y = 10**yi
for k in k_range:
    x.append(k/div_x)
    y_bs.append(o_bs_s(k)/div_y)
    y_bl.append(o_bl_s(k)/div_y)
    y_bi.append(o_bi_s(k)/div_y)

plt.plot(x, y_bs, 'r', label='Búsqueda binaria') # plotting t, a separately 
plt.plot(x, y_bl, 'g', label='Búsqueda lineal') # plotting t, a separately 
plt.plot(x, y_bi, 'b', label='Búsqueda indexada') # plotting t, a separately 
plt.title("Total de operaciones I/Os teórico en los diferentes algoritmos\n en función del valor $\\rho$=|T|/|P|")
plt.xlabel("Valor de $\\rho$ (10^{})".format(xi))
plt.ylabel("Número de operaciones I/O (10^{})".format(yi))
plt.legend() 
plt.savefig("visualizations/valor_rho.png", dpi=300)
plt.show()