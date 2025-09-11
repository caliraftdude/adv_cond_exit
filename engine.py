"""
Integrated Game Engine with Resource Loading
Shows how to use the Game API with the Resource Loader
"""

import logging
from pathlib import Path
from typing import Optional, Union

from game import Game
from resource_loader import ResourceLoader

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Engine:
    """
    Game engine that integrates the Game API with dynamic resource loading.
    """
    
    def __init__(self):
        """Initialize the integrated game engine"""
        self.game = Game()
        self.resource_loader = ResourceLoader(self.game)
        self.module_path: Optional[Path] = None
        
    def load_game_module(self, module_path: Union[str, Path]) -> bool:
        """
        Load a complete game module.
        
        Args:
            module_path: Path to the game module directory (e.g., "Deadline/")
            
        Returns:
            True if successful
        """
        try:
            # Convert to Path object
            path = Path(module_path)
            
            if not path.exists():
                logger.error(f"Game module path does not exist: {path}")
                return False
            
            if not path.is_dir():
                logger.error(f"Game module path is not a directory: {path}")
                return False
            
            # Check for game.json
            manifest_file = path / "game.json"
            if not manifest_file.exists():
                logger.error(f"No game.json found in {path}")
                return False
            
            # Load the module
            logger.info(f"Loading game module from {path}")
            self.module_path = path
            
            # Use the resource loader
            success = self.resource_loader.load_game_module(path)
            
            if success:
                logger.info("Game module loaded successfully")
                self._post_load_initialization()
            else:
                logger.error("Failed to load game module")
            
            return success
            
        except Exception as e:
            logger.error(f"Error loading game module: {e}")
            return False
    
    def _post_load_initialization(self) -> None:
        """Perform initialization after loading resources"""
        try:
            # Initialize player object if not exists
            if "PLAYER" not in self.game.objects:
                from .game_api import GameObject
                player = GameObject(
                    id="PLAYER",
                    name="yourself",
                    description="As good looking as ever.",
                    location=self.game.HERE,
                    flags={"PERSON", "TRANSPARENT"}
                )
                self.game.objects["PLAYER"] = player
            
            # Set initial game state
            if "WELCOMED" not in self.game.globals:
                self.game.globals["WELCOMED"] = False
            
            # Initialize special globals for Deadline
            self._init_deadline_specifics()
            
            logger.info("Post-load initialization complete")
            
        except Exception as e:
            logger.error(f"Error in post-load initialization: {e}")
    
    def _init_deadline_specifics(self) -> None:
        """Initialize Deadline-specific game elements"""
        # These would normally be in the JSON data, but we can set defaults
        deadline_defaults = {
            "MURDERER": None,
            "MURDER-TIME": 0,
            "EVIDENCE-COUNT": 0,
            "ACCUSATION-MADE": False,
            "CASE-SOLVED": False,
            "SCORE": 0
        }
        
        for key, value in deadline_defaults.items():
            if key not in self.game.globals:
                self.game.globals[key] = value
    
    def execute_action(self, obj_id: str, rarg: Optional[str] = None) -> Optional[bool]:
        """
        Execute an action handler for an object or room.
        
        Args:
            obj_id: Object or room ID
            rarg: Optional routine argument (e.g., "M-LOOK", "M-ENTER")
            
        Returns:
            Result from action handler or None
        """
        try:
            # Get the object or room
            obj = self.game._get_object_or_room(obj_id)
            if not obj:
                logger.warning(f"Object/room not found: {obj_id}")
                return None
            
            # Check if it has an action handler
            if hasattr(obj, 'action_handler') and obj.action_handler:
                # Call the action handler with the game instance
                if rarg:
                    result = obj.action_handler(self.game, rarg)
                else:
                    result = obj.action_handler(self.game)
                
                logger.debug(f"Executed action for {obj_id}: {result}")
                return result
            
            # Try to find handler in registry
            handler_name = f"{obj_id}_F"
            handler = self.resource_loader.get_action(handler_name, obj)
            
            if handler:
                if rarg:
                    result = handler(self.game, rarg)
                else:
                    result = handler(self.game)
                
                logger.debug(f"Executed registered action for {obj_id}: {result}")
                return result
            
            logger.debug(f"No action handler found for {obj_id}")
            return None
            
        except Exception as e:
            logger.error(f"Error executing action for {obj_id}: {e}")
            return None
    
    def process_verb_on_object(self, verb: str, obj_id: str, 
                               indirect_obj: Optional[str] = None) -> bool:
        """
        Process a verb action on an object.
        
        Args:
            verb: Verb/action to perform
            obj_id: Direct object ID
            indirect_obj: Optional indirect object ID
            
        Returns:
            True if action was handled
        """
        try:
            # Set up parser state
            self.game.PRSA = verb
            self.game.PRSO = obj_id
            self.game.PRSI = indirect_obj
            
            # Try object's action handler
            result = self.execute_action(obj_id)
            
            if result is not None:
                return bool(result)
            
            # Try room's action handler
            result = self.execute_action(self.game.HERE)
            
            if result is not None:
                return bool(result)
            
            # Try global handlers
            global_handler = self.resource_loader.get_action(f"GLOBAL_{verb}")
            if global_handler:
                result = global_handler(self.game)
                return bool(result) if result is not None else False
            
            return False
            
        except Exception as e:
            logger.error(f"Error processing verb {verb} on {obj_id}: {e}")
            return False
    
    def reload_actions(self, module_name: str = "actions") -> bool:
        """
        Reload action handlers (useful for development).
        
        Args:
            module_name: Name of module to reload
            
        Returns:
            True if successful
        """
        return self.resource_loader.reload_module(module_name)
    
    def get_game_info(self) -> dict:
        """Get information about the loaded game"""
        return {
            "module_path": str(self.module_path) if self.module_path else None,
            "rooms_loaded": len(self.game.rooms),
            "objects_loaded": len(self.game.objects),
            "actions_registered": len(self.resource_loader.action_registry.actions),
            "current_location": self.game.HERE,
            "game_time": self.game.PRESENT_TIME,
            "score": self.game.globals.get("SCORE", 0),
            "max_score": self.game.globals.get("MAX_SCORE", 100)
        }


# Example usage
def example_usage():
    """Example of how to use the integrated game engine"""
    
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create engine
    engine = Engine()
    
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
    example_usage()