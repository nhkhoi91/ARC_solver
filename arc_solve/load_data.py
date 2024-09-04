import json
import os


def get_arc_data_dir():
    """
    Get the path to the ARC data directory.
    """
    current_dir = os.getcwd()
    data_dir = os.path.join(current_dir, 'data')
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found at {data_dir}")

    return data_dir


def load_and_combine_arc_data(base_dir, dataset_type):
    """
    Load and combine ARC challenge and solution data from JSON files.

    :param base_dir: The base directory of the ARC data
    :param dataset_type: The type of dataset to load (e.g. 'training', 'evaluation', 'test')
    :return: A dictionary with task IDs as keys and a dictionary containing the 'train' and 'test' data for each task
    """
    challenges_file = os.path.join(base_dir, 'original', dataset_type, f'arc-agi_{dataset_type}_challenges.json')
    solutions_file = os.path.join(base_dir, 'original', dataset_type, f'arc-agi_{dataset_type}_solutions.json')

    challenges = None
    with open(challenges_file, 'r') as f:
        challenges = json.load(f)

    solutions = None
    with open(solutions_file, 'r') as f:
        solutions = json.load(f)

    combined_data = {}
    for task_id, challenge_data in challenges.items():
        combined_data[task_id] = {
            'train': challenge_data.get('train', []),
            'test': []
        }

        # Process test data and add solutions
        for i, test_item in enumerate(challenge_data.get('test', [])):
            test_with_solution = {
                'input': test_item['input'],
                'output': solutions.get(task_id, [])[i] if task_id in solutions and i < len(solutions[task_id]) else None
            }
            combined_data[task_id]['test'].append(test_with_solution)

    return combined_data
