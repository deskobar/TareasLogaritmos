from pathlib import Path
import sys
import time


def binary_search(arr, low, high, x): 
    if high >= low: 
  
        mid = (high + low) // 2
   
        if arr[mid] == x or high == low: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x) 
    else: 
        return -1


def indexedSearch(path_p, path_t):
    P = open(path_p, 'r')
    T = open(path_t, 'r')
    S = []
    out = open('output.txt', 'w+')
    
    len_t = get_len(T)
    B = BLOCK_SIZE
    n_blocks = len_t // B + 1

    for i in range(n_blocks):
        T.seek(10 * i * B)
        S.append(int(T.read(9)))
    
    for line in P.readlines():
        searched = int(line)
        s_interval_id = binary_search(S, 0, len(S) - 1, searched)
        
        if searched == S[s_interval_id]:
            num = str(searched).zfill(9) + '\n'
            out.write(num)
        else:
            T.seek(10 * s_interval_id * B)
            block = T.read(10 * B).split(sep='\n')
            for block_number in block:
                if searched == int(block_number):
                    num = str(searched).zfill(9) + '\n'
                    out.write(num)
    
    P.close()
    T.close()
    out.close()
