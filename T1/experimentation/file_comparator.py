def are_files_equal(file_name_1, file_name_2):
    with open(file_name_1, 'r') as file1:
        with open(file_name_2, 'r') as file2:
            difference = set(file1).difference(file2)
    file1.close()
    file2.close()
    if len(difference) > 0:
        return False
    return True

def are_all_files_equal(file_array):
    response = True
    first_file = file_array[0]
    index = 1
    while index < len(file_array):
        file_element = file_array[index]
        if not are_files_equal(first_file, file_element):
            response = False
            print('{} is not equal to the rest of the files'.format(file_element))
            break
        index += 1
    return response

def compare_output_files():
    file_array = ['output_files/output_binary.txt', 'output_files/output_indexed.txt', 'output_files/output_linear_search_plus_binary.txt', 'output_files/output_linear_search_plus_merge.txt']
    response = are_all_files_equal(file_array)
    if response:
        print ('[*] ALL OUTPUT FILES ARE EQUAL')
    else:
        print ('[*] ALL OUTPUT FILES ARE NOT EQUAL')