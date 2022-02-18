from application.data import Data
from application.algorithms.bubble_sort import bubble_sort
from application.algorithms.selection_sort import selection_sort
from application.algorithms.merge_sort import merge_sort
from application.algorithms.insertion_sort import insertion_sort
from application.algorithms.bogo_sort import bogo_sort
from application.algorithms.quick_sort import quick_sort

data_ctx = {'Random': Data.random,
            'Reversed': Data.reversed,
            'Few Unique': Data.few_unique,
            }

algo_ctx = {'Selection': selection_sort,
            'Bubble': bubble_sort,
            'Merge': merge_sort,
            'Insertion': insertion_sort,
            'QuickSort': quick_sort,
            'BogoSort': bogo_sort,
            }
