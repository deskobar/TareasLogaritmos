import time

super_array = range(500)
ti = time.time()
for i in range(5000):
    a = super_array[225]
tf = time.time()

dt = tf - ti
dp = dt/5000

filename = 'examplefile.txt'

ti = time.time()
for i in range(10):
    opened_file = open(filename, 'r')
tf = time.time()

dt = tf - ti
ds = dt/10

print(ds/dp)