# l: inicio del espacio de búsqueda
# h: fin del espacio de búsqueda
# Requiere que la propiedad sea "monótona": es falsa hasta cierto punto. Después de ese punto y en adelante es siempre verdadera.
# Busca el primer valor entre l y h que hace a la propiedad verdadera.
from utils import execute_search, get_P, get_T, get_output, get_length_file, read_a_line_from_file, LINE_SIZE, BLOCK_SIZE

def binary_search(path_p, path_t):
  read_accesses = 0
  write_accesses = 0
  to_write = []
  P = get_P(path_p)
  ft = get_T(path_t)
  output = get_output('output_files/output_binary.txt')
  
  # We need to iterate over P loaded in memory
  for p in P:
    l = 0
    h = get_length_file(path_t) - 1
    m = 0
    stop = False
    while (l <= h and not stop):
      m = (l + h) // 2
      current_num = read_a_line_from_file(ft, m)
      read_accesses += 1
      if p < current_num:
        h = m - 1
      elif p > current_num:
        l = m + 1
      else:
        num = current_num.zfill(9) + '\n'
        to_write.append(num)
        if len(to_write) * LINE_SIZE >= BLOCK_SIZE:
          output.write(''.join(to_write))
          write_accesses += 1
          to_write = []   
        stop = True
  ft.close()
  if(len(to_write) != 0):
      output.write(''.join(to_write))
      write_accesses += 1
  output.close()
  return read_accesses, write_accesses
