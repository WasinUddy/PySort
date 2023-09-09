from visualizer import SortVisualizer

class SelectionSort(SortVisualizer):
    """
    SelectionSort class that extends the SortVisualizer class to visualize the selection sort algorithm.

    Attributes:
        data (list): A list of integers to be sorted.
    """

    def __init__(self, data):
        """
        Constructor for the SelectionSort class.

        Args:
            data (list): A list of integers to be sorted.
        """
        super().__init__(data)

    def sort(self):
        """
        Implements the selection sort algorithm to sort the data in ascending order.
        During each pass, it identifies the smallest (or largest, depending on sorting order) 
        element from the unsorted segment of the list and swaps it with the first unsorted element.
        The visualization is updated after each comparison and swap.

        The algorithm divides the input list into two parts:
        - A sorted sublist which is built up from left to right at the front (left) of the list.
        - A sublist of the remaining unsorted items.
        """
        for i in range(len(self.data)):  # Outer loop to move the boundary of the unsorted segment
            min_idx = i  # Assume the minimum value is at the current index
            for j in range(i+1, len(self.data)):  # Inner loop to iterate over the unsorted segment
                if self.data[j] < self.data[min_idx]:  # If a smaller value is found
                    min_idx = j  # Update the minimum index
                self.update()  # Update the visualization after each comparison
            # Swap the found minimum element with the first element of the unsorted segment
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            # Update the visualization after the swap
            self.update(i, min_idx)
