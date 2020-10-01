from utils import execute_search, get_P, get_T, get_output, get_length_file, BLOCK_SIZE, math, read_a_line_from_file, read_many_lines, LINE_SIZE

def linear_search_plus_merge(file_path_P, file_path_T):
    P = get_P(file_path_P)
    P.sort()
    file_T = get_T(file_path_T)
    length_T = get_length_file(file_path_T)
    output = get_output("output_linear_plus_merge.txt")
    for iteration_index in range(0, length_T, BLOCK_SIZE):
        start_reading_from = LINE_SIZE * iteration_index
        if iteration_index + BLOCK_SIZE > length_T:
            number_of_lines = length_T - iteration_index
        else:
            number_of_lines = BLOCK_SIZE
        lines = read_many_lines(start_reading_from, number_of_lines, file_T)
        index_P = 0
        index_T = 0
        next = True
        while index_P < len(P) and index_T < len(lines) and next:
            element_P = P[index_P]
            element_T = lines[index_T]
            if element_P > int(element_T):
                index_T += 1
            elif element_P < int(element_T):
                index_P += 1
            else:
                found_element = element_T.zfill(9) + '\n'
                output.write(found_element)
                next = False
    file_T.close()
    output.close()
    return 0

execute_search(linear_search_plus_merge)
