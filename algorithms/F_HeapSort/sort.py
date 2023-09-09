from visualizer import SortVisualizer

class HeapSort(SortVisualizer):
    """
    HeapSort class that extends the SortVisualizer class to visualize the heap sort algorithm.

    Attributes:
        data (list): A list of integers to be sorted.
    """

    def __init__(self, data):
        """
        Constructor for the HeapSort class.

        Args:
            data (list): A list of integers to be sorted.
        """
        super().__init__(data)

    def sort(self):
        """
        Implements the heap sort algorithm to sort the data in ascending order.
        The method first builds a max heap and then extracts the maximum element (root of the heap)
        repeatedly to get the sorted list.

        The visualization is updated after each swap.
        """
        n = len(self.data)
        
        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)
        
        # Extract elements from the heap one by one
        for i in range(n-1, 0, -1):
            # Move the current root (maximum element) to the end of the list
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.update(i, 0)
            
            # Call _heapify on the reduced heap
            self._heapify(i, 0)

    def _heapify(self, n, i):
        """
        Utility function to turn the subtree rooted at index i into a max heap, 
        assuming the subtrees rooted at its children are already max heaps.

        Args:
            n (int): Total number of elements in the heap.
            i (int): Index of the current node.
        """
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # Left child index
        r = 2 * i + 2  # Right child index
        
        # Check if left child exists and is greater than root
        if l < n and self.data[i] < self.data[l]:
            largest = l
        
        # Check if right child exists and is greater than the largest so far
        if r < n and self.data[largest] < self.data[r]:
            largest = r
        
        # If the largest is not root
        if largest != i:
            # Swap the root with the largest child
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.update(i, largest)
            
            # Recursively heapify the affected subtree
            self._heapify(n, largest)
