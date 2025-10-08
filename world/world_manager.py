"""
world_manager.py
Used to manage all the world objects




Notes:
GLOBAL and NON GLOBAL CHARACTERS
The dual object system (regular and GLOBAL- versions) in ZIL/Infocom games serves a specific and clever purpose for handling character 
references in different contexts. This is a common pattern in text adventure games to solve a particular problem.
The Problem They Solve
In text adventures, players need to be able to refer to characters in two distinct situations:

1. When the character is present in the current room (DUNBAR)
2. When talking/thinking about the character who isn't present (GLOBAL-DUNBAR)

Why Two Objects?
The Local Object (DUNBAR)
    Location: Specific room (LIVING-ROOM)
    Purpose: Represents the physical presence of the character
    Features:
        Has capacity (can carry items)
        Has state (for tracking character behavior)
        Has OPENBIT (can give/take items)
        Uses character-specific action handler (DUNBAR-F)

The Global Object (GLOBAL-DUNBAR)
    Location: GLOBAL-OBJECTS (always accessible)
    Purpose: Allows references when character isn't present
    Features:
        Minimal properties
        Uses generic action handler (GLOBAL-PERSON)
        Always available for parser matching

Why This Design?
1. Parser Flexibility: Players can always refer to any character
2. Contextual Responses: Game knows if you're talking TO someone vs ABOUT someone
3. Memory Efficiency: In 1982, having one object that moves around was more efficient than having copies in every room
4. Clean Separation: Physical presence vs conceptual reference

This pattern is common in text adventures and represents an elegant solution to the problem of allowing players to reference entities 
that may or may not be physically present in the current scene.

DIFFERENCE BETWEEN LOCAL-GLOBALS and GLOBAL-OBJECTS
The difference between GLOBAL-OBJECTS and LOCAL-GLOBALS relates to the scope of object accessibility in different parts of the game map.
GLOBAL-OBJECTS
Objects that are universally accessible from anywhere in the game. These represent:

    Abstract concepts (GLOBAL-MURDER, GLOBAL-SUICIDE)
    People you can talk about but aren't present (GLOBAL-MR-ROBNER)
    General references (GLOBAL-WEATHER, AIR, GROUND)
    Things that exist conceptually everywhere (INTNUM for number parsing)

LOCAL-GLOBALS
Objects that are accessible in multiple related rooms but not everywhere. These represent physical features shared across connected areas:

Why This Design?
    Memory Efficiency: In 1982, this saved memory by not duplicating objects
    Logical Grouping: Features naturally belong to certain area types
    Simpler Management: One TELEPHONE object serves all rooms with phones
    Consistent Behavior: Same sink behavior in all bathrooms

This three-tier system (Local → Local-Global → Global) provides a sophisticated way to manage object visibility and accessibility based 
on context, making the game world feel more coherent and realistic.




"""



import sys
import logging
import importlib
import importlib.util
import inspect
import json

from typing import Dict, Any, Optional, Callable
from pathlib import Path



from core.game_object import Manifest, Object, Room
from core.flags import ObjectFlag


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WorldManager:
    """
    Central manager for the game world
    Handles all objects, rooms, characters, and their interactions
    """
    
    
    def __init__(self, manifest: Manifest, data_path: Path):
        """Initialize world manager with game data"""
        self.manifest: Manifest = manifest
        self.data_path: Path = data_path

        # Object registries
        self.loaded_modules: Dict[str, Any] = {}            # not really needed
        self.function_registry: Dict[str, Callable] = {}

        self.objects: Dict[str, Object] = {}                # objects (local)
        self.local_globals: Dict[str, Object] = {}          # local global objects
        self.global_objects: Dict[str, Object] = {}         # global objects
        self.global_vars: Dict[str, Any] = {}               # Used to store global variables
        self.characters: Dict[str, Object] = {}             # Characters and the player

        self.rooms: Dict[str, Room] = {}

        # Player
        self.player: Optional[Object] = None                # The player
        
        # Subsystem managers
        #self.room_manager = RoomManager()
        #self.character_manager = CharacterManager()
        #self.evidence_manager = EvidenceManager()
            
        # Current state
        #self.current_room_id: Optional[str] = None


    def initialize_world(self):
        """Initialize the game world from data"""

        # Load resources in order
        success = True

        try:
            # 1. Load action module for action routines
            for module_name in self.manifest.action_files:
                if not self._load_python_module(module_name, self.data_path):
                    logger.warning(f"Failed to load action module: {module_name}")
                    success = False

            # 2. Load the objects (this includes doors)
            for obj_file in self.manifest.object_files:
                if not self._load_objects(self.data_path / obj_file):
                    logger.error("Failed to load objects")
                    success = False

            # 3. Load the room objects
            for room_file in self.manifest.room_files:
                if not self._load_rooms(self.data_path / room_file):
                    logger.error("Failed to load rooms")
                    success = False

            logger.info(f"Game module loaded: {success}")
            logger.info(f"World initialized with {len(self.objects)} objects, {len(self.local_globals)} local-globals, {len(self.global_objects)} global objects, {len(self.rooms)} rooms, and {len(self.function_registry)} functions")
            return success
        
        except Exception as e:
            logger.error(f"Error loading game module: {e}")
            return False

        # XXX Post processing needed after the data is loaded?
        # Create player
        self._create_player()
        
        # Create rooms
        self._create_rooms()
        
        # Create objects
        self._create_objects()
        
        # Create characters
        self._create_characters()
        
        # Set initial positions
        self._set_initial_positions()
        
        # Initialize managers
        # self.room_manager.initialize(self.rooms)
        # self.character_manager.initialize(self.characters)
        # self.evidence_manager.initialize(self.game_data.get('solution', {}))



    def _load_python_module(self, module_name: str, module_path: Path) -> bool:
        """
        Dynamically load a Python module containing action handlers.
        
        Args:
            module_name: Name of the module (without .py)
            module_type: Type of module (actions/events/custom)
            
        Returns:
            True if successful
        """
        try:
            # Construct module path
            module_file: Path = module_path / module_name

            if not module_file.exists():
                logger.debug(f"Module file not found: {module_file}")
                return False
            
            # Load the module dynamically
            spec = importlib.util.spec_from_file_location(
                f"deadline.game_modules.{module_name}",
                module_file
            )
            
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                
                # Add to sys.modules so it can be imported by other modules
                sys.modules[spec.name] = module
                
                # Execute the module
                spec.loader.exec_module(module)
                
                # Store the loaded module
                self.loaded_modules[module_name] = module
                
                # Register action handlers
                self._register_action_handlers(module)
            
                logger.info(f"Loaded Python module: {module_name}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error loading Python module {module_name}: {e}")
            return False
        

    def _register_action_handlers(self, module: Any) -> None:
        """
        Register action handlers from a module.  Looks for functions ending with _F (ZIL convention).
        """
        try:
            for name, obj in inspect.getmembers(module):
                # Look for functions ending with _F
                if callable(obj):
                    self.function_registry[name] = obj           
                    logger.info(f"Registered action handler: {name}")

            logger.info(f"Loaded {len(self.function_registry)} fucntions from module {module.__name__}")
                    
        except Exception as e:
            logger.error(f"Error registering action handlers: {e}")


    def _load_objects(self, objects_path: Path) -> bool:
        """Load object data"""

        try:
            if not objects_path.exists():
                logger.debug(f"Objects file not found: {objects_path}")
                return False
            
            with open(objects_path, 'r') as f:
                data:Dict = json.load(f)
            
            # Other ways to do this - but this is fine
            objcount: int = 0

            # Create Object instances
            for obj_name, obj_data in data.items():
                new_object = Object.from_json(obj_name, obj_data)

                # Need to determine the correct location to put the objects into
                # It may be unnecessary to do this and just do heavy searching on query
                if new_object.location == "GLOBAL-OBJECTS":
                    self.global_objects[obj_name] = new_object
                    logger.info(f"Created id [{new_object.id}]  object: {obj_name} put into GLOBAL-OBJECTS")

                elif new_object.location == "LOCAL-GLOBALS":
                    self.local_globals[obj_name] = new_object
                    logger.info(f"Created id [{new_object.id}]  object: {obj_name} put into LOCAL-GLOBALS")

                elif ObjectFlag.PERSON in new_object.flags:
                    if new_object.character == 0:
                        self.player = new_object
                        logger.info(f"Created id [{new_object.id}]  object: {obj_name} Player object created")
                    else:
                        self.characters[obj_name] = new_object
                        logger.info(f"Created id [{new_object.id}]  object: {obj_name} put into characters")
                else:
                    self.objects[obj_name] = new_object
                    logger.info(f"Created id [{new_object.id}]  object: {obj_name} put into objects")

                objcount = objcount+1
                
            
            logger.info(f"Loaded {objcount} objects from {objects_path}")
            return True
        
        except Exception as e:
            logger.error(f"Error loading objects: {e}")
            return False

    def _load_rooms(self, rooms_path: Path) -> bool:
        """Load room data"""
        try:
            if not rooms_path.exists():
                logger.debug(f"Rooms file not found: {rooms_path}")
                return False
            
            with open(rooms_path, 'r') as f:
                data = json.load(f)
            
            # Other ways to do this - but this is fine
            objcount = len(self.rooms)

            # Create Room objects
            for room_name, room_data in data.items():
                new_room = Room.from_json(room_name, room_data)

                self.rooms[room_name] = new_room
                logger.info(f"Created id [{new_room.id}]  room: {room_name} ")
            
            logger.info(f"Loaded {len(self.rooms)-objcount} rooms from {rooms_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading rooms: {e}")
            return False





    def _create_player(self):
        """Create the player character"""
        pass

    def _load_module(self, module_name: str):
        """Dynamically load a module by name"""
        pass