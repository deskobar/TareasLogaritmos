def array_chunks(array, size):
    for index in range(0, len(array), size):
        yield array[index:index + size]

def linear_search(array_P, array_T, size_B):
    P_intersection_T = []
    chunks = array_chunks(array_T, size_B)
    for chunk in chunks:
        for element in chunk:
            if element in array_P:
                P_intersection_T.append(element)
    return P_intersection_T

array_P = [3, 5, -4598, 9, 0, 345, 23]
array_T = [-378, 2, 7, 3, 67, 900, 2321, 4, 6, 0, 2, 1, 90, 134, 23, 345, 56, 22]
size_B = 2

print(linear_search(array_P, array_T, size_B))
