from data import Data
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort

data_ctx = {'Random': Data.random,
            'Reversed': Data.reversed,
            'Few Unique': Data.few_unique,
            }

algo_ctx = {'Selection': selection_sort,
            'Bubble': bubble_sort,
            'Merge': merge_sort,
            'Insertion': None,
            'QuickSort': None,
            }
