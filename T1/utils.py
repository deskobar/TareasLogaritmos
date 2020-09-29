from pathlib import Path
import sys
import time

ENDLINE = sys.getsizeof('\n') - 49 
LINE_SIZE = 9 + ENDLINE

def get_len(fn):
  kB = Path(fn).stat().st_size
  len_file = kB // LINE_SIZE
  return len_file

def read_line_from_file(file, line):
    to_move = line * LINE_SIZE 
    to_read = LINE_SIZE - ENDLINE
    file.seek(to_move)
    line = file.read(to_read)
    return line

def execute_search(algorithm):
    args = sys.argv

    t_i = time.time()
    algorithm(args[1], args[2])
    delta_t = time.time() - t_i

    print("[*] ISEARCH FINISHED SUCCESSFULLY")
    print("[*] TIME ELAPSED: " + str(delta_t) + " (s)")
