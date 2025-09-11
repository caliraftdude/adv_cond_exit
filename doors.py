"""
Door dataclass and base class for the Deadline adventure game.
This module provides the core Door functionality for the game engine.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Set
from enum import Flag, auto


class DoorFlag(Flag):
    """
    Bit flags for door properties.
    
    These flags control door behavior and state in the game.
    Uses Python's Flag enum for efficient bitwise operations.
    """
    NONE = 0
    DOORBIT = auto()      # Object is a door
    CONTBIT = auto()      # Can contain objects (e.g., mail slot)
    OPENBIT = auto()      # Door is currently open
    INVISIBLE = auto()    # Door is hidden/secret
    LOCKEDBIT = auto()    # Door is locked
    TRANSBIT = auto()     # Can see through (glass door, window)
    
    @classmethod
    def from_string_list(cls, flag_strings: List[str]) -> 'DoorFlag':
        """
        Convert a list of flag strings to a DoorFlag combination.
        
        Args:
            flag_strings: List of flag names as strings
            
        Returns:
            Combined DoorFlag value
        """
        result = cls.NONE
        for flag_str in flag_strings:
            # Convert string to uppercase and try to get the flag
            flag_name = flag_str.upper()
            if hasattr(cls, flag_name):
                result |= getattr(cls, flag_name)
            else:
                # Log unknown flags for debugging but don't fail
                print(f"Warning: Unknown door flag '{flag_str}'")
        return result
    
    def to_string_list(self) -> List[str]:
        """
        Convert flag combination back to list of strings.
        
        Returns:
            List of flag names that are set
        """
        result = []
        for flag in DoorFlag:
            if flag != DoorFlag.NONE and flag in self:
                result.append(flag.name)
        return result


@dataclass
class Door:
    """
    Base Door class for all door-like objects in the game.
    
    Doors are special objects that connect rooms and can be opened/closed,
    locked/unlocked, and may be hidden or transparent. They can also act
    as containers (like mail slots).
    """
    
    # Core identification
    id: str                                          # Unique door identifier (e.g., "FRONT-DOOR")
    description: str                                 # Display description (e.g., "front door")
    
    # Word parsing support
    synonyms: List[str] = field(default_factory=list)      # Alternative names (usually includes "door")
    adjectives: List[str] = field(default_factory=list)    # Descriptive adjectives (e.g., ["front"])
    
    # Door state and properties
    flags: DoorFlag = DoorFlag.DOORBIT                     # Bit flags for door properties
    
    # Location and connections
    location: str = "LOCAL-GLOBALS"                        # Where door exists (usually LOCAL-GLOBALS)
    connects: Dict[str, str] = field(default_factory=dict) # Room connections {"room1": "room2"}
    
    # Action handler
    action: Optional[str] = None                           # Associated action routine name
    
    # Runtime state (not loaded from JSON)
    _is_open: bool = field(default=False, init=False)      # Current open/closed state
    _is_locked: bool = field(default=False, init=False)    # Current locked state
    _contained_objects: List[str] = field(default_factory=list, init=False)  # Objects in door (mail)
    
    def __post_init__(self):
        """
        Post-initialization processing and state setup.
        
        Sets initial door state based on flags.
        """
        # Set initial state from flags
        self._is_open = DoorFlag.OPENBIT in self.flags
        self._is_locked = DoorFlag.LOCKEDBIT in self.flags
        
        # Ensure DOORBIT is always set
        if DoorFlag.DOORBIT not in self.flags:
            self.flags |= DoorFlag.DOORBIT
        
        # Validate required fields
        if not self.id:
            raise ValueError("Door must have a valid ID")
        
        if not self.description:
            self.description = self.id.replace('-', ' ').replace('_', ' ').lower()
    
    @classmethod
    def from_json_data(cls, door_id: str, data: Dict[str, Any]) -> 'Door':
        """
        Factory method to create a Door from JSON data.
        
        Args:
            door_id: Unique identifier for the door
            data: Dictionary containing door data from JSON
            
        Returns:
            Door instance
        """
        # Parse flags
        flag_list = data.get('flags', ['DOORBIT'])
        flags = DoorFlag.from_string_list(flag_list)
        
        # Create door instance
        door = cls(
            id=door_id,
            description=data.get('description', ''),
            synonyms=data.get('synonyms', []),
            adjectives=data.get('adjectives', []),
            flags=flags,
            location=data.get('location', 'LOCAL-GLOBALS'),
            connects=data.get('connects', {}),
            action=data.get('action')
        )
        
        return door
    
    # Door state management methods
    
    def is_open(self) -> bool:
        """Check if door is currently open."""
        return self._is_open
    
    def is_closed(self) -> bool:
        """Check if door is currently closed."""
        return not self._is_open
    
    def is_locked(self) -> bool:
        """Check if door is currently locked."""
        return self._is_locked
    
    def is_hidden(self) -> bool:
        """Check if door is hidden/invisible."""
        return DoorFlag.INVISIBLE in self.flags
    
    def is_transparent(self) -> bool:
        """Check if you can see through the door."""
        return DoorFlag.TRANSBIT in self.flags
    
    def can_contain_objects(self) -> bool:
        """Check if door can contain objects (like a mail slot)."""
        return DoorFlag.CONTBIT in self.flags
    
    # Door manipulation methods
    
    def open(self) -> tuple[bool, str]:
        """
        Attempt to open the door.
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        if self._is_open:
            return False, f"The {self.get_name()} is already open."
        
        if self._is_locked:
            return False, f"The {self.get_name()} is locked."
        
        self._is_open = True
        self.flags |= DoorFlag.OPENBIT
        return True, f"You open the {self.get_name()}."
    
    def close(self) -> tuple[bool, str]:
        """
        Attempt to close the door.
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        if not self._is_open:
            return False, f"The {self.get_name()} is already closed."
        
        self._is_open = False
        self.flags &= ~DoorFlag.OPENBIT
        return True, f"You close the {self.get_name()}."
    
    def lock(self, with_key: Optional[str] = None) -> tuple[bool, str]:
        """
        Attempt to lock the door.
        
        Args:
            with_key: Optional key object ID required to lock
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if self._is_locked:
            return False, f"The {self.get_name()} is already locked."
        
        if self._is_open:
            return False, f"You can't lock the {self.get_name()} while it's open."
        
        # TODO: Check if correct key is provided when key system is implemented
        
        self._is_locked = True
        self.flags |= DoorFlag.LOCKEDBIT
        return True, f"You lock the {self.get_name()}."
    
    def unlock(self, with_key: Optional[str] = None) -> tuple[bool, str]:
        """
        Attempt to unlock the door.
        
        Args:
            with_key: Optional key object ID required to unlock
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if not self._is_locked:
            return False, f"The {self.get_name()} is not locked."
        
        # TODO: Check if correct key is provided when key system is implemented
        
        self._is_locked = False
        self.flags &= ~DoorFlag.LOCKEDBIT
        return True, f"You unlock the {self.get_name()}."
    
    # Container functionality (for doors with CONTBIT)
    
    def add_object(self, obj_id: str) -> bool:
        """
        Add an object to the door (e.g., mail in mail slot).
        
        Args:
            obj_id: Object identifier to add
            
        Returns:
            True if object was added, False if door can't contain objects
        """
        if not self.can_contain_objects():
            return False
        
        if obj_id not in self._contained_objects:
            self._contained_objects.append(obj_id)
        return True
    
    def remove_object(self, obj_id: str) -> bool:
        """
        Remove an object from the door.
        
        Args:
            obj_id: Object identifier to remove
            
        Returns:
            True if object was removed, False if not present
        """
        if obj_id in self._contained_objects:
            self._contained_objects.remove(obj_id)
            return True
        return False
    
    def get_contained_objects(self) -> List[str]:
        """Get list of objects contained in this door."""
        return self._contained_objects.copy()
    
    # Utility methods
    
    def get_name(self) -> str:
        """
        Get the display name for this door.
        
        Combines adjectives with description for full name.
        
        Returns:
            Full display name
        """
        if self.adjectives:
            adj_str = ' '.join(self.adjectives)
            return f"{adj_str} {self.description}"
        return self.description
    
    def matches_name(self, text: str) -> bool:
        """
        Check if text matches this door's name or synonyms.
        
        Args:
            text: Text to match against
            
        Returns:
            True if text matches door identification
        """
        text_lower = text.lower()
        
        # Check description
        if text_lower in self.description.lower():
            return True
        
        # Check synonyms
        for synonym in self.synonyms:
            if text_lower in synonym.lower():
                return True
        
        # Check with adjectives
        for adj in self.adjectives:
            full_name = f"{adj} {text_lower}"
            if full_name in self.description.lower():
                return True
            for synonym in self.synonyms:
                if full_name in f"{adj} {synonym}".lower():
                    return True
        
        return False
    
    def get_room_connection(self, from_room: str) -> Optional[str]:
        """
        Get the destination room when going through this door.
        
        Args:
            from_room: The room the player is currently in
            
        Returns:
            The destination room ID, or None if not connected
        """
        return self.connects.get(from_room)
    
    def connects_rooms(self, room1: str, room2: str) -> bool:
        """
        Check if this door connects two specific rooms.
        
        Args:
            room1: First room ID
            room2: Second room ID
            
        Returns:
            True if door connects these rooms
        """
        return (self.connects.get(room1) == room2 or 
                self.connects.get(room2) == room1)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert door to dictionary for serialization.
        
        Returns:
            Dictionary representation of door
        """
        data = {
            'id': self.id,
            'description': self.description,
            'synonyms': self.synonyms,
            'adjectives': self.adjectives,
            'flags': self.flags.to_string_list(),
            'location': self.location,
            '_is_open': self._is_open,
            '_is_locked': self._is_locked
        }
        
        if self.action:
            data['action'] = self.action
        
        if self.connects:
            data['connects'] = self.connects
        
        if self._contained_objects:
            data['_contained_objects'] = self._contained_objects
        
        return data
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        state = []
        if self._is_open:
            state.append("open")
        else:
            state.append("closed")
        if self._is_locked:
            state.append("locked")
        if self.is_hidden():
            state.append("hidden")
        
        state_str = ', '.join(state)
        return f"Door(id='{self.id}', name='{self.get_name()}', state=[{state_str}])"


# Helper functions for door factory pattern support

def create_door_from_json(door_id: str, json_data: Dict[str, Any]) -> Door:
    """
    Factory function to create a Door instance from JSON data.
    
    This is the primary way doors should be instantiated from game data files.
    
    Args:
        door_id: Unique door identifier
        json_data: Door data from JSON file
        
    Returns:
        Configured Door instance
    """
    return Door.from_json_data(door_id, json_data)


def validate_door_data(data: Dict[str, Any]) -> List[str]:
    """
    Validate door data structure and return list of issues.
    
    Args:
        data: Door data to validate
        
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    # Check recommended fields
    if not data.get('description'):
        errors.append("Door missing 'description' field")
    
    # Validate flags structure
    if 'flags' in data:
        flags = data['flags']
        if not isinstance(flags, list):
            errors.append(f"Flags must be a list, got {type(flags)}")
        else:
            # Check for DOORBIT
            if 'DOORBIT' not in flags:
                errors.append("Door should have 'DOORBIT' flag")
    
    # Validate connects structure if present
    if 'connects' in data:
        connects = data['connects']
        if not isinstance(connects, dict):
            errors.append(f"Connects must be a dictionary, got {type(connects)}")
    
    # Check action is a string if present
    if 'action' in data and not isinstance(data['action'], str):
        errors.append(f"Action must be a string, got {type(data['action'])}")
    
    return errors


def get_door_state_description(door: Door) -> str:
    """
    Get a human-readable description of the door's current state.
    
    Args:
        door: Door object to describe
        
    Returns:
        Description string
    """
    parts = [f"The {door.get_name()} is"]
    
    if door.is_hidden():
        return f"You don't see any {door.get_name()} here."
    
    if door.is_open():
        parts.append("open")
    else:
        parts.append("closed")
    
    if door.is_locked():
        parts.append("and locked")
    
    if door.is_transparent():
        parts.append("(you can see through it)")
    
    return ' '.join(parts) + '.'


# Action dispatcher placeholder
# This will be implemented later to handle the 'action' field

class DoorActionDispatcher:
    """
    Placeholder for the door action dispatcher.
    
    This class will be implemented later to handle action routines
    specified in the 'action' field of door definitions.
    """
    
    def __init__(self):
        """
        Initialize the dispatcher with an empty action registry.
        
        The registry will map action names (strings) to callable functions.
        """
        self.action_registry: Dict[str, callable] = {}
    
    def register_action(self, action_name: str, action_function: callable):
        """
        Register an action function.
        
        Args:
            action_name: Name of the action (matches 'action' field in JSON)
            action_function: Callable to execute for this action
        """
        self.action_registry[action_name] = action_function
    
    def dispatch(self, door: Door, *args, **kwargs):
        """
        Dispatch an action for a door.
        
        Args:
            door: Door object to act upon
            *args, **kwargs: Additional arguments for the action
            
        Returns:
            Result from the action function, or None if no action
        """
        if door.action and door.action in self.action_registry:
            return self.action_registry[door.action](door, *args, **kwargs)
        return None


# Note: The actual action functions (DOOR-F, BAY-WINDOW-F, etc.) 
# will be implemented in actions.py and registered with the dispatcher
# during game initialization.