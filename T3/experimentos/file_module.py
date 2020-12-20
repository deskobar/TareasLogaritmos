import os
import random
from src.bloom_filter import BloomFilter
from src.utils import generate_random_string

MIN_USERNAME_SIZE = 4
MAX_USERNAME_SIZE = 30
MIN_EMAIL_SIZE = 10
MAX_EMAIL_SIZE = 50
EMAIL_DOMAIN = '@email.cl'

def generate_files_and_bloom_filter(m, k, big_n, small_n):
    bloom_filter = BloomFilter(m, k)
    universe_file = open('universe_file.txt')
    L_file = open('L_file.txt') 
    for i in range(0, big_n):
        random_length_1 = random.randint(MIN_USERNAME_SIZE, MAX_USERNAME_SIZE)
        random_username = generate_random_string(random_length_1)
        bloom_filter.insert(random_username)
        with open('universe_file.txt', 'a') as universe_file:
            universe_file.write(random_username)
        if i < small_n:
            random_length_2 = random.randint(MIN_EMAIL_SIZE, MAX_EMAIL_SIZE)
            random_email = generate_random_string(random_length_2) + EMAIL_DOMAIN
            line = random_username + ' ' + random_email + '\n'
            with open('L_file.txt', 'a') as L_file:
                L_file.write(line)
    universe_file.close()
    L_file.close()
    return bloom_filter, L_file, universe_file

#generate_file(5, 2, 20)

def search_username_in_file(username, L_file_name):
    cmd = f"grep '{username}' '{L_file_name}'"
    os.system(cmd)

search_username_in_file('bffrobqsoywoxdmfzkoq', 'L_file.txt')
