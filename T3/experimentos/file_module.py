import os
import random
from src.bloom_filter import BloomFilter
from src.utils import generate_random_string, out

MIN_USERNAME_SIZE = 4
MAX_USERNAME_SIZE = 30
MIN_EMAIL_SIZE = 10
MAX_EMAIL_SIZE = 50
EMAIL_DOMAIN = '@email.cl'

def generate_files_and_insert_to_bloom_filter(bf, big_n, small_n):
    universe_file = open('universe_file.txt', 'w+')
    L_file = open('L_file.txt', 'w+') 
    for i in range(0, big_n):
        random_length_1 = random.randint(MIN_USERNAME_SIZE, MAX_USERNAME_SIZE)
        random_username = generate_random_string(random_length_1)
        universe_file.write(random_username + '\n')
        if i < small_n:
            bf.insert(random_username)
            random_length_2 = random.randint(MIN_EMAIL_SIZE, MAX_EMAIL_SIZE)
            random_email = generate_random_string(random_length_2) + EMAIL_DOMAIN
            line = random_username + ' ' + random_email + '\n'
            L_file.write(line)
    universe_file.close()
    L_file.close()
    return bf, L_file, universe_file

def search_username_in_file(username, L_file_name):
    cmd = f"grep '{username}' " + L_file_name
    output = out(cmd)
    if output != "":
        return output
    else:
        return None
