from utils import execute_search
from algorithms.binary_search import binary_search
from algorithms.linear_search import linear_search
from algorithms.indexed_search import indexed_search
from algorithms.linear_search_plus_binary import linear_search_plus_binary
from algorithms.linear_search_plus_merge import linear_search_plus_merge
from experimentation.file_comparator import compare_output_files

def algorithms_executor():
    algorithms = [binary_search, indexed_search, linear_search_plus_binary, linear_search_plus_merge]
    for algorithm in algorithms:
        execute_search(algorithm)
    compare_output_files()

algorithms_executor()