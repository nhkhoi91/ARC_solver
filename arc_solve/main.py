from display import display_arc_task
from load_data import load_and_combine_arc_data, get_arc_data_dir

if __name__ == "__main__":
    # Sample ARC task data
    train_task = load_and_combine_arc_data(get_arc_data_dir(), 'training')
    first_item = dict(next(iter(train_task.values())))
    print(first_item)
    display_arc_task(first_item)
