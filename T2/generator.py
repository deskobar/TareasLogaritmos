import sys
from src.generator_base import generator

generated_graph = generator(int(sys.argv[1]), float(sys.argv[2]))
for key, value in generated_graph.items():
    print(key, value)