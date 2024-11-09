import json
import os

def load_json(filepath):
    """
    Load JSON data from a file.
    :param filepath: Path to the JSON file.
    :return: Parsed JSON data as a dictionary.
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filepath}: {e}")
        return {}
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return {}

def save_json(data, filepath):
    """
    Save data to a file in JSON format.
    :param data: Data to save (dict or list).
    :param filepath: Path to the output JSON file.
    """
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filepath}")
    except IOError as e:
        print(f"Error saving JSON to {filepath}: {e}")

def list_json_files(directory):
    """
    List all JSON files in a directory.
    :param directory: Path to the directory.
    :return: List of JSON file paths.
    """
    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_files.append(os.path.join(directory, filename))
    return json_files

