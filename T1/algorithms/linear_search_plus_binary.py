from utils import execute_search, get_P, get_T, get_output, get_length_file, BLOCK_SIZE, math, read_a_line_from_file, read_many_lines, LINE_SIZE, B

def binary_search_general(arr, x, n):
    low = 0
    mid = 0
    high = n
    while (low < high):
        mid = low + (high - low) // 2
        if x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            return False
    if x == arr[low]:
        return low
    else:
        return -1

def linear_search_plus_binary(file_path_P, file_path_T):
    read_accesses = 0
    write_accesses = 0
    to_write = []
    P = get_P(file_path_P)
    P_len = len(P)
    P.sort()
    file_T = get_T(file_path_T)
    length_T = get_length_file(file_path_T)
    output = get_output('output_files/output_linear_search_plus_binary.txt')
    for iteration_index in range(0, length_T, B):
        start_reading_from = LINE_SIZE * iteration_index
        if(iteration_index + B > length_T):
            number_of_lines = length_T - iteration_index
        else:
            number_of_lines = B
        lines = read_many_lines(start_reading_from, number_of_lines, file_T)
        read_accesses += 1
        for element in lines:
            current = element
            if binary_search_general(P, current, P_len - 1) != -1:
                found_element = element.zfill(9) + '\n'
                to_write.append(found_element)
                if len(to_write) * LINE_SIZE >= BLOCK_SIZE:
                    output.write(''.join(to_write))
                    write_accesses += 1
                    to_write = []  
    file_T.close()
    if(len(to_write) != 0):
        output.write(''.join(to_write))
        write_accesses += 1
    output.close()
    return read_accesses, write_accesses
