import random
import string
from subprocess import PIPE, run

def generate_random_string(length):
    letters = string.ascii_lowercase
    resulting_string = ''.join(random.choice(letters) for i in range(length))
    return resulting_string

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout.strip('\n')