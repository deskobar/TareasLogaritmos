from utils import *

BLOCK_SIZE = 500

def linear_search(file_path_P, file_path_T):
    P = get_P(file_path_P)
    file_T = get_T(file_path_T)
    length_T = get_length_file(file_path_T)
    output = open('linear_output.txt', 'w+') 
    for iteration_index in range(0, length_T, BLOCK_SIZE):
        start_reading_from = LINE_SIZE * iteration_index
        if(iteration_index + BLOCK_SIZE > length_T):
            number_of_lines = length_T - iteration_index
        else:
            number_of_lines = BLOCK_SIZE
        lines = read_many_lines(start_reading_from, number_of_lines, file_T)
        for element in lines:
            if int(element) in P:
                found_element = element.zfill(9) + '\n'
                output.write(found_element)
    output.close()
    file_T.close()
    return 0

execute_search(linear_search)
