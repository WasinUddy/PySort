from visualizer import SortVisualizer

class BubbleSort(SortVisualizer):
    """
    BubbleSort class that extends the SortVisualizer class to visualize the bubble sort algorithm.

    Attributes:
        data (list): A list of integers to be sorted.
    """

    def __init__(self, data):
        """
        Constructor for the BubbleSort class.

        Args:
            data (list): A list of integers to be sorted.
        """
        super().__init__(data)

    def sort(self):
        """
        Implements the bubble sort algorithm to sort the data in ascending order.
        During each pass, it compares adjacent elements and swaps them if they are in the wrong order.
        The process is repeated for each element in the list, ensuring the largest element bubbles up to its correct position.
        The visualization is updated after each swap or comparison.
        """
        for i in range(len(self.data) - 1):  # Outer loop for each pass
            for j in range(len(self.data) - 1 - i):  # Inner loop for comparing adjacent elements
                if self.data[j] > self.data[j + 1]:  # If the current element is greater than the next element
                    # Swap the elements
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    # Update the visualization with the swapped indices
                    self.update(j, j+1)
                else:
                    # Update the visualization without swapping
                    self.update()
