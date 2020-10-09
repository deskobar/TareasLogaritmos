from utils import execute_search, get_P, get_T, get_output, get_length_file, BLOCK_SIZE, math, read_a_line_from_file, read_many_lines, LINE_SIZE

def binary_search_modified(arr, x, n):
    low = 0
    mid = 0
    high = n
    if n == 0:
        return 0
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

def indexed_search(path_p, path_t):
    read_accesses = 0
    write_accesses = 0
    P = get_P(path_p)
    T = get_T(path_t)
    out = get_output('output_files/output_indexed.txt')
    S = []
    to_write = []
    len_t = get_length_file(path_t)
    n_blocks = math.ceil(len_t / BLOCK_SIZE)
    for i in range(n_blocks):
        line_str = read_a_line_from_file(T, i * BLOCK_SIZE)
        read_accesses += 1
        S.append(line_str)
    for searched in P:
        s_interval_id = binary_search_modified(S, searched, len(S) - 1)
        if s_interval_id != -1:
            start_reading_at = LINE_SIZE * s_interval_id * BLOCK_SIZE
            many_lines = read_many_lines(start_reading_at, BLOCK_SIZE, T)
            read_accesses += 1
            for block_number in many_lines:
                if block_number != '' and searched == block_number:
                    num = searched.zfill(9) + '\n'
                    to_write.append(num)
                    if len(to_write) * LINE_SIZE >= BLOCK_SIZE:
                        out.write(''.join(to_write))
                        write_accesses += 1
                        to_write = []  
    T.close()
    if(len(to_write) != 0):
        out.write(''.join(to_write))
        write_accesses += 1
    out.close()
    return read_accesses, write_accesses
