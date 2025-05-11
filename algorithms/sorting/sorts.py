class Sort:
    def __init__(self):
        self.lst = [3,6,2,3,5,2,1,3,6,7]

    def swap( first, second, list ):
        temp = list[first]
        list[first] = list[second]
        list[second] = temp;


    def bubble_sort(self):
        """Return a sorted copy of self.lst using bubble sort."""
        local_lst = self.lst.copy()
        n = len( local_lst )

        for i in range( n-1 ):
            for j in range ( n-i-1 ):
                if local_lst[j] > local_lst[j+1]:
                    Sort.swap( j, j+1,local_lst )

        print(local_lst)
        return local_lst

    def selection_sort(self):
        """Return a sorted copy of self.lst using selection sort."""
        local_lst = self.lst.copy()
        n = len( local_lst )

        for i in range( n-1 ):
            smallest = i
            for j in range ( i+1, n ):
                if local_lst[j] < local_lst[smallest]:
                    smallest = j
            Sort.swap(i, smallest, local_lst)

        print(local_lst)
        return local_lst;


    def insertion_sort(self):
        """Return a sorted copy of self.lst using insertion sort."""
        local_lst = self.lst.copy()
        n = len( local_lst)

        for i in range( 1,n ):
                curr = i
                while curr>0 and local_lst[curr]< local_lst[curr-1]:
                    Sort.swap( curr,curr-1,local_lst )
                    curr -=1

        print(local_lst)
        return local_lst

    def merge_sort(self):
        print(self.lst)

    def quick_sort(self):
        print(self.lst)

    def shell_sort(self):
        print(self.lst)

    def heap_sort(self):
        print(self.lst)



