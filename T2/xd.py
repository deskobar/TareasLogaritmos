from src.generator_base import generator
from src.utils import get_aristas
import random

for i in range(100):
    density = random.random()
    nodes = 1000
    graph = generator(nodes, density)
    aristas_dadas = get_aristas(graph)
    aristas_esperadas = (nodes - 1) + density*((nodes**2 - nodes)//2 - (nodes - 1))//1
    dt = aristas_dadas - aristas_esperadas
    msj = "[{}] || [Nodes] {} || [Density] {} || [AristasR] {} || [AristasE] {} || [Delta] {}".format(i, nodes, density, aristas_dadas, aristas_esperadas, dt)
    print(msj) 