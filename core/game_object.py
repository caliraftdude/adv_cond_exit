###############################################################################
#   core/game_object.py
#
#   Base game object classes - translated from ZIL object system
#   XXX Implements the core object hierarchy and property system
#   
###############################################################################
import json
import logging
import operator
from typing import ClassVar, List, Dict, Optional, Callable, Any, Set
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from functools import reduce


from core.flags import ObjectFlag
from core.exceptions import ResourceLoadError



# from typing import Dict, List, Any, Optional, Set, TYPE_CHECKING, Tuple, Callable, ClassVar
# from enum import Flag, auto, Enum
# from typing import Optional, Union
# import importlib
# import importlib.util
# import sys
# import inspect

#if TYPE_CHECKING:  - avoid loops and type checking wanks
    #from .property_system import PropertyManager

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
    location: Optional['Object'] = None                                 # Where this object is (LOC)

    # Vocabulary - for parser matching
    synonyms: List[str] = field(default_factory=list)       # Alternative names
    adjectives: List[str] = field(default_factory=list)     # Descriptive words

    # Action handler - equivalent to ZIL's ACTION property
    action: Optional[Callable] = None               # Name of action routine

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
    fdesc: str = str()                          # First-time description (FDESC), not in people or doors
    capacity: int = 0                           # All but doors
    text: str = str()                           # All but doors

    count: int = 0                              # Only in drugs
    descfcn: Optional[Callable] = None           # Only evidence and people
    ldesc: str = str()                          # gobjects and objects
    character: int = 0                          # Only people
    state: int = 0                              # Only people
    size: int = 0                               # All but doors, objects, and people
    
    # Containment hierarchy - ZIL's IN/LOC system
    
    #contents: List['Object'] = field(default_factory=list)  # What's inside
    
    # Properties dictionary - ZIL's property system
    #properties: Dict[str, Any] = field(default_factory=dict)
    
    # State tracking
    #_original_location: Optional['Object'] = None
    #_state_variables: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, obj_id: str, obj_data: Dict[str, Any]) -> 'Object':
        # Load object from JSON file
        try:
            # Create Object instance
            obj = cls(
                # Start with BaseObj attributes first
                name=obj_id,
                description=obj_data.get("description", ""),
                flags=Object._parse_flags(obj_data.get("flags", [])),
                location=obj_data.get("location"),
                synonyms=obj_data.get("synonyms", []),
                adjectives=obj_data.get("adjectives", []),            
                action=obj_data.get("action", None),
                
                # These are frequently found, but not in all object types
                fdesc=obj_data.get("fdesc", ""),
                capacity=obj_data.get("capacity", 0),
                text=obj_data.get("text", ""),

                # These are a little more specialized and specific to only 1 or 2 types
                count=obj_data.get("count", 0),
                descfcn=obj_data.get("descfn", None),
                ldesc=obj_data.get("ldesc", ""),
                character=obj_data.get("character", 0),
                state=obj_data.get("state", 0),
                size=obj_data.get("size", 0)

                # ?  Not sure where Claude was going here - revisit later.
                #properties=obj_data.get("properties", {}),
                #contents=obj_data.get("contents", [])
            )

            classattrs: Dict = obj.__dict__.keys()
            json_obj_keys = obj_data.keys()
            
            a = set(json_obj_keys)
            b = set(classattrs)

            missing: Set = set(json_obj_keys) - set(classattrs)
            if len(missing) > 0:
                print(f"Attributes present in JSON objects, but missing in Object definition: {missing}, for objects {obj_id}")

            return obj
        
        except Exception as e:
            logger.error(f"Failed to load object {obj_id} with {obj_data}: {e}")
            raise ResourceLoadError(f"Cannot load object: {e}")



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
                action=room_data.get("action"),

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


