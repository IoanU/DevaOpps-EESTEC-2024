import json
from pathlib import Path

# Define the project root and config path
PROJECT_ROOT = Path("/usr/src/app")
CONFIG_PATH = Path("/usr/src/app/source/config.json")

def load_json(filepath):
    """Load JSON data from a file."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading JSON from {filepath}: {e}")
        return {}

def save_json(data, filepath):
    """Save data to a file in JSON format."""
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filepath}")
    except IOError as e:
        print(f"Error saving JSON to {filepath}: {e}")

def list_json_files(directory):
    """List all JSON files in a directory."""
    directory = Path(directory)
    return [file for file in directory.iterdir() if file.suffix == '.json']

