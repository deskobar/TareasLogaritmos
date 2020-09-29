from pathlib import Path
import sys
import time
import math

ENDLINE_SIZE = sys.getsizeof('\n') - sys.getsizeof('') 
READ_SIZE = sys.getsizeof('000000000') - sys.getsizeof('') 
LINE_SIZE =  READ_SIZE + ENDLINE_SIZE


def get_length_file(fn):
  kB = Path(fn).stat().st_size
  len_file = kB // LINE_SIZE
  return len_file

def read_a_line_from_file(file, line):
    to_move = line * LINE_SIZE 
    file.seek(to_move)
    line = file.read(READ_SIZE)
    return line

def read_many_lines(start, number_of_lines, file_object):
    file_object.seek(start)
    one_big_line = file_object.read(LINE_SIZE * number_of_lines - ENDLINE_SIZE)
    lines = one_big_line.split('\n')
    return lines

def get_P(path_p):
  B = 500
  P_size = get_length_file(path_p)
  P_file = open(path_p, 'r')
  P_array = []
  #index_P_array = 0
  n_chunks = math.ceil(P_size / B)
  for i in range(n_chunks):
      start_reading_from = i * B * LINE_SIZE
      str_chunk = read_many_lines(start_reading_from, B, P_file)
      for str_number in str_chunk:
        if str_number != '':
          P_array.append( int(str_number) )# si es que haces conversión a enteros
          #index_P_array += 1
  P_file.close()
  return P_array

def get_T(path_t):
  return open(path_t, 'r')

def get_output(path_output):
  return open(path_output, "w+")

def execute_search(algorithm):
  args = sys.argv
  t_i = time.time()
  algorithm(args[1], args[2])
  delta_t = time.time() - t_i
  print("[*] " + algorithm.__name__.upper() + " FINISHED SUCCESSFULLY")
  print("[*] TIME ELAPSED: " + str(delta_t) + " (s)")

"""
    P_size = get_length_file(path_p)
    P_file = open(path_p, 'r')
    P_array = [None for i in range(P_size)]
    index_P_array = 0
    while True:
       read_chunk = P_file.read(B)
       if not read_chunk: # se acabó el archivo
           break
       str_numbers = read_chunk.split('\n')
       for str_number in str_numbers:
           P_array[index_P_array] = int(str_number) # si es que haces conversión a enteros
           index_P_array += 1
    return P_array
"""