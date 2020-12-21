from mmh3 import hash as hash_function
import BitVector.BitVector as BitVector
from random import randint
import sys
import time
import tracemalloc

class BloomFilter:

    def __init__(self, m, k):
        self.m = m
        self.V = BitVector(intVal = 0, size = m)
        self.hash_seeds = [None] * k
        self._fill_hash_seeds_array(k)
        
    
    def _fill_hash_seeds_array(self, k):
        for i in range(k):
            self.hash_seeds[i] = randint(1, sys.maxsize)
    
    def insert(self, p):
        for seed in self.hash_seeds:
            current_pos = hash_function(p, seed) % self.m
            self.V[current_pos] = 1

    def check(self, p):
        for seed in self.hash_seeds:
            current_pos = hash_function(p, seed) % self.m 
            current_val = self.V[current_pos]
            if current_val == 0:
                return 0
        return 1

    def insert_list(self, words):
        for word in words:
            self.insert(word)
    
    def get_V(self):
        return self.V

