# l: inicio del espacio de búsqueda
# h: fin del espacio de búsqueda
# Requiere que la propiedad sea "monótona": es falsa hasta cierto punto. Después de ese punto y en adelante es siempre verdadera.
# Busca el primer valor entre l y h que hace a la propiedad verdadera.
from pathlib import Path

def get_len(fn):
    kB = Path(fn).stat().st_size
    return kB//10

path_p = "P.txt"
path_t = "T.txt"

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
        text = "".join([str(current_num),"\n"])
        output.write(text)
output.close()
ft.close()
