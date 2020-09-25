# l: inicio del espacio de búsqueda
# h: fin del espacio de búsqueda
# Requiere que la propiedad sea "monótona": es falsa hasta cierto punto. Después de ese punto y en adelante es siempre verdadera.
# Busca el primer valor entre l y h que hace a la propiedad verdadera.
from pathlib import Path
import sys
def get_len(fn):
    kB = Path(fn).stat().st_size
    return kB//10

def binarySearch(path_p, path_t):
  P = []
  with open(path_p, 'r') as fp:
    P = [int(line.strip()) for line in fp]
  fp.close()
  ft = open(path_t, 'r')
  output = open("output.txt", "w+")
  for p in P:
    l = 0
    h = get_len(path_t)
    m = 0
    while (l < h):
      m = l + (h - l)//2
      ft.seek(10*m)
      current_num = int(ft.read(9))
      if p <= current_num:
        h = m;
      else:
        l = m + 1;
    ft.seek(10*l)
    current_num = int(ft.read(9))
    if p == current_num:
        num_str = str(current_num) 
        num_str_zeros = num_str.zfill(9)
        text = "".join([num_str_zeros,"\n"])
        output.write(text)
  output.close()
  ft.close()
  return 0

arg = sys.argv
binarySearch(arg[1], arg[2])
