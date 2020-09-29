# l: inicio del espacio de búsqueda
# h: fin del espacio de búsqueda
# Requiere que la propiedad sea "monótona": es falsa hasta cierto punto. Después de ese punto y en adelante es siempre verdadera.
# Busca el primer valor entre l y h que hace a la propiedad verdadera.
from pathlib import Path
import sys
import time
from utils import *

def get_P(path_p):
  with open(path_p, 'r') as fp:
    P = [int(line.strip()) for line in fp]
  fp.close()
  return P

def get_T(path_t):
  return open(path_t, 'r')

def get_output(path_output):
  return open(path_output, "w+") 

def binary_search(path_p, path_t):
  
  P = get_P(path_p)
  ft = get_T(path_t)
  output = get_output("output.txt")

  # We need to iterate over P loaded in memory
  for p in P:
    l = 0
    h = get_len(path_t) - 1
    m = 0
    while (l < h):
      m = l + (h - l)//2
      current_num = read_line_from_file(ft, m)
      if p <= int(current_num):
        h = m
      else:
        l = m + 1
    current_num = read_line_from_file(ft, l)
    if p == int(current_num):
        num = current_num.zfill(9) + '\n'
        output.write(num)
  output.close()
  ft.close()
  return 0

arg = sys.argv
binary_search(arg[1], arg[2])
