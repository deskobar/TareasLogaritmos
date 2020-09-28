from pathlib import Path
import sys
import time

def get_P(file_path_P):
    P = []
    with open(file_path_P, 'r') as file_P:
        P = [line.strip() for line in file_P]
    file_P.close()
    return P

def get_T(file_path_T):
    file_T = open(file_path_T, 'r')
    return file_T

def get_length_file(file_path):
    kB = Path(file_path).stat().st_size
    line_size = 10
    length_file = kB//line_size
    return length_file

def read_lines(characters_per_line, number_of_lines, file_object):
    one_big_line = file_object.read(characters_per_line * number_of_lines - 1)
    lines = one_big_line.split('\n')
    return lines

def linear_search(file_path_P, file_path_T, block_size_B):
    initial_time = time.time()
    print('[*] LINEAR SEARCH STARTED')

    block_size_B = int(block_size_B)
    characters_per_line = 10
    file_T = get_T(file_path_T)
    length_T = get_length_file(file_path_T) - 1
    P = get_P(file_path_P)
    P_intersection_T_file = open('P_intersection_T_file.txt', 'w+') 
    
    for iteration_index in range(0, length_T, block_size_B):
        file_pointer_location = (characters_per_line + 1) * iteration_index
        file_T.seek(file_pointer_location)
        if(iteration_index + block_size_B > length_T):
            number_of_lines = length_T - iteration_index
        else:
            number_of_lines = block_size_B
        lines = read_lines(characters_per_line, number_of_lines, file_T)
        for element in lines:
            if element in P:
                found_element = str(element).zfill(characters_per_line - 1) + '\n'
                P_intersection_T_file.write(found_element)
    
    P_intersection_T_file.close()
    file_T.close()

    final_time = time.time()
    delta_time = final_time - initial_time
    print('[*] LINEAR SEARCH FINISHED SUCCESSFULLY')
    print('[*] TIME ELAPSED: ' + str(delta_time) + ' (s)')
    return delta_time

arg = sys.argv
linear_search(arg[1], arg[2], arg[3])
