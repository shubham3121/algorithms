class MergeSort:
    def __init__(self, array):
        self.array = array
        self.size = len(array)

    @staticmethod
    def _merge(left, right):
        """
        Merges left and right array into a single array.
        Assumes, left and right are sorted independently sorted.
        """

        resultant = []

        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                resultant.append(left[i])
                i += 1
            else:
                resultant.append(right[j])
                j += 1

        while i < len(left):
            resultant.append(left[i])
            i += 1

        while j < len(right):
            resultant.append(right[j])
            j += 1

        return resultant

    def sort(self):
        """
        Sorts the array using Merge Sort algorithm.

        1. Divide the array into 2 arrays of size n/2.
        2. Merge the two sorted arrays of size n/2.
        3. Resultant is a sorted array of size n.

        Time Complexity: O(n*log(n))
        Space Complexity: n
        """
        self.array = self._sort(self.array)
        return self.array

    @classmethod
    def _sort(cls, array):

        if len(array) < 2:
            return array

        mid = len(array) // 2

        left = cls._sort(array[:mid])
        right = cls._sort(array[mid:])

        return cls._merge(left=left, right=right)

    def __repr__(self):
        return str(self.array)

    def __str__(self):
        return self.__repr__()
