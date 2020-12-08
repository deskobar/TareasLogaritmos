import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    resulting_string = ''.join(random.choice(letters) for i in range(length))
    return resulting_string