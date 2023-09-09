from visualizer import SortVisualizer

class InsertionSort(SortVisualizer):
    """
    InsertionSort class that extends the SortVisualizer class to visualize the insertion sort algorithm.

    Attributes:
        data (list): A list of integers or comparable elements to be sorted.
    """

    def __init__(self, data):
        """
        Constructor for the InsertionSort class.

        Args:
            data (list): A list of integers or comparable elements to be sorted.
        """
        super().__init__(data)

    def sort(self):
        """
        Implements the insertion sort algorithm to sort the data in ascending order.
        
        The algorithm works by building a sorted portion of the list one element at a time. 
        For each position, it checks the current element against the previous elements in the sorted portion.
        If the current element is smaller, it shifts the larger elements to the right until the correct position 
        for the current element is found. The current element is then inserted in its correct position.
        
        The visualization is updated after each shift or insertion.
        """
        for i in range(1, len(self.data)):  # Start from the second element
            key = self.data[i]  # Current element to be compared
            j = i - 1  # Start comparing with the element just before the current element

            # Shift elements of the sorted portion that are greater than 'key' to the right
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                self.update(j, j+1)  # Update the visualization with the shifted indices
                j -= 1  # Move to the previous element

            # Insert the 'key' in its correct position
            self.data[j + 1] = key
            self.update()  # Update the visualization after insertion
