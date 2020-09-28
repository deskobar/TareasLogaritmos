# l: inicio del espacio de búsqueda
# h: fin del espacio de búsqueda
# Requiere que la propiedad sea "monótona": es falsa hasta cierto punto. Después de ese punto y en adelante es siempre verdadera.
# Busca el primer valor entre l y h que hace a la propiedad verdadera.
from pathlib import Path
import sys

def get_len(fn):
    kB = Path(fn).stat().st_size
    line_size = 10
    len_file = kB//line_size
    return len_file

def binarySearch(path_p, path_t):
  # Files section
  P = []
  with open(path_p, 'r') as fp:
    P = [int(line.strip()) for line in fp]
  fp.close()
  ft = open(path_t, 'r')
  output = open("output.txt", "w+") # Could be a huge file, so we don't read nothing

  # We need to iterate over P loaded in memory
  for p in P:
    l = 0
    h = get_len(path_t)
    m = 0
    while (l < h):
      m = l + (h - l)//2
      ft.seek(10*m) # Move the pointer to the line we're interested 
      current_num = int(ft.read(9)) # And read
      if p <= current_num:
        h = m
      else:
        l = m + 1
    ft.seek(10*l)
    current_num = int(ft.read(9))
    if p == current_num:
        num = str(current_num).zfill(9) + '\n'
        output.write(num)
  output.close()
  ft.close()
  return 0

arg = sys.argv
binarySearch(arg[1], arg[2])
