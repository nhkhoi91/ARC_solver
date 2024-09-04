def convert_to_relational(task):
    """
    Convert an ARC task to relational format.

    :param task: A dictionary containing 'train' and 'test' lists of input-output pairs.
    :return: A dictionary with the same structure, but with relational representations.
    """
    relational_task = {
        'train': [convert_pair(pair) for pair in task['train']],
        'test': [convert_pair(pair) for pair in task['test']]
    }
    return relational_task


def convert_pair(pair):
    """
    Convert a single input-output pair to relational format.

    :param pair: A dictionary containing 'input' and 'output' grids.
    :return: A dictionary with relational representations of input and output.
    """
    return {
        'input': convert_grid(pair['input'], 'in'),
        'output': convert_grid(pair['output'], 'out')
    }


def convert_grid(grid, prefix):
    """
    Convert a single grid to relational format.

    :param grid: A 2D list representing the colored grid.
    :param prefix: Either 'in' or 'out' to denote input or output.
    :return: A list of relational facts.
    """
    facts = []
    height = len(grid)
    width = len(grid[0])

    for x in range(height):
        for y in range(width):
            color = grid[x][y]
            if color != 0:  # Assuming 0 represents empty/background
                facts.append(f"{prefix}({x+1},{y+1},{color})")
            else:
                facts.append(f"empty({x+1},{y+1})")

    # Add height and width facts
    facts.append(f"height({height})")
    facts.append(f"width({width})")

    # Add midrow and midcol facts
    facts.append(f"midrow({(height + 1) // 2})")
    facts.append(f"midcol({(width + 1) // 2})")

    return facts


def convert_to_arc_format(relational_task):
    """
    Convert a relational representation of an ARC task back to the original ARC format.

    :param relational_task: A dictionary containing 'train' and 'test' lists of relational representations.
    :return: A dictionary with the same structure, but with grid representations.
    """
    arc_task = {
        'train': [convert_relational_pair(pair) for pair in relational_task['train']],
        'test': [convert_relational_pair(pair) for pair in relational_task['test']]
    }
    return arc_task


def convert_relational_pair(relational_pair):
    """
    Convert a single relational input-output pair back to grid format.

    :param relational_pair: A dictionary containing 'input' and 'output' relational representations.
    :return: A dictionary with grid representations of input and output.
    """
    return {
        'input': convert_relational_to_grid(relational_pair['input']),
        'output': convert_relational_to_grid(relational_pair['output'])
    }


def convert_relational_to_grid(relational_facts):
    """
    Convert a list of relational facts back to a 2D grid.

    :param relational_facts: A list of relational facts.
    :return: A 2D list representing the colored grid.
    """
    # Extract height and width
    height = next(int(f.split('(')[1].split(')')[0]) for f in relational_facts if f.startswith('height'))
    width = next(int(f.split('(')[1].split(')')[0]) for f in relational_facts if f.startswith('width'))

    # Initialize grid with zeros (empty/background)
    grid = [[0 for _ in range(width)] for _ in range(height)]

    # Fill in the grid based on the facts
    for fact in relational_facts:
        if fact.startswith(('in', 'out')):
            _, coords_color = fact.split('(')
            x, y, color = map(int, coords_color.split(')')[0].split(','))
            grid[x-1][y-1] = color  # Subtract 1 because relational facts use 1-based indexing

    return grid