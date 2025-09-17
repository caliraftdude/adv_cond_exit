import sys
import logging
import importlib
import importlib.util
import inspect
import json

from typing import Dict, Any, Optional, Callable
from pathlib import Path



from core.game_object import Manifest, Object, Room


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
        self.loaded_modules: Dict[str, Any] = {}
        self.function_registry: Dict[str, Callable] = {}
        self.objects: Dict[str, Object] = {}
        self.rooms: Dict[str, Room] = {}

        # Player
        #self.player: Optional[Player] = None
        
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
            logger.info(f"World initialized with  {len(self.objects)} objects , {len(self.rooms)} rooms, and {len(self.function_registry)} functions")
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
            objcount = len(self.objects)

            # XXX Some temp BS
            temp_dict:dict = dict()

            # Create Object instances
            for obj_name, obj_data in data.items():
                new_object = Object.from_json(obj_name, obj_data)

                self.objects[obj_name] = new_object
                logger.info(f"Created id [{new_object.id}]  object: {obj_name} ")

            
            logger.info(f"Loaded {len(self.objects)-objcount} objects from {objects_path}")
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