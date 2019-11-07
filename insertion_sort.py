class BinaryInsertionSort:
    """
    Binary Insertion sort performs search and compare
    operation using binary search. Thus the search and compare operation
    takes O(log(n)) time, while swaps takes O(n) time.

    Time Complexity: O(n*(log(n) + n)) ≈ O(n^2)
    """

    def __init__(self, array):
        self.array = array
        self.size = len(array)

    def sort(self):
        """
        Sorts the elements of the array in ascending order

        Time complexity: O(n^2)
        Space complexity: O(1)

        :param array:
        :return: sorted array
        """

        if self.size < 2:
            return self.array

        for i in range(1, self.size):
            # search and compare function
            idx = self._search_lower_element_idx(key=i)

            # swap function
            self._swap_elements(src=i, dest=idx)

        return self.array

    def _swap_elements(self, src, dest):
        """
        Swaps all elements in reverse order i.e. starting from src
        index till the destination index.

        Time Complexity:  O(n)
        """
        while src > dest:
            if self.array[src] < self.array[src-1]:
                temp = self.array[src]
                self.array[src] = self.array[src - 1]
                self.array[src - 1] = temp
            src = src - 1

    def _search_lower_element_idx(self, key):
        """
        Search for the index in the array[0, key-1], whose value is
        less than the value at the key index of the array.

        Compare & search Time Complexity: O(log(n))
        """

        start, end = 0, len(self.array[:key-1])
        mid = (start + end) // 2

        while start < end:

            if self.array[mid] > self.array[key]:
                end = mid
            else:
                return mid + 1

            mid = (start + end) // 2

        return mid
