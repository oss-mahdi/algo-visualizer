from algorithms.sorting.sorts import Sort


lst1 = [3, 2, 1, 4, 5, 6, 7, 8, 9, 0]
lst2 = [6, 4, 3, 2, 1, 8, 5, 9, 7, 0, 11, 25, 23, 22, 21, 19, 18, 17, 16, 15, 14, 13, 12, 24, 20, 10]
lst3 = [1]
lst4 = []
lst5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sorted1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
sorted3 = [1]
sorted4 = []
sorted5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

test_cases = (
    (lst1, sorted1),
    (lst2, sorted2),
    (lst3, sorted3),
    (lst4, sorted4),
    (lst5, sorted5),
)


def test_bubble_sort():
    for lst, expected in test_cases:
        sort = Sort(lst)
        result = sort.bubble_sort()
        print("Result: ", result)
        print("Expected: ", expected)
        assert result == expected

if __name__ == "__main__":
    test_bubble_sort()
