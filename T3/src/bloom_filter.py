from mmh3 import hash128 as hash_function
import BitVector.BitVector as BitVector
from random import randint
import sys

class BloomFilter:

    m = None
    V = None
    hash_seed = []

    def __init__(self, m, k):
        self.m = m
        self.V = BitVector(intVal = 0, size = m)
        self.hash_seed = [0]*k
        self._fill_hash_seed_array(k)
        
    
    def _fill_hash_seed_array(self, k):
        for i in range(k):
            self.hash_seed[i] = randint(1, sys.maxsize)
    
    def insert(self, p):
        for seed in self.hash_seed:
            current_pos = hash_function(p, seed, signed = False) % self.m
            self.V[current_pos] = 1

    def check(self, p):
        for seed in self.hash_seed:
            current_pos = hash_function(p, seed, signed = False) % self.m 
            current_val = self.V[current_pos]
            if current_val == 0:
                return 0
        return 1

    def insert_list(self, words):
        for word in words:
            self.insert(word)

