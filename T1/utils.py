xd = ['a', 'b', 'c', 'd']
en = enumerate(xd)

path_t = "binarySearch/T.txt"
ft = open(path_t, 'r')
ft.seek(10)
print(ft.read(9))
ft.seek(10)
print(ft.read(9))
ft.close()