import numpy as np
import matplotlib.pyplot as plt


def display_arc_task(task):
    """
    Display the input and output images for an ARC task.

    :param task: A dictionary containing 'train' and 'test' lists of input-output pairs.
    """
    # Display training examples
    for i, pair in enumerate(task['train']):
        display_io_pair(pair, title=f"Training Example {i+1}")

    # Display test examples
    for i, pair in enumerate(task['test']):
        display_io_pair(pair, title=f"Test Example {i+1}")


def display_io_pair(pair, title):
    """
    Display an input-output pair.

    :param pair: A dictionary containing 'input' and 'output' grids.
    :param title: The title for the plot.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle(title)

    display_grid(pair['input'], ax1, "Input")
    display_grid(pair['output'], ax2, "Output")

    plt.show()


def display_grid(grid, ax, title):
    """
    Display a single grid (input or output) on the given axis.

    :param grid: A 2D list representing the colored grid.
    :param ax: The matplotlib axis to plot on.
    :param title: The title for this grid.
    """
    ax.imshow(grid, cmap='tab10', vmin=0, vmax=9)
    ax.set_title(title)
    ax.axis('off')

    # Add grid lines
    for i in range(len(grid)):
        ax.axhline(i - 0.5, color='black', linewidth=0.5)
    for j in range(len(grid[0])):
        ax.axvline(j - 0.5, color='black', linewidth=0.5)
