from utils import execute_search, get_P, get_T, get_output, get_length_file, BLOCK_SIZE, math, read_a_line_from_file, read_many_lines, LINE_SIZE

def linear_search(file_path_P, file_path_T):
    read_accesses = 0
    write_accesses = 0
    to_write = []
    P = get_P(file_path_P)
    file_T = get_T(file_path_T)
    length_T = get_length_file(file_path_T)
    output = get_output('output_files/output_linear.txt')
    for iteration_index in range(0, length_T, BLOCK_SIZE):
        start_reading_from = LINE_SIZE * iteration_index
        if(iteration_index + BLOCK_SIZE > length_T):
            number_of_lines = length_T - iteration_index
        else:
            number_of_lines = BLOCK_SIZE
        lines = read_many_lines(start_reading_from, number_of_lines, file_T)
        read_accesses += 1
        for element in lines:
            if element in P:
                found_element = element.zfill(9) + '\n'
                to_write.append(found_element)
                if len(to_write) * LINE_SIZE == BLOCK_SIZE:
                    output.write(''.join(to_write))
                    write_accesses += 1
                    to_write = []   
    file_T.close()
    if(len(to_write) != 0):
        output.write(''.join(to_write))
        write_accesses += 1
    output.close()
    return read_accesses, write_accesses

execute_search(linear_search)
