import random
import yaml

def select_random(arr: list) -> int:
    try:
        return arr[random.randrange(0, len(arr))]
    except ValueError:
        raise IndexError('Cannot select random element from empty list')

def load_yaml(file_path: str) -> any:
    with open(file_path, 'r') as file:
        assert file, f'File {file_path} not found'
        return yaml.safe_load(file)

