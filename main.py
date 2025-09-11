
"""
Test main function to work out the data objects and data files
"""
import logging
from pathlib import Path
from typing import Optional, Union

from .game import Game
from .resource_loader import ResourceLoader

from Deadline import load_config


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)




# Load the game.json file to find out the import list
config = load_config()

doors_json = load_config(config["doors"])
rooms_json = load_config(config["rooms"])

print(config["game_name"])


""" According to the AI, this is the way that the game gets loaded and initialized
Loading process:
1. ResourceLoader reads game.json manifest
2. Loads all JSON data files into Game objects
3. Dynamically imports Python modules (actions.py, etc.)
4. Registers all _F functions as action handlers
5. Wires action handlers to objects/rooms via "action" property
6. Objects/rooms can now respond to game events
"""


# Example usage
def main():
    """Example of how to use the integrated game engine"""
    
    # Create engine
    engine = IntegratedGameEngine()
    
    # Load the Deadline game module
    if engine.load_game_module("Deadline"):
        print("Game loaded successfully!")
        print(f"Game info: {engine.get_game_info()}")
        
        # Example: Execute room description
        engine.game.PRSA = "LOOK"
        result = engine.execute_action(engine.game.HERE, "M-LOOK")
        
        # Example: Process a verb on an object
        engine.process_verb_on_object("EXAMINE", "CALENDAR")
        
        # Example: Move player and describe new room
        engine.game.GOTO("LIVING-ROOM")
        engine.execute_action("LIVING-ROOM", "M-LOOK")
        
        # Example: Interact with an object
        engine.process_verb_on_object("TAKE", "LADDER")
        
    else:
        print("Failed to load game module")


if __name__ == "__main__":
    # Run the main entrypoint
    main()