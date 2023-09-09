from visualizer import SortVisualizer

class MergeSort(SortVisualizer):
    """
    MergeSort class that extends the SortVisualizer class to visualize the merge sort algorithm.

    Attributes:
        data (list): A list of integers to be sorted.
    """

    def __init__(self, data):
        """
        Constructor for the MergeSort class.

        Args:
            data (list): A list of integers to be sorted.
        """
        super().__init__(data)

    def sort(self):
        """
        Public method to initiate the merge sort algorithm.
        """
        self._merge_sort(0, len(self.data) - 1)

    def _merge_sort(self, l, r):
        """
        Recursive method that divides the list into two halves, sorts them, 
        and then merges the sorted halves.

        Args:
            l (int): Starting index of the list segment.
            r (int): Ending index of the list segment.
        """
        if l < r:
            m = (l + r) // 2  # Calculate mid point of the list segment
            self._merge_sort(l, m)  # Sort the first half
            self._merge_sort(m + 1, r)  # Sort the second half
            self._merge(l, m, r)  # Merge the sorted halves

    def _merge(self, l, m, r):
        """
        Helper method to merge two sorted sublists into a single sorted sublist.

        Args:
            l (int): Starting index of the left sublist.
            m (int): Ending index of the left sublist (or mid-point).
            r (int): Ending index of the right sublist.
        """
        # Create temporary lists to hold the two sublists to be merged
        L = self.data[l:m+1]
        R = self.data[m+1:r+1]

        i = j = 0  # Initialize pointers for L and R
        k = l  # Initialize pointer for the main list

        # Merge the data back into the main list in sorted order
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                self.data[k] = L[i]
                i += 1
            else:
                self.data[k] = R[j]
                j += 1
            self.update()  # Update the visualization
            k += 1

        # If there are remaining elements in L, add them to the main list
        while i < len(L):
            self.data[k] = L[i]
            i += 1
            k += 1
            self.update()  # Update the visualization

        # If there are remaining elements in R, add them to the main list
        while j < len(R):
            self.data[k] = R[j]
            j += 1
            k += 1
            self.update()  # Update the visualization
