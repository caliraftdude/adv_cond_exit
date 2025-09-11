"""
Room dataclass and base class for the Deadline adventure game.
This module provides the core Room functionality for the game engine.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Union
from enum import Enum, auto


class ExitType(Enum):
    """Enumeration of exit types in the game"""
    NORMAL = auto()      # Standard exit to another room
    DOOR = auto()        # Exit through a door object
    NON_EXIT = auto()    # Blocked exit with message
    CONDITIONAL = auto() # Exit with condition check


@dataclass
class NavigationData:
    """
    Navigation metadata for room positioning and pathfinding.
    
    Used by NPCs and the game engine for movement calculations.
    """
    line: int = 0        # Navigation line/layer (vertical position in building)
    station: str = ""    # Reference point for navigation
    corridor: int = 0    # Corridor/path identifier for pathfinding
    
    def __post_init__(self):
        """Validate navigation data after initialization"""
        if self.line < 0:
            raise ValueError(f"Navigation line must be non-negative, got {self.line}")
        if self.corridor < 0:
            raise ValueError(f"Navigation corridor must be non-negative, got {self.corridor}")


@dataclass
class ExitData:
    """
    Represents a single exit from a room.
    
    Can be a simple destination string or a complex exit with conditions.
    """
    destination: Optional[str] = None      # Target room ID
    exit_type: ExitType = ExitType.NORMAL  # Type of exit
    door_object: Optional[str] = None      # Associated door object ID (for DOOR type)
    message: Optional[str] = None          # Message for NON_EXIT type
    condition_var: Optional[str] = None    # Condition variable for CONDITIONAL type
    failure_message: Optional[str] = None  # Message when condition fails
    
    @classmethod
    def from_dict(cls, data: Union[str, Dict[str, Any]]) -> 'ExitData':
        """
        Factory method to create ExitData from various input formats.
        
        Args:
            data: Either a string (simple destination) or dict (complex exit)
            
        Returns:
            ExitData instance
        """
        # Simple string destination
        if isinstance(data, str):
            return cls(destination=data, exit_type=ExitType.NORMAL)
        
        # Complex exit dictionary
        if isinstance(data, dict):
            exit_type_str = data.get('type', 'normal')
            
            # Map string types to enum
            type_map = {
                'normal': ExitType.NORMAL,
                'door': ExitType.DOOR,
                'non_exit': ExitType.NON_EXIT,
                'conditional': ExitType.CONDITIONAL
            }
            
            exit_type = type_map.get(exit_type_str, ExitType.NORMAL)
            
            return cls(
                destination=data.get('destination'),
                exit_type=exit_type,
                door_object=data.get('door_object'),
                message=data.get('message'),
                condition_var=data.get('condition_var'),
                failure_message=data.get('failure_message')
            )
        
        raise ValueError(f"Invalid exit data format: {type(data)}")


@dataclass
class Room:
    """
    Base Room class for all locations in the game.
    
    This class represents a single location in the game world with all its
    properties, exits, objects, and associated behaviors.
    """
    
    # Core identification
    id: str                                     # Unique room identifier (e.g., "SOUTH-LAWN")
    name: str                                   # Display name (e.g., "South Lawn")
    description: str                            # Full room description
    
    # Word parsing support
    synonyms: List[str] = field(default_factory=list)      # Alternative names for the room
    adjectives: List[str] = field(default_factory=list)    # Descriptive adjectives
    
    # Game flags (will be converted to bit flags in game engine)
    flags: List[str] = field(default_factory=list)         # Room flags (e.g., ["RLANDBIT", "ONBIT"])
    
    # Action handler
    action: Optional[str] = None                # Associated action routine name
    
    # Exits to other rooms
    exits: Dict[str, ExitData] = field(default_factory=dict)  # Direction -> Exit mapping
    
    # Objects and items
    global_objects: List[str] = field(default_factory=list)   # Objects visible in this room
    pseudo_objects: List[str] = field(default_factory=list)   # Mentioned but non-takeable objects
    
    # Navigation metadata
    navigation: Optional[NavigationData] = None
    
    # Optional room size (for capacity constraints)
    size: Optional[int] = None
    
    # Runtime state (not loaded from JSON)
    visited: bool = field(default=False, init=False)          # Has player visited this room?
    light_level: int = field(default=100, init=False)         # Current light level (0-100)
    _objects_present: List[str] = field(default_factory=list, init=False)  # Currently present objects
    
    def __post_init__(self):
        """
        Post-initialization processing and validation.
        
        Converts raw exit data to ExitData objects and validates room data.
        """
        # Convert exit data to ExitData objects
        processed_exits = {}
        for direction, exit_info in self.exits.items():
            if isinstance(exit_info, ExitData):
                processed_exits[direction] = exit_info
            else:
                processed_exits[direction] = ExitData.from_dict(exit_info)
        self.exits = processed_exits
        
        # Validate room ID
        if not self.id:
            raise ValueError("Room must have a valid ID")
        
        # Ensure name exists (use ID if not provided)
        if not self.name:
            self.name = self.id.replace('-', ' ').replace('_', ' ').title()
    
    @classmethod
    def from_json_data(cls, room_id: str, data: Dict[str, Any]) -> 'Room':
        """
        Factory method to create a Room from JSON data.
        
        Args:
            room_id: Unique identifier for the room
            data: Dictionary containing room data from JSON
            
        Returns:
            Room instance
        """
        # Extract navigation data if present
        navigation = None
        if 'navigation' in data:
            nav_data = data['navigation']
            navigation = NavigationData(
                line=nav_data.get('line', 0),
                station=nav_data.get('station', ''),
                corridor=nav_data.get('corridor', 0)
            )
        
        # Create room instance
        room = cls(
            id=room_id,
            name=data.get('name', ''),
            description=data.get('description', ''),
            synonyms=data.get('synonyms', []),
            adjectives=data.get('adjectives', []),
            flags=data.get('flags', []),
            action=data.get('action'),
            exits=data.get('exits', {}),
            global_objects=data.get('global_objects', []),
            pseudo_objects=data.get('pseudo_objects', []),
            navigation=navigation,
            size=data.get('size')
        )
        
        return room
    
    def get_exit(self, direction: str) -> Optional[ExitData]:
        """
        Get exit data for a given direction.
        
        Args:
            direction: Cardinal direction or special exit (e.g., "north", "in", "up")
            
        Returns:
            ExitData if exit exists, None otherwise
        """
        return self.exits.get(direction.lower())
    
    def get_available_exits(self) -> List[str]:
        """
        Get list of all available exit directions.
        
        Returns:
            List of direction strings
        """
        return list(self.exits.keys())
    
    def has_exit(self, direction: str) -> bool:
        """
        Check if room has an exit in the given direction.
        
        Args:
            direction: Direction to check
            
        Returns:
            True if exit exists
        """
        return direction.lower() in self.exits
    
    def is_dark(self) -> bool:
        """
        Check if room is currently dark.
        
        Returns:
            True if room is dark (needs light source)
        """
        # Check for ONBIT flag (indicates room has light)
        if "ONBIT" in self.flags:
            return False
        
        # Room is dark if light level is too low
        return self.light_level < 30
    
    def add_object(self, obj_id: str):
        """
        Add an object to this room.
        
        Args:
            obj_id: Object identifier to add
        """
        if obj_id not in self._objects_present:
            self._objects_present.append(obj_id)
    
    def remove_object(self, obj_id: str) -> bool:
        """
        Remove an object from this room.
        
        Args:
            obj_id: Object identifier to remove
            
        Returns:
            True if object was removed, False if not present
        """
        if obj_id in self._objects_present:
            self._objects_present.remove(obj_id)
            return True
        return False
    
    def get_objects(self) -> List[str]:
        """
        Get all objects currently in this room.
        
        Returns:
            List of object identifiers
        """
        # Combine runtime objects with global objects
        all_objects = self._objects_present.copy()
        all_objects.extend(self.global_objects)
        return all_objects
    
    def has_object(self, obj_id: str) -> bool:
        """
        Check if an object is present in this room.
        
        Args:
            obj_id: Object identifier to check
            
        Returns:
            True if object is present
        """
        return obj_id in self._objects_present or obj_id in self.global_objects
    
    def get_description(self, verbose: bool = False) -> str:
        """
        Get room description based on context.
        
        Args:
            verbose: If True, always return full description
            
        Returns:
            Appropriate room description string
        """
        # For first visit or verbose mode, return full description
        if not self.visited or verbose:
            return self.description
        
        # For subsequent visits, return just the name
        return self.name
    
    def enter(self):
        """
        Called when player enters this room.
        
        Updates room state and triggers any entry actions.
        """
        self.visited = True
        
        # TODO: Trigger room action if defined
        # This would call the action routine specified in self.action
    
    def matches_name(self, text: str) -> bool:
        """
        Check if text matches this room's name or synonyms.
        
        Args:
            text: Text to match against
            
        Returns:
            True if text matches room identification
        """
        text_lower = text.lower()
        
        # Check main name
        if text_lower in self.name.lower():
            return True
        
        # Check synonyms
        for synonym in self.synonyms:
            if text_lower in synonym.lower():
                return True
        
        # Check with adjectives
        for adj in self.adjectives:
            if f"{adj} {text_lower}" in self.name.lower():
                return True
            for synonym in self.synonyms:
                if f"{adj} {text_lower}" in synonym.lower():
                    return True
        
        return False
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert room to dictionary for serialization.
        
        Returns:
            Dictionary representation of room
        """
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'synonyms': self.synonyms,
            'adjectives': self.adjectives,
            'flags': self.flags,
            'global_objects': self.global_objects,
            'visited': self.visited,
            'light_level': self.light_level,
            '_objects_present': self._objects_present
        }
        
        if self.action:
            data['action'] = self.action
        
        if self.pseudo_objects:
            data['pseudo_objects'] = self.pseudo_objects
        
        if self.navigation:
            data['navigation'] = {
                'line': self.navigation.line,
                'station': self.navigation.station,
                'corridor': self.navigation.corridor
            }
        
        if self.size is not None:
            data['size'] = self.size
        
        # Convert exits
        exits_data = {}
        for direction, exit_data in self.exits.items():
            if exit_data.exit_type == ExitType.NORMAL:
                exits_data[direction] = exit_data.destination
            else:
                exit_dict = {'type': exit_data.exit_type.name.lower()}
                if exit_data.destination:
                    exit_dict['destination'] = exit_data.destination
                if exit_data.door_object:
                    exit_dict['door_object'] = exit_data.door_object
                if exit_data.message:
                    exit_dict['message'] = exit_data.message
                if exit_data.condition_var:
                    exit_dict['condition_var'] = exit_data.condition_var
                if exit_data.failure_message:
                    exit_dict['failure_message'] = exit_data.failure_message
                exits_data[direction] = exit_dict
        
        data['exits'] = exits_data
        
        return data
    
    def __repr__(self) -> str:
        """String representation for debugging"""
        return f"Room(id='{self.id}', name='{self.name}', exits={list(self.exits.keys())})"


# Helper functions for room factory pattern support

def create_room_from_json(room_id: str, json_data: Dict[str, Any]) -> Room:
    """
    Factory function to create a Room instance from JSON data.
    
    This is the primary way rooms should be instantiated from game data files.
    
    Args:
        room_id: Unique room identifier
        json_data: Room data from JSON file
        
    Returns:
        Configured Room instance
    """
    return Room.from_json_data(room_id, json_data)


def validate_room_data(data: Dict[str, Any]) -> List[str]:
    """
    Validate room data structure and return list of issues.
    
    Args:
        data: Room data to validate
        
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    # Check required fields
    if not data.get('name'):
        errors.append("Room missing required 'name' field")
    
    if not data.get('description'):
        errors.append("Room missing required 'description' field")
    
    # Validate exits structure
    if 'exits' in data:
        exits = data['exits']
        if not isinstance(exits, dict):
            errors.append(f"Exits must be a dictionary, got {type(exits)}")
        else:
            for direction, exit_data in exits.items():
                if isinstance(exit_data, dict):
                    exit_type = exit_data.get('type')
                    if exit_type == 'door' and not exit_data.get('door_object'):
                        errors.append(f"Door exit '{direction}' missing door_object")
                    if exit_type == 'non_exit' and not exit_data.get('message'):
                        errors.append(f"Non-exit '{direction}' missing message")
                    if exit_type == 'conditional':
                        if not exit_data.get('condition_var'):
                            errors.append(f"Conditional exit '{direction}' missing condition_var")
                        if not exit_data.get('failure_message'):
                            errors.append(f"Conditional exit '{direction}' missing failure_message")
    
    # Validate navigation structure
    if 'navigation' in data:
        nav = data['navigation']
        if not isinstance(nav, dict):
            errors.append(f"Navigation must be a dictionary, got {type(nav)}")
        else:
            for field in ['line', 'station', 'corridor']:
                if field not in nav:
                    errors.append(f"Navigation missing '{field}' field")
    
    return errors