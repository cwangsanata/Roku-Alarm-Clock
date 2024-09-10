import random
import yaml

def select_random(arr: list) -> int:
    return arr[random.randrange(0, len(arr))]

def load_yaml(file_path: str) -> any:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

