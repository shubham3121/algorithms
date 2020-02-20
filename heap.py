class Heap:
    """
    Heaps are implementation of priority queues.
    Max Heap Property: The key of a node is greater than
    the keys of its children.
    """

    def __init__(self, array):
        self.array = array
        self.heap_size = len(array)
        self.is_heap = False

    def _build_max_heap(self):
        """
        Builds a max heap, from an ordered array.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = self.heap_size // 2
        for i in range(n, -1, -1):
            self._max_heapify(i)

        self.is_heap = True

    def _max_heapify(self, i):
        """
        Checks if the parent i satisfies the heap property.
        If not then fix the heap property in the subtree root.

        Assumption: Trees rooted at left(i) and right(i) are max heaps.

        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < self.heap_size and self.array[left] > self.array[largest]:
            largest = left
        if right < self.heap_size and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            temp = self.array[i]
            self.array[i] = self.array[largest]
            self.array[largest] = temp
            self._max_heapify(i=largest)

    def sort(self):
        """
        Builds a max heap, if not already build.
        Swaps the first/ root element (largest) with the last element.
        Reduce the heap size by 1 and call max_heapify to fix the heap
        property at the root.
        Continue this process, till heap size is 0.

        Time Complexity: O(n*log(n))
        Space Complexity: O(1)
        """
        if not self.is_heap:
            self._build_max_heap()

        while self.heap_size > 0:
            self.array[0], self.array[self.heap_size - 1] = (
                self.array[self.heap_size - 1],
                self.array[0],
            )
            self.heap_size -= 1
            self._max_heapify(i=0)

        self.heap_size = len(self.array)
        return self.array

    def __repr__(self):
        return str(self.array)

    def __str__(self):
        return self.__repr__()


class MinHeap:
    """
    Implementation of priority queue using min heap.
    """

    def __init__(self, array):
        self.array = array
        self.heap_size = len(array)

    def build_min_heap(self):
        """
        Builds the min heap, with the min element on the top.
        """
        n = self.heap_size // 2
        for i in reversed(range(n)):
            self._min_heapify(i)

    def _min_heapify(self, curr_index):
        left = 2 * curr_index + 1
        right = 2 * curr_index + 2
        smallest = curr_index

        if left < self.heap_size and self.array[left] < self.array[smallest]:
            smallest = left
        if right < self.heap_size and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != curr_index:
            temp = self.array[curr_index]
            self.array[curr_index] = self.array[smallest]
            self.array[smallest] = temp
            self._min_heapify(curr_index=smallest)

    def _perc_up(self, curr_index):
        if curr_index > 0:
            parent_idx = curr_index // 2
            if self.array[parent_idx] > self.array[curr_index]:
                temp = self.array[parent_idx]
                self.array[parent_idx] = self.array[curr_index]
                self.array[curr_index] = temp
                self._perc_up(parent_idx)

    @property
    def getMinValue(self):
        min_val = None
        if self.heap_size:
            min_val = self.array[0]
        return min_val

    @property
    def extractMinValue(self):
        min_val = None
        if self.heap_size:
            min_val = self.array[0]
            self.array[0], self.array[-1] = self.array[-1], self.array[0]
            self.array.pop(-1)
            self.heap_size -= 1
            self._min_heapify(curr_index=0)
        return min_val

    def decreaseKey(self, key, value):
        self.array[key] = value
        if value < self.getMinValue():
            self._perc_up(curr_index=key)

    def insertValue(self, value):
        self.array.append(value)
        self.heap_size += 1
        self._perc_up(curr_index=self.heap_size - 1)

    def __repr__(self):
        return str(self.array[: self.heap_size])

    def __str__(self):
        return self.__repr__()
