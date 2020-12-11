import os
import random
from .bloom_filter import BloomFilter
from .utils import generate_random_string

MIN_USERNAME_SIZE = 4
MAX_USERNAME_SIZE = 30
MIN_EMAIL_SIZE = 10
MAX_EMAIL_SIZE = 50
EMAIL_DOMAIN = '@email.cl'

def generate_file(m, k, n):
    bloom_filter = BloomFilter(m, k)
    L_file = open('L_file.txt', 'x') #?
    for _ in range(0, n):
        random_length_1 = random.randint(MIN_USERNAME_SIZE, MAX_USERNAME_SIZE)
        random_username = generate_random_string(random_length_1)
        bloom_filter.insert(random_username)
        random_length_2 = random.randint(MIN_EMAIL_SIZE, MAX_EMAIL_SIZE)
        random_email = generate_random_string(random_length_2) + EMAIL_DOMAIN
        line = random_username + ' ' + random_email + '\n'
        print(line + '\n')
        with open('L_file.txt', 'a') as L_file:
            L_file.write(line)
    L_file.close()
    return bloom_filter, L_file

#generate_file(5, 2, 20)

def search_username_in_file(username, L_file_name):
    cmd = f"grep '{username}' '{L_file_name}'"
    os.system(cmd)

search_username_in_file('bffrobqsoywoxdmfzkoq', 'L_file.txt')
