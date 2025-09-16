###############################################################################
#   core/game_object.py
#
#   Base game object classes - translated from ZIL object system
#   XXX Implements the core object hierarchy and property system
#   
###############################################################################
from typing import Dict, List, Any, Optional, Set, TYPE_CHECKING, Tuple, Callable, ClassVar
from dataclasses import dataclass, field
from enum import Flag, auto, Enum
import json
import logging

# temp imports while authoring
from pathlib import Path
from typing import Optional, Union
import importlib
import importlib.util
import sys
import inspect
from functools import reduce
import operator

from core.flags import ObjectFlag
from core.exceptions import ResourceLoadError

#if TYPE_CHECKING:
    #from .property_system import PropertyManager

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



@dataclass
class BaseObj:
    """
    Base object class for all objects and elements within the game.
    """
    _classid: ClassVar[int] = 0  # Class variable to assign unique IDs

    id: int = field(default_factory=lambda: BaseObj._getObjectID())     # Unique identifier
    name: str  = str()                                                  # Short name (DESC in ZIL)
    description: str = str()                                            # Long description (LDESC)
    flags: ObjectFlag = ObjectFlag.NONE
    
    # Vocabulary - for parser matching
    synonyms: List[str] = field(default_factory=list)       # Alternative names
    adjectives: List[str] = field(default_factory=list)     # Descriptive words

    # Action handler - equivalent to ZIL's ACTION property
    action_handler: Optional[Callable] = None               # Name of action routine

    @staticmethod
    def _getObjectID() -> int:
            """Get a unique object ID"""
            BaseObj._classid += 1
            return BaseObj._classid

    @staticmethod
    def _parse_flags(flag_list):
        if not flag_list:
            return ObjectFlag.NONE
        
        flags = [ObjectFlag[flag] for flag in flag_list if flag in ObjectFlag.__members__]
        return reduce(operator.or_, flags) if flags else ObjectFlag.NONE
    

@dataclass
class Object(BaseObj) :
    """
    Game Object class for all game objects.  Equivalent to ZIL OBJECT definition
    """
    # Core properties - match ZIL object properties
    initial_description: str = str()                        # First-time description (FDESC)
    
    # Containment hierarchy - ZIL's IN/LOC system
    location: Optional['Object'] = None                     # Where this object is (LOC)
    contents: List['Object'] = field(default_factory=list)  # What's inside
    
    # Properties dictionary - ZIL's property system
    properties: Dict[str, Any] = field(default_factory=dict)
    
    # State tracking
    _original_location: Optional['Object'] = None
    _state_variables: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, obj_id: str, obj_data: Dict[str, Any]) -> 'Object':
        # Load object from JSON file
        try:
            # Create Object instance
            obj = cls(
                name=obj_id,
                description=obj_data.get("description", ""),
                flags=Object._parse_flags(obj_data.get("flags", [])),
                synonyms=obj_data.get("synonyms", []),
                adjectives=obj_data.get("adjectives", []),            
                location=obj_data.get("location"),
                action_handler=obj_data.get("action"),
                
                properties=obj_data.get("properties", {}),
                contents=obj_data.get("contents", [])
            )
            return obj
        
        except Exception as e:
            logger.error(f"Failed to load object {obj_id} with {obj_data}: {e}")
            raise ResourceLoadError(f"Cannot load object: {e}")

    @staticmethod
    def _load_objects(objects_path: Path) -> bool:
        """Load object data"""

        try:
            if not objects_path.exists():
                logger.debug(f"Objects file not found: {objects_path}")
                return False
            
            with open(objects_path, 'r') as f:
                data = json.load(f)
            
            # Other ways to do this - but this is fine
            objcount = len(objects)

            # Create Object instances
            for obj_name, obj_data in data.items():
                new_object = Object.from_json(obj_name, obj_data)

                objects[obj_name] = new_object
                logger.info(f"Created id [{new_object.id}]  object: {obj_name} ")

            
            logger.info(f"Loaded {len(objects)-objcount} objects from {objects_path}")
            return True
        
        except Exception as e:
            logger.error(f"Error loading objects: {e}")
            return False



class ExitType(Enum):
    """Enumeration of exit types in the game"""
    NORMAL = auto()      # Standard exit to another room
    DOOR = auto()        # Exit through a door object
    NON_EXIT = auto()    # Blocked exit with message
    CONDITIONAL = auto() # Exit with condition check


@dataclass
class Exit:
    """Class representing an exit from a room"""
    name: str = str()                           # Name of the exit (e.g., "north", "south")

@dataclass
class Normal_Exit(Exit):
    """Normal exit to another room """
    type: ExitType = ExitType.NORMAL            # Type of exit  (NORMAL)
    dest: str = str()                           # Destination room ID for NORMAL exits

@dataclass
class Non_Exit(Exit):
    """Non-exit with message"""
    type: ExitType = ExitType.NON_EXIT          # Type of exit  (NON_EXIT)
    message: str = str()                        # Message for NON_EXIT exits

@dataclass
class Door_Exit(Exit):
    """Exit through a door object"""
    type: ExitType = ExitType.DOOR              # Type of exit  (DOOR)
    dest: str = str()                           # Destination room ID for NORMAL exits
    door_obj: str = str()                       # Door object ID for DOOR exits

@dataclass
class Conditional_Exit(Exit):
    """Conditional exit with check function"""
    type: ExitType = ExitType.CONDITIONAL       # Type of exit  (CONDITIONAL)
    dest: str = str()                           # Destination room ID for CONDITIONAL exits
    cond_var: str = str()                       # Condition variable name
    message: str = str()                        # Failure message for COND_EXIT exits


@dataclass
class Naviagation:
    """
    Navigation aids for rooms, such as lines, stations, corridors.  This simplifies Room class definition and object creation
    """
    line: Optional[int] = None
    station: Optional[str] = None
    corridor: Optional[int] = None


@dataclass
class Room(BaseObj):
    """
    Room class - represents locations in the game.  Equivalent to ZIL rooms with special properties
    """
    exits: Dict[str, Exit] = field(default_factory=dict)                 # direction -> room_id
    global_objects: List[str] = field(default_factory=list)              # Objects always present
    navigation: Naviagation = field(default_factory=Naviagation)               # Navigation aids

    @classmethod
    def from_json(cls, room_name: str, room_data: Dict[str, Any]) -> 'Room':
        # Load Room from JSON file
        try:
            room = cls(
                name=room_name,
                description=room_data.get("description", ""),
                flags=Room._parse_flags(room_data.get("flags", [])),
                synonyms=room_data.get("synonyms", []),
                adjectives=room_data.get("adjectives", []),   
                action_handler=room_data.get("action"),

                exits=Room.parse_exits(room_data.get("exits", {}) ),
                global_objects=room_data.get("global_objects", []),
                navigation=Naviagation(line=room_data.get("navigation", {}).get("line"),
                                    station=room_data.get("navigation", {}).get("station"), 
                                    corridor=room_data.get("navigation", {}).get("corridor")),

            )

            return room

        
        except Exception as e:
            logger.error(f"Failed to load room {room_name} with {room_data}: {e}")
            raise ResourceLoadError(f"Cannot load room: {e}")


    @staticmethod
    def parse_exits(exits_data: Dict[str, Any]) -> Dict[str, Exit]:
        """Parse exits from JSON data into Exit objects"""
        exits = {}

        for direction, exit_info in exits_data.items():
            if isinstance(exit_info, str):
                # Normal exit
                exits[direction] = Normal_Exit(name=direction, dest=exit_info)

            elif isinstance(exit_info, dict):
                exit_type = exit_info.get("type")

                if exit_type == "door":
                    exits[direction] = Door_Exit(
                        name=direction,
                        dest=exit_info.get("dest", ""),
                        door_obj=exit_info.get("door_obj", "")
                    )
                elif exit_type == "non_exit":
                    exits[direction] = Non_Exit(
                        name=direction,
                        message=exit_info.get("message", "You can't go that way.")
                    )
                elif exit_type == "conditional":
                    exits[direction] = Conditional_Exit(
                        name=direction,
                        dest=exit_info.get("dest", ""),
                        cond_var=exit_info.get("cond_var", ""),
                        message=exit_info.get("message", "You can't go that way.")
                    )
        return exits

    @staticmethod
    def _load_rooms(rooms_path: Path) -> bool:
        """Load room data"""
        try:
            if not rooms_path.exists():
                logger.debug(f"Rooms file not found: {rooms_path}")
                return False
            
            with open(rooms_path, 'r') as f:
                data = json.load(f)
            
            # Other ways to do this - but this is fine
            objcount = len(rooms)

            # Create Room objects
            for room_name, room_data in data.items():
                new_room = Room.from_json(room_name, room_data)

                rooms[room_name] = new_room
                logger.info(f"Created id [{new_room.id}]  room: {room_name} ")
            
            logger.info(f"Loaded {len(rooms)-objcount} rooms from {rooms_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading rooms: {e}")
            return False



@dataclass
class Manifest:
    """
    Describes all resources to be loaded for a game module.
    This is typically loaded from game.json
    """
    game_name: str
    version: str
    description: str = ""
    author: str = ""
    difficulty: str = ""

    # Resource files
    object_files: List[str] = field(default_factory=list)
    room_files: List[str] = field(default_factory=list)
    action_files: List[str] = field(default_factory=list)
 
    # Additional configuration
    config: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_json(cls, json_path: Path) -> 'Manifest':
        """Load manifest from JSON file"""
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            # Map JSON keys to manifest fields
            return cls(
                game_name=data.get("game_name", "XXX"),
                version=data.get("version", "0.0.0"),
                description=data.get("description", ""),
                author=data.get("author", ""),
                difficulty=data.get("difficulty", ""),
                object_files=data.get("objects", ["objects.json"]),
                room_files=data.get("rooms", ["rooms.json"]),
                action_files=data.get("actions", ["actions.py"]),
                config=data.get("config", {})
            )
        except Exception as e:
            logger.error(f"Failed to load manifest from {json_path}: {e}")
            raise ResourceLoadError(f"Cannot load manifest: {e}")


#game = game
manifest: Optional[Manifest] = None
function_registry: Dict[str, Callable] = {}
loaded_modules: Dict[str, Any] = {}
objects: Dict[str, Object] = {}
rooms: Dict[str, Room] = {}


def load_game_module(module_path: Union[str, Path]) -> bool:
    """
    Load a complete game module with all its resources.
    Args:
        module_path: Path to the game module directory
    """
    
    try:
        global manifest 

        manifest = Manifest.from_json(Path(module_path) / "game.json")
        logger.info(f"Loaded manifest for game: {manifest.game_name} v{manifest.version}")

        # Load resources in order
        success = True

        # 1. Load action module for action routines
        for module_name in manifest.action_files:
            if not _load_python_module(module_name, module_path):
                logger.warning(f"Failed to load action module: {module_name}")
                success = False

        # 2. Load the objects (this includes doors)
        for obj_file in manifest.object_files:
            if not Object._load_objects(module_path / obj_file):
                logger.error("Failed to load objects")
                success = False

        # 3. Load the room objects
        for room_file in manifest.room_files:
            if not Room._load_rooms(module_path / room_file):
                logger.error("Failed to load rooms")
                success = False


        logger.info(f"Game module loaded: {success}")
        logger.info(f"Loaded {len(objects)} objects , {len(rooms)} rooms, and {len(function_registry)} functions")
        return success
        
    except Exception as e:
        logger.error(f"Error loading game module: {e}")
        return False


def _load_python_module(module_name: str, module_path: Path) -> bool:
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
            loaded_modules[module_name] = module
            
            # Register action handlers
            _register_action_handlers(module)
         
            logger.info(f"Loaded Python module: {module_name}")
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error loading Python module {module_name}: {e}")
        return False


def _register_action_handlers(module: Any) -> None:
    """
    Register action handlers from a module.  Looks for functions ending with _F (ZIL convention).
    """
    try:
        for name, obj in inspect.getmembers(module):
            # Look for functions ending with _F
            if callable(obj):
                function_registry[name] = obj           
                logger.info(f"Registered action handler: {name}")

        logger.info(f"Loaded {len(function_registry)} fucntions from module {module.__name__}")
                
    except Exception as e:
        logger.error(f"Error registering action handlers: {e}")






if __name__ == "__main__":
    fp = Path("./Deadline")
    load_game_module(fp)


