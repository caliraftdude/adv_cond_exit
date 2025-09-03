import json
import os

def load_config(filename="game.json"):
    """Load JSON configuration from the module directory."""
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, filename)
    
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Configuration file {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
    return {}


