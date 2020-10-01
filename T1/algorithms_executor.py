from utils import execute_search
from binary_search import binary_search
from linear_search import linear_search
from indexed_search import indexed_search
from linear_search_plus_binary import linear_search_plus_binary
from linear_search_plus_merge import linear_search_plus_merge
from file_comparator import compare_output_files

def algorithms_executor():
    algorithms = [binary_search, linear_search, indexed_search, linear_search_plus_binary, linear_search_plus_merge]
    for algorithm in algorithms:
        execute_search(algorithm)
    compare_output_files