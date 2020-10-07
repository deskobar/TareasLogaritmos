import matplotlib.pyplot as plt
import math

K_MAX = 10000
T_SIZE = 1000000

# O(P*log2(T))
def o_bs_s(T, k):
    lg = math.log(T, 2.0)
    return (T/k)*lg

def o_bs_p(T, k):
    lg = math.log(T, 2.0)
    return (T/k)*lg

# O(T/k)
def o_bl_s(T, k):
    return T/500

def o_bl_p(T, k):
    return T**2/k

# O(B + T/500)
def o_bi_s(T, k):
    l = T/k
    r = T/500
    return l + r

def o_bi_p(T, k):
    lg = math.log(T/500, 2.0)
    return T/k*(lg + 500)

k_range = range(9000, 10500)
x = []
y_bs = []
y_bl = []
y_bi = []

div = 1000
for k in k_range:
    x.append(k/div)
    y_bs.append(o_bs_s(T_SIZE, k)/div)
    y_bl.append(o_bl_s(T_SIZE, k)/div)
    y_bi.append(o_bi_s(T_SIZE, k)/div)

plt.plot(x, y_bs, 'r', label='Búsqueda binaria') # plotting t, a separately 
plt.plot(x, y_bl, 'g', label='Búsqueda lineal') # plotting t, a separately 
plt.plot(x, y_bi, 'b', label='Búsqueda indexada') # plotting t, a separately 
plt.title("Total de operaciones I/Os teórico en los diferentes algoritmos\n en función del valor k=|T|/|P|")
plt.xlabel("Valor de k (10^3)")
plt.ylabel("Número de operaciones I/O (10^3)")
plt.legend()
plt.savefig("valor de k op io")
plt.show()
