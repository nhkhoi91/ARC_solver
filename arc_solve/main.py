from display import display_arc_task
from load_data import load_and_combine_arc_data

if __name__ == "__main__":
    # Sample ARC task data
    sample_task = {
        'train': [
            {
                'input': [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                'output': [[0, 1, 2, 0], [3, 4, 5, 1], [6, 7, 8, 2], [0, 1, 2, 3]]
            }
        ],
        'test': [
            {
                'input': [[1, 2, 3], [4, 5, 6]],
                'output': [[1, 2, 3, 1], [4, 5, 6, 2], [1, 2, 3, 3]]
            }
        ]
    }

    display_arc_task(sample_task)