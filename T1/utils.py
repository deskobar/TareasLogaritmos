from pathlib import Path
import sys
import time
import math
import os

BLOCK_SIZE = 500
if os.name == 'nt':
  ENDLINE_SIZE = sys.getsizeof('\r\n') - sys.getsizeof('') 
else:
  ENDLINE_SIZE = sys.getsizeof('\n') - sys.getsizeof('') 
READ_SIZE = sys.getsizeof('000000000') - sys.getsizeof('') 
LINE_SIZE =  READ_SIZE + ENDLINE_SIZE
B = BLOCK_SIZE // LINE_SIZE

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
  one_big_line = file_object.read(LINE_SIZE * number_of_lines)
  lines = one_big_line.split('\n')
  return lines

def get_P(path_p):
  P_size = get_length_file(path_p)
  P_file = open(path_p, 'r')
  P_array = [None for i in range(P_size)]
  n_chunks = math.ceil(P_size / B)
  index_P_array = 0
  for i in range(n_chunks):
    start_reading_from = i * B * LINE_SIZE
    str_chunk = read_many_lines(start_reading_from, B, P_file)
    for str_number in str_chunk:
      if str_number != '':
        P_array[index_P_array] = str_number
        index_P_array += 1
  P_file.close()
  return P_array

def get_T(path_t):
  return open(path_t, 'r')

def get_output(path_output):
  return open(path_output, 'w+')

def execute_search(algorithm):
  args = sys.argv
  t_i = time.time()
  algorithm(args[1], args[2])
  delta_t = time.time() - t_i
  print('[*] ' + algorithm.__name__.upper() + ' FINISHED SUCCESSFULLY')
  print('[*] TIME ELAPSED: ' + str(delta_t) + ' (s)')