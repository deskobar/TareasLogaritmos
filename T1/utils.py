from pathlib import Path
import sys
import time

def get_len(fn):
  kB = Path(fn).stat().st_size
  line_size = 10
  len_file = kB // line_size
  return len_file


def execute_search(algorithm):
    args = sys.argv

    t_i = time.time()
    algorithm(args[1], args[2])
    delta_t = time.time() - t_i

    print("[*] ISEARCH FINISHED SUCCESSFULLY")
    print("[*] TIME ELAPSED: " + str(delta_t) + " (s)")