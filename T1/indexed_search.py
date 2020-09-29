from utils import *

BLOCK_SIZE = 500

def binary_search_modified(arr, x, n):
    low = 0
    mid = 0
    high = n
    while (low < high):
        mid = low + (high - low) // 2
        if x <= arr[mid]:
            high = mid
        else:
            low = mid + 1
    if x < arr[low]:
        return low - 1
    elif x == arr[low]:
        return low
    else:
        return -1

def indexedSearch(path_p, path_t):
    P = get_P(path_p)
    T = get_T(path_t)
    out = get_output("output_indexed.txt")
    S = []
    len_t = get_length_file(path_t)
    B = BLOCK_SIZE
    n_blocks = len_t // B + 1
    for i in range(n_blocks):
        line_str = read_a_line_from_file(T, i * B)
        if line_str != '':
            S.append(int(line_str))
    for searched in P:
        s_interval_id = binary_search_modified(S, searched, len(S) - 1)
        if s_interval_id != -1:
            start_reading_at = LINE_SIZE * s_interval_id * B
            for block_number in read_many_lines(start_reading_at, B, T):
                if block_number != '' and searched == int(block_number):
                    num = str(searched).zfill(9) + '\n'
                    out.write(num)
    T.close()
    out.close()
    return 0

execute_search(indexedSearch)