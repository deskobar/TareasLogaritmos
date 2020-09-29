from pathlib import Path
import sys
import time

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
  with open(path_p, 'r') as fp:
    P = [int(line.strip()) for line in fp]
  fp.close()
  return P

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

