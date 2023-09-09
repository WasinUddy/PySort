import matplotlib.pyplot as plt

class SortVisualizer:
    """
    A class for visualizing sorting algorithms on a set of data using Matplotlib.
    
    Attributes:
        data (list): The input data to be visualized and sorted.
        fig (matplotlib.figure.Figure): The Matplotlib figure for the visualization.
        ax (matplotlib.axes.Axes): The Matplotlib axis for the visualization.
        bar_rects (list): A list of bar rectangles representing the data elements in the visualization.
    """

    def __init__(self, data):
        """
        Initialize the SortVisualizer object.

        Args:
            data (list): A list of numerical data to be visualized and sorted.
        """
        self.data = data
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(data)), data)
        self.ax.set_xlim(0, len(data))
        self.ax.set_ylim(0, int(1.1 * max(data)))

    def update(self, swap1=None, swap2=None):
        """
        Update the visualization during sorting.

        Args:
            swap1 (int, optional): Index of the first element to be swapped (default: None).
            swap2 (int, optional): Index of the second element to be swapped (default: None).
        """
        for rect, val in zip(self.bar_rects, self.data):
            rect.set_height(val)

        if swap1 is not None and swap2 is not None:
            self.bar_rects[swap1].set_color('r')
            self.bar_rects[swap2].set_color('g')
        else:
            for rect in self.bar_rects:
                rect.set_color('b')

        plt.pause(0.02)
        self.fig.canvas.draw()

    def sort(self):
        """
        Sort method for sorting the data elements.
        This method should be implemented in derived classes.
        """
        raise NotImplementedError("Sort method not implemented!")

    def do_visual_sort(self):
        """
        Execute the sorting process and display the visualization.
        """
        plt.ion()
        self.sort()
        plt.ioff()
        plt.show()
