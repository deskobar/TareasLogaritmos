import sys
from src.generator_base import generator

output, graph, start = generator(int(sys.argv[1]), float(sys.argv[2]), toPrint=True)
for i in output:
    print(i)