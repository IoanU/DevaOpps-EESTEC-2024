import json

def load_json(filepath):
    """Load JSON data from a file."""
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(data, filepath):
    """Save data to a file in JSON format."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

