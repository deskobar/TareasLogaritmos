from utils import *


BLOCK_SIZE = 200


def binary_search_modified(arr, low, high, x): 
    if high >= low: 
  
        mid = (high + low) // 2
   
        if arr[mid] == x or high == low: 
            return mid 
        elif arr[mid] > x: 
            return binary_search_modified(arr, low, mid - 1, x) 
        else: 
            return binary_search_modified(arr, mid + 1, high, x) 
    else: 
        return -1


def indexedSearch(path_p, path_t):
    P = open(path_p, 'r')
    T = open(path_t, 'r')
    S = []
    out = open('output.txt', 'w+')
    
    len_t = get_len(path_t)
    B = BLOCK_SIZE
    n_blocks = len_t // B + 1

    for i in range(n_blocks):
        T.seek(11 * i * B)
        line_str = T.read(9)
        if bool(line_str):
            S.append(int(line_str))
    
    for line in P.readlines():
        searched = int(line)
        s_interval_id = binary_search_modified(S, 0, len(S) - 1, searched)

        if s_interval_id >= 0:
            if searched == S[s_interval_id]:
                num = str(searched).zfill(9) + '\n'
                out.write(num)
            else:
                T.seek(11 * s_interval_id * B)
                block = T.read(11 * B).split(sep='\n')
                for block_number in block:
                    if bool(block_number) and searched == int(block_number):
                        num = str(searched).zfill(9) + '\n'
                        out.write(num)

    P.close()
    T.close()
    out.close()


execute_search(indexedSearch)
