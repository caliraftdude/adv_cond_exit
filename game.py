"""
Game API Class - Provides all game.* functions for action scripts
This class serves as the central API for all game actions from the translated ZIL code.
"""

import logging
import random
from typing import Any, Dict, List, Optional, Union, Callable, Set, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
import json

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GameException(Exception):
    """Base exception for game errors"""
    pass


class ObjectNotFoundError(GameException):
    """Raised when an object cannot be found"""
    pass


class InvalidActionError(GameException):
    """Raised when an invalid action is attempted"""
    pass


class PropertyError(GameException):
    """Raised when there's an issue with object properties"""
    pass


@dataclass
class GameObject:
    """Represents any object in the game"""
    id: str
    name: str
    description: str = ""
    location: Optional[str] = None
    flags: Set[str] = field(default_factory=set)
    properties: Dict[str, Any] = field(default_factory=dict)
    contents: List[str] = field(default_factory=list)
    action_handler: Optional[Callable] = None


@dataclass
class Room:
    """Represents a room/location in the game"""
    id: str
    name: str
    description: str
    exits: Dict[str, str] = field(default_factory=dict)
    contents: List[str] = field(default_factory=list)
    flags: Set[str] = field(default_factory=set)
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ScheduledEvent:
    """Represents a scheduled event"""
    name: str
    turns_remaining: int
    callback: Callable
    enabled: bool = True
    recurring: bool = False
    interval: int = 0


class Game:
    """
    Main Game API class providing all game.* functions for action scripts.
    This class maintains all game state and provides the interface for
    game actions to interact with the game world.
    """
    
    def __init__(self, data_path: Optional[Path] = None):
        """
        Initialize the game state.
        
        Args:
            data_path: Path to game data files (JSON)
        """
        # Core game state
        self.globals: Dict[str, Any] = {}
        self.objects: Dict[str, GameObject] = {}
        self.rooms: Dict[str, Room] = {}
        self.vocabulary: Dict[str, List[str]] = {}
        
        # Parser state
        self.PRSO: Optional[str] = None  # Direct object
        self.PRSI: Optional[str] = None  # Indirect object
        self.PRSA: Optional[str] = None  # Current action/verb
        self.P_NUMBER: Optional[int] = None  # Parsed number
        
        # Player state
        self.HERE: str = "ENTRANCE-HALL"  # Current location
        self.WINNER: str = "PLAYER"  # Current actor (usually player)
        self.PRESENT_TIME: int = 480  # Game time (minutes since midnight, 480 = 8:00 AM)
        
        # Output buffer
        self.output_buffer: List[str] = []
        
        # Scheduled events
        self.events: List[ScheduledEvent] = []
        
        # Special flags
        self.return_value: Optional[bool] = None
        
        # Load game data if provided
        if data_path:
            self._load_game_data(data_path)
        
        # Initialize common globals used in Deadline
        # XXX The globals should be loaded in the game files and initialized there.. this is unneeded. 
        # self._init_deadline_globals()
        
        logger.info("Game API initialized successfully")
    
    def _init_deadline_globals(self) -> None:
        """Initialize Deadline-specific global variables"""
        self.globals.update({
            "LADDER-FLAG": False,
            "LADDER-FLAG-2": False,
            "LADDER-POSITIONED": False,
            "FRAGMENT-FOUND": False,
            "FRAGMENT-FELT": False,
            "FRAGMENT-CLEANED": False,
            "FRAGMENT-FLAG": False,
            "CHINA-EXAMINED": False,
            "CALENDAR-PAGE": 7,
            "NOTE-READ": False,
            "FINGERPRINT-OBJ": None,
            "ANALYSIS-OBJ": None,
            "ANALYSIS-GOAL": None,
            "SECRET-MEETING": 0,
            "CALL-IN-PROGRESS": False,
            "HOLE-TELL": False,
            "HOLE-SHOWN": False,
            "RST": 0,
            "ROSE-DIGS": [
                "You dig around a bit but find nothing unusual.",
                "Still digging... you feel something sharp but can't locate it.",
                "You're getting closer to finding something..."
            ],
            "GARDENER-ANGRY": False,
            "GARDENER-NO-REPLY": False,
            "GARDENER-SHOW": False,
            "G-I-G": False,
            "WELCOMED": False,
            "WILL-TIME": 0,
            "DRUNK-FLAG": False,
            "STEREO-ON": False,
            "TUNE-ON": None,
            "GEORGE-RUN": 0,
        })
    
    def _load_game_data(self, data_path: Path) -> None:
        """
        Load game data from JSON files.
        
        Args:
            data_path: Path to directory containing game data files
        """
        try:
            # Load main game data
            game_file = data_path / "game_data.json"
            if game_file.exists():
                with open(game_file, 'r') as f:
                    data = json.load(f)
                    # Process rooms, objects, etc.
                    logger.info(f"Loaded game data from {game_file}")
            
            # Load vocabulary
            vocab_file = data_path / "vocabulary.json"
            if vocab_file.exists():
                with open(vocab_file, 'r') as f:
                    self.vocabulary = json.load(f)
                    logger.info(f"Loaded vocabulary from {vocab_file}")
                    
        except Exception as e:
            logger.error(f"Error loading game data: {e}")
            raise GameException(f"Failed to load game data: {e}")
    
    # ========== OUTPUT FUNCTIONS ==========
    

    
    def CRLF(self) -> None:
        """
        Output a newline.
        Equivalent to ZIL's CRLF.
        """
        try:
            if self.output_buffer:
                print(''.join(self.output_buffer))
                self.output_buffer.clear()
            else:
                print()
            logger.debug("CRLF")
        except Exception as e:
            logger.error(f"Error in CRLF: {e}")
            raise GameException(f"Newline error: {e}")
    
    def DDESC(self, str1: str, door: str, str2: str = "") -> None:
        """
        Describe with door state - prints text with door open/closed status.
        
        Args:
            str1: Text before door state
            door: Door object ID
            str2: Text after door state
        """
        try:
            self.TELL(str1, end="")
            if self.IS_FSET(door, "OPENBIT"):
                self.TELL("open", end="")
            else:
                self.TELL("closed", end="")
            self.TELL(str2)
        except Exception as e:
            logger.error(f"Error in DDESC: {e}")
            raise GameException(f"Door description error: {e}")
    

    
    def VAR(self, name: str) -> Any:
        """
        Alias for GETG for compatibility.
        
        Args:
            name: Variable name
            
        Returns:
            The global variable value
        """
        return self.GETG(name)
    
    # ========== VERB/ACTION FUNCTIONS ==========
    
    def VERB(self, *verbs: str) -> bool:
        """
        Check if the current action is one of the specified verbs.
        Equivalent to ZIL's VERB?.
        
        Args:
            *verbs: One or more verb names to check
            
        Returns:
            True if current action matches any of the verbs
        """
        try:
            result = self.PRSA in verbs
            logger.debug(f"VERB check: {verbs} -> {result} (current: {self.PRSA})")
            return result
        except Exception as e:
            logger.error(f"Error in VERB check: {e}")
            return False
    
    def IS_VERB(self, *verbs: str) -> bool:
        """
        Alias for VERB for compatibility.
        
        Args:
            *verbs: One or more verb names to check
            
        Returns:
            True if current action matches any of the verbs
        """
        return self.VERB(*verbs)
    
    # ========== FLAG FUNCTIONS ==========
    
    def FSET(self, obj_id: str, flag: str) -> None:
        """
        Set a flag on an object.
        Equivalent to ZIL's FSET.
        
        Args:
            obj_id: Object ID
            flag: Flag name to set
        """
        try:
            obj = self._get_object_or_room(obj_id)
            if obj:
                obj.flags.add(flag)
                logger.debug(f"FSET: {obj_id}.{flag} = True")
            else:
                raise ObjectNotFoundError(f"Object {obj_id} not found")
        except Exception as e:
            logger.error(f"Error setting flag {flag} on {obj_id}: {e}")
            raise GameException(f"Cannot set flag: {e}")
    
    def FCLEAR(self, obj_id: str, flag: str) -> None:
        """
        Clear a flag from an object.
        Equivalent to ZIL's FCLEAR.
        
        Args:
            obj_id: Object ID
            flag: Flag name to clear
        """
        try:
            obj = self._get_object_or_room(obj_id)
            if obj:
                obj.flags.discard(flag)
                logger.debug(f"FCLEAR: {obj_id}.{flag} = False")
            else:
                raise ObjectNotFoundError(f"Object {obj_id} not found")
        except Exception as e:
            logger.error(f"Error clearing flag {flag} on {obj_id}: {e}")
            raise GameException(f"Cannot clear flag: {e}")
    
    def IS_FSET(self, obj_id: str, flag: str) -> bool:
        """
        Check if an object has a flag set.
        Equivalent to ZIL's FSET?.
        
        Args:
            obj_id: Object ID
            flag: Flag name to check
            
        Returns:
            True if flag is set
        """
        try:
            obj = self._get_object_or_room(obj_id)
            if obj:
                result = flag in obj.flags
                logger.debug(f"IS_FSET: {obj_id}.{flag} = {result}")
                return result
            return False
        except Exception as e:
            logger.error(f"Error checking flag {flag} on {obj_id}: {e}")
            return False
    
    def IS_SET(self, obj_id: str, flag: str) -> bool:
        """
        Alias for IS_FSET for compatibility.
        
        Args:
            obj_id: Object ID
            flag: Flag name to check
            
        Returns:
            True if flag is set
        """
        return self.IS_FSET(obj_id, flag)
    
    # ========== OBJECT MANIPULATION FUNCTIONS ==========
    
    def MOVE(self, obj_id: str, dest_id: str) -> None:
        """
        Move an object to a new location.
        Equivalent to ZIL's MOVE.
        
        Args:
            obj_id: Object to move
            dest_id: Destination (room or container)
        """
        try:
            obj = self._get_object(obj_id)
            if not obj:
                raise ObjectNotFoundError(f"Object {obj_id} not found")
            
            # Remove from current location
            if obj.location:
                old_loc = self._get_object_or_room(obj.location)
                if old_loc and obj_id in old_loc.contents:
                    old_loc.contents.remove(obj_id)
            
            # Add to new location
            new_loc = self._get_object_or_room(dest_id)
            if new_loc:
                if obj_id not in new_loc.contents:
                    new_loc.contents.append(obj_id)
                obj.location = dest_id
            
            logger.debug(f"MOVE: {obj_id} -> {dest_id}")
        except Exception as e:
            logger.error(f"Error moving {obj_id} to {dest_id}: {e}")
            raise GameException(f"Cannot move object: {e}")
    
    def REMOVE(self, obj_id: str) -> None:
        """
        Remove an object from play (move to nowhere).
        Equivalent to ZIL's REMOVE.
        
        Args:
            obj_id: Object to remove
        """
        try:
            obj = self._get_object(obj_id)
            if not obj:
                raise ObjectNotFoundError(f"Object {obj_id} not found")
            
            # Remove from current location
            if obj.location:
                old_loc = self._get_object_or_room(obj.location)
                if old_loc and obj_id in old_loc.contents:
                    old_loc.contents.remove(obj_id)
            
            obj.location = None
            logger.debug(f"REMOVE: {obj_id}")
        except Exception as e:
            logger.error(f"Error removing {obj_id}: {e}")
            raise GameException(f"Cannot remove object: {e}")
    
    def IN(self, obj_id: str, location_id: str) -> bool:
        """
        Check if an object is in a specific location.
        Equivalent to ZIL's IN?.
        
        Args:
            obj_id: Object to check
            location_id: Location to check
            
        Returns:
            True if object is in location
        """
        try:
            obj = self._get_object(obj_id)
            if not obj:
                return False
            
            # Check direct location
            if obj.location == location_id:
                return True
            
            # Check if in contents
            loc = self._get_object_or_room(location_id)
            if loc and obj_id in loc.contents:
                return True
            
            return False
        except Exception as e:
            logger.error(f"Error checking IN({obj_id}, {location_id}): {e}")
            return False
    
    def LOC(self, obj_id: str) -> Optional[str]:
        """
        Get the location of an object.
        Equivalent to ZIL's LOC.
        
        Args:
            obj_id: Object ID
            
        Returns:
            Location ID or None
        """
        try:
            obj = self._get_object(obj_id)
            if obj:
                return obj.location
            return None
        except Exception as e:
            logger.error(f"Error getting location of {obj_id}: {e}")
            return None
    
    def FIRST(self, container_id: str) -> Optional[str]:
        """
        Get the first object in a container.
        Equivalent to ZIL's FIRST?.
        
        Args:
            container_id: Container ID
            
        Returns:
            First object ID or None
        """
        try:
            container = self._get_object_or_room(container_id)
            if container and container.contents:
                return container.contents[0]
            return None
        except Exception as e:
            logger.error(f"Error getting first object in {container_id}: {e}")
            return None
    
    def NEXT(self, obj_id: str) -> Optional[str]:
        """
        Get the next sibling object in the same container.
        Equivalent to ZIL's NEXT?.
        
        Args:
            obj_id: Current object ID
            
        Returns:
            Next object ID or None
        """
        try:
            obj = self._get_object(obj_id)
            if not obj or not obj.location:
                return None
            
            container = self._get_object_or_room(obj.location)
            if not container or obj_id not in container.contents:
                return None
            
            idx = container.contents.index(obj_id)
            if idx < len(container.contents) - 1:
                return container.contents[idx + 1]
            
            return None
        except Exception as e:
            logger.error(f"Error getting next object after {obj_id}: {e}")
            return None
    
    # ========== PROPERTY FUNCTIONS ==========
    
    def GETP(self, obj_id: str, prop_name: str, default: Any = None) -> Any:
        """
        Get a property value from an object.
        Equivalent to ZIL's GETP.
        
        Args:
            obj_id: Object ID
            prop_name: Property name
            default: Default value if not found
            
        Returns:
            Property value or default
        """
        try:
            obj = self._get_object_or_room(obj_id)
            if obj:
                value = obj.properties.get(prop_name, default)
                logger.debug(f"GETP: {obj_id}.{prop_name} = {value}")
                return value
            return default
        except Exception as e:
            logger.error(f"Error getting property {prop_name} from {obj_id}: {e}")
            return default
    
    def PUTP(self, obj_id: str, prop_name: str, value: Any) -> None:
        """
        Set a property value on an object.
        Equivalent to ZIL's PUTP.
        
        Args:
            obj_id: Object ID
            prop_name: Property name
            value: Property value
        """
        try:
            obj = self._get_object_or_room(obj_id)
            if obj:
                obj.properties[prop_name] = value
                logger.debug(f"PUTP: {obj_id}.{prop_name} = {value}")
            else:
                raise ObjectNotFoundError(f"Object {obj_id} not found")
        except Exception as e:
            logger.error(f"Error setting property {prop_name} on {obj_id}: {e}")
            raise GameException(f"Cannot set property: {e}")
    
    # ========== GAME CONTROL FUNCTIONS ==========
    
    def GOTO(self, room_id: str) -> None:
        """
        Move the player to a new room.
        Equivalent to ZIL's GOTO.
        
        Args:
            room_id: Room ID to move to
        """
        try:
            if room_id in self.rooms:
                self.HERE = room_id
                logger.debug(f"GOTO: Player moved to {room_id}")
            else:
                raise ObjectNotFoundError(f"Room {room_id} not found")
        except Exception as e:
            logger.error(f"Error moving player to {room_id}: {e}")
            raise GameException(f"Cannot move to room: {e}")
    
    def PERFORM(self, verb: str, *objects: str) -> Any:
        """
        Perform a game action.
        Equivalent to ZIL's PERFORM.
        
        Args:
            verb: Verb/action to perform
            *objects: Objects involved
            
        Returns:
            Result of action
        """
        try:
            old_prsa = self.PRSA
            old_prso = self.PRSO
            old_prsi = self.PRSI
            
            self.PRSA = verb
            if len(objects) > 0:
                self.PRSO = objects[0]
            if len(objects) > 1:
                self.PRSI = objects[1]
            
            logger.debug(f"PERFORM: {verb} {objects}")
            
            # Here you would call the appropriate action handler
            # For now, we'll just restore the parser state
            result = True
            
            self.PRSA = old_prsa
            self.PRSO = old_prso
            self.PRSI = old_prsi
            
            return result
        except Exception as e:
            logger.error(f"Error performing {verb}: {e}")
            raise GameException(f"Cannot perform action: {e}")
    
    def RFALSE(self) -> bool:
        """
        Return false from current routine.
        Equivalent to ZIL's RFALSE.
        
        Returns:
            False
        """
        self.return_value = False
        logger.debug("RFALSE")
        return False
    
    def RTRUE(self) -> bool:
        """
        Return true from current routine.
        Equivalent to ZIL's RTRUE.
        
        Returns:
            True
        """
        self.return_value = True
        logger.debug("RTRUE")
        return True
    
    # ========== SCHEDULING FUNCTIONS ==========
    
    def QUEUE(self, event_name: str, turns: int) -> None:
        """
        Schedule an event to occur after a number of turns.
        Equivalent to ZIL's QUEUE.
        
        Args:
            event_name: Event name
            turns: Number of turns to wait (0 to cancel)
        """
        try:
            if turns == 0:
                # Cancel the event
                self.events = [e for e in self.events if e.name != event_name]
                logger.debug(f"QUEUE: Cancelled {event_name}")
            else:
                # Add or update event
                existing = next((e for e in self.events if e.name == event_name), None)
                if existing:
                    existing.turns_remaining = turns
                else:
                    # Create new event (callback would be looked up from event handlers)
                    event = ScheduledEvent(
                        name=event_name,
                        turns_remaining=turns,
                        callback=lambda: None  # Placeholder
                    )
                    self.events.append(event)
                logger.debug(f"QUEUE: Scheduled {event_name} in {turns} turns")
        except Exception as e:
            logger.error(f"Error queueing event {event_name}: {e}")
            raise GameException(f"Cannot queue event: {e}")
    
    def ENABLE(self, event: Any) -> None:
        """
        Enable an event or interrupt.
        Equivalent to ZIL's ENABLE.
        
        Args:
            event: Event to enable
        """
        try:
            # Handle the return value from QUEUE
            logger.debug(f"ENABLE: {event}")
            # In ZIL, this enables interrupts - we'll treat it as a no-op for now
        except Exception as e:
            logger.error(f"Error enabling event: {e}")
    
    # ========== UTILITY FUNCTIONS ==========
    
    def RANDOM(self, max_value: int) -> int:
        """
        Generate a random number from 1 to max_value.
        Equivalent to ZIL's RANDOM.
        
        Args:
            max_value: Maximum value (inclusive)
            
        Returns:
            Random number between 1 and max_value
        """
        try:
            result = random.randint(1, max_value)
            logger.debug(f"RANDOM({max_value}) = {result}")
            return result
        except Exception as e:
            logger.error(f"Error generating random number: {e}")
            return 1
    
    def PROB(self, percentage: int) -> bool:
        """
        Return true with given percentage probability.
        Equivalent to ZIL's PROB.
        
        Args:
            percentage: Probability percentage (0-100)
            
        Returns:
            True with given probability
        """
        try:
            result = random.randint(1, 100) <= percentage
            logger.debug(f"PROB({percentage}) = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in probability check: {e}")
            return False
    
    def EQUAL(self, value: Any, *options: Any) -> bool:
        """
        Check if value equals any of the options.
        Equivalent to ZIL's EQUAL?.
        
        Args:
            value: Value to check
            *options: Options to compare against
            
        Returns:
            True if value equals any option
        """
        try:
            result = value in options
            logger.debug(f"EQUAL({value}, {options}) = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in EQUAL check: {e}")
            return False
    
    def D(self, obj_id: str) -> str:
        """
        Get the description/name of an object.
        Equivalent to ZIL's D (PRINTD).
        
        Args:
            obj_id: Object ID
            
        Returns:
            Object description/name
        """
        try:
            obj = self._get_object_or_room(obj_id)
            if obj:
                return obj.name
            return obj_id
        except Exception as e:
            logger.error(f"Error getting description of {obj_id}: {e}")
            return obj_id
    
    def THIS_IS_IT(self, obj_id: str) -> None:
        """
        Set the current object as "it" for pronoun reference.
        Equivalent to ZIL's THIS-IS-IT.
        
        Args:
            obj_id: Object ID to set as "it"
        """
        try:
            self.SETG("IT", obj_id)
            logger.debug(f"THIS_IS_IT: {obj_id}")
        except Exception as e:
            logger.error(f"Error setting IT to {obj_id}: {e}")
    
    def IN_MOTION(self, obj_id: str) -> bool:
        """
        Check if an object/character is in motion.
        
        Args:
            obj_id: Object ID to check
            
        Returns:
            True if object is in motion
        """
        try:
            # Check if object has motion flag or is scheduled to move
            obj = self._get_object(obj_id)
            if obj:
                return "IN-MOTION" in obj.flags
            return False
        except Exception as e:
            logger.error(f"Error checking motion of {obj_id}: {e}")
            return False
    
    # ========== SPECIAL GAME-SPECIFIC FUNCTIONS ==========
    
    def CSCP(self) -> None:
        """
        China/plates special handling.
        Specific to Deadline game.
        """
        try:
            self.TELL("China and other valuable objects are not to be handled.")
            logger.debug("CSCP: China handling")
        except Exception as e:
            logger.error(f"Error in CSCP: {e}")
    
    def PAD_READ(self, text: str) -> None:
        """
        Read pad with special formatting.
        Specific to Deadline game.
        
        Args:
            text: Text to display
        """
        try:
            self.TELL(f"\n{text}:\n")
            self.TELL("reveals slight impressions of the note above!")
            self.SETG("NOTE-READ", True)
            logger.debug(f"PAD_READ: {text}")
        except Exception as e:
            logger.error(f"Error in PAD_READ: {e}")
    
    def DO_ANALYZE(self) -> None:
        """
        Perform analysis action.
        Specific to Deadline game.
        """
        try:
            # This would call the fingerprint analysis routine
            self.DO_FINGERPRINT(True)
            logger.debug("DO_ANALYZE called")
        except Exception as e:
            logger.error(f"Error in DO_ANALYZE: {e}")
    
    def DO_FINGERPRINT(self, analysis: bool = False) -> None:
        """
        Perform fingerprint analysis.
        Specific to Deadline game.
        
        Args:
            analysis: Whether this is part of analysis
        """
        try:
            # Placeholder for fingerprint analysis logic
            logger.debug(f"DO_FINGERPRINT: analysis={analysis}")
        except Exception as e:
            logger.error(f"Error in DO_FINGERPRINT: {e}")
    
    # ========== HELPER METHODS ==========
    
    def _get_object(self, obj_id: str) -> Optional[GameObject]:
        """
        Get an object by ID.
        
        Args:
            obj_id: Object ID
            
        Returns:
            GameObject or None
        """
        if obj_id in self.objects:
            return self.objects[obj_id]
        return None
    
    def _get_room(self, room_id: str) -> Optional[Room]:
        """
        Get a room by ID.
        
        Args:
            room_id: Room ID
            
        Returns:
            Room or None
        """
        if room_id in self.rooms:
            return self.rooms[room_id]
        return None
    
    def _get_object_or_room(self, id_str: str) -> Optional[Union[GameObject, Room]]:
        """
        Get an object or room by ID.
        
        Args:
            id_str: Object or room ID
            
        Returns:
            GameObject, Room, or None
        """
        # Check objects first
        obj = self._get_object(id_str)
        if obj:
            return obj
        
        # Check rooms
        room = self._get_room(id_str)
        if room:
            return room
        
        # Special case for HERE
        if id_str == "HERE":
            return self._get_room(self.HERE)
        
        # Special case for WINNER (player)
        if id_str in ["WINNER", "PLAYER"]:
            return self._get_object("PLAYER")
        
        return None
    
    # ========== STATE MANAGEMENT ==========
    
    def save_state(self) -> Dict[str, Any]:
        """
        Save the current game state.
        
        Returns:
            Dictionary containing all game state
        """
        try:
            state = {
                "globals": self.globals.copy(),
                "HERE": self.HERE,
                "WINNER": self.WINNER,
                "PRESENT_TIME": self.PRESENT_TIME,
                "PRSA": self.PRSA,
                "PRSO": self.PRSO,
                "PRSI": self.PRSI,
                "P_NUMBER": self.P_NUMBER,
                "objects": {
                    id: {
                        "location": obj.location,
                        "flags": list(obj.flags),
                        "properties": obj.properties.copy()
                    }
                    for id, obj in self.objects.items()
                },
                "rooms": {
                    id: {
                        "contents": room.contents.copy(),
                        "flags": list(room.flags),
                        "properties": room.properties.copy()
                    }
                    for id, room in self.rooms.items()
                },
                "events": [
                    {
                        "name": e.name,
                        "turns_remaining": e.turns_remaining,
                        "enabled": e.enabled,
                        "recurring": e.recurring,
                        "interval": e.interval
                    }
                    for e in self.events
                ]
            }
            logger.info("Game state saved")
            return state
        except Exception as e:
            logger.error(f"Error saving game state: {e}")
            raise GameException(f"Cannot save state: {e}")
    
    def load_state(self, state: Dict[str, Any]) -> None:
        """
        Load a saved game state.
        
        Args:
            state: Dictionary containing game state
        """
        try:
            self.globals = state["globals"].copy()
            self.HERE = state["HERE"]
            self.WINNER = state["WINNER"]
            self.PRESENT_TIME = state["PRESENT_TIME"]
            self.PRSA = state.get("PRSA")
            self.PRSO = state.get("PRSO")
            self.PRSI = state.get("PRSI")
            self.P_NUMBER = state.get("P_NUMBER")
            
            # Restore object states
            for obj_id, obj_state in state["objects"].items():
                if obj_id in self.objects:
                    self.objects[obj_id].location = obj_state["location"]
                    self.objects[obj_id].flags = set(obj_state["flags"])
                    self.objects[obj_id].properties = obj_state["properties"].copy()
            
            # Restore room states
            for room_id, room_state in state["rooms"].items():
                if room_id in self.rooms:
                    self.rooms[room_id].contents = room_state["contents"].copy()
                    self.rooms[room_id].flags = set(room_state["flags"])
                    self.rooms[room_id].properties = room_state["properties"].copy()
            
            # Restore events
            self.events = []
            for event_state in state.get("events", []):
                event = ScheduledEvent(
                    name=event_state["name"],
                    turns_remaining=event_state["turns_remaining"],
                    callback=lambda: None,  # Would be looked up
                    enabled=event_state["enabled"],
                    recurring=event_state.get("recurring", False),
                    interval=event_state.get("interval", 0)
                )
                self.events.append(event)
            
            logger.info("Game state loaded")
        except Exception as e:
            logger.error(f"Error loading game state: {e}")
            raise GameException(f"Cannot load state: {e}")