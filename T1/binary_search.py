# l: inicio del espacio de búsqueda
# h: fin del espacio de búsqueda
# Requiere que la propiedad sea "monótona": es falsa hasta cierto punto. Después de ese punto y en adelante es siempre verdadera.
# Busca el primer valor entre l y h que hace a la propiedad verdadera.
from utils import execute_search, get_P, get_T, get_output, get_length_file, read_a_line_from_file

def binary_search(path_p, path_t):
  
  P = get_P(path_p)
  ft = get_T(path_t)
  output = get_output("output_binary.txt")
  # We need to iterate over P loaded in memory
  for p in P:
    l = 0
    h = get_length_file(path_t) - 1
    m = 0
    while (l <= h):
      m = (l + h) // 2
      current_num = read_a_line_from_file(ft, m)
      if p < int(current_num):
        h = m - 1
      elif p > int(current_num):
        l = m + 1
      else:
        num = current_num.zfill(9) + '\n'
        output.write(num)   
        break
  ft.close()
  output.close()
  return 0

execute_search(binary_search)
