from algorithms.graph.graphs import Graph
from algorithms.sorting.sorts import Sort


if __name__ == "__main__":
    lst = [3,4,2,6,1,7,9,0,8,5]

    sorter = Sort(lst) 
    sorter.bubble_sort()
    sorter.selection_sort()
    sorter.insertion_sort()
    sorter.merge_sort_recursive()
    sorter.quick_sort()
    sorter.shell_sort()
    sorter.heap_sort()
