from visualizer import SortVisualizer

class QuickSort(SortVisualizer):
    """
    QuickSort class that extends the SortVisualizer class to visualize the quick sort algorithm.

    Attributes:
        data (list): A list of integers to be sorted.
    """

    def __init__(self, data):
        """
        Constructor for the QuickSort class.

        Args:
            data (list): A list of integers to be sorted.
        """
        super().__init__(data)

    def sort(self):
        """
        Public method to initiate the quick sort algorithm.
        """
        self._quicksort(0, len(self.data) - 1)

    def _quicksort(self, low, high):
        """
        Private recursive method to perform the quick sort.

        Args:
            low (int): Starting index of the segment to be sorted.
            high (int): Ending index of the segment to be sorted.
        """
        if low < high:
            pivot_index = self._partition(low, high)
            self._quicksort(low, pivot_index)
            self._quicksort(pivot_index + 1, high)

    def _partition(self, low, high):
        """
        Private method to partition the segment of the list using the pivot. 
        Elements smaller than the pivot will be on the left, and elements greater than the pivot will be on the right.

        Args:
            low (int): Starting index of the segment to be partitioned.
            high (int): Ending index of the segment to be partitioned.

        Returns:
            int: The index position of the pivot after partitioning.
        """
        pivot = self.data[low]
        left = low + 1
        right = high
        done = False

        while not done:
            # Increment 'left' index while the element at 'left' is less than the pivot
            while left <= right and self.data[left] <= pivot:
                left = left + 1
                self.update()

            # Decrement 'right' index while the element at 'right' is greater than the pivot
            while self.data[right] >= pivot and right >= left:
                right = right - 1
                self.update()

            # If there is an element larger on the left of the pivot and an element smaller on the right, swap them
            if right < left:
                done = True
            else:
                self.data[left], self.data[right] = self.data[right], self.data[left]
                self.update(left, right)

        # Swap the pivot with the element at the 'right' index
        self.data[low], self.data[right] = self.data[right], self.data[low]
        self.update(low, right)

        return right
