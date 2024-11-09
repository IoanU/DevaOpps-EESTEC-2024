import json
from pathlib import Path

# Define the project root and config path
PROJECT_ROOT = Path("/usr/src/app")
CONFIG_PATH = PROJECT_ROOT / "config.json"

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

def load_config():
    """Load configuration and resolve paths relative to the PROJECT_ROOT."""
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
        
        # Resolve paths relative to the project root
        config["train_dir"] = PROJECT_ROOT / config["train_dir"]
        config["test_dir"] = PROJECT_ROOT / config["test_dir"]
        config["output_dir"] = PROJECT_ROOT / config["output_dir"]
        config["model_dir"] = PROJECT_ROOT / config["model_dir"]
        
        return config
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {CONFIG_PATH}: {e}")
        return {}
    except FileNotFoundError:
        print(f"Config file not found: {CONFIG_PATH}")
        return {}
