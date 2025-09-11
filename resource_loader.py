"""
Resource Loader - Dynamic loading and wiring of game resources
This module handles loading JSON data, Python action scripts, and connecting them together.
"""
import json
import logging
import importlib
import importlib.util
from pathlib import Path
from typing import Dict, Any, Optional, List, Callable, Type, Union, Tuple
from dataclasses import dataclass, field
import inspect
import sys

from game import GameObject, Room, Game, GameException

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ResourceLoadError(GameException):
    """Exception raised when resource loading fails"""
    pass


class ActionRegistryError(GameException):
    """Exception raised when action registration fails"""
    pass


@dataclass
class ResourceManifest:
    """
    Describes all resources to be loaded for a game module.
    This is typically loaded from game.json
    """
    game_name: str
    version: str
    author: str = ""
    description: str = ""
    
    # Resource files
    rooms_file: str = "rooms.json"
    objects_file: str = "objects.json"
    doors_file: str = "doors.json"
    characters_file: str = "characters.json"
    vocabulary_file: str = "vocabulary.json"
    syntax_file: str = "syntax.json"
    schedules_file: str = "schedules.json"
    
    # Python modules
    action_modules: List[str] = field(default_factory=list)
    event_modules: List[str] = field(default_factory=list)
    custom_modules: List[str] = field(default_factory=list)
    
    # Additional configuration
    config: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_json(cls, json_path: Path) -> 'ResourceManifest':
        """Load manifest from JSON file"""
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
            
            # Map JSON keys to manifest fields
            return cls(
                game_name=data.get("game_name", "Unknown Game"),
                version=data.get("version", "1.0.0"),
                author=data.get("author", ""),
                description=data.get("description", ""),
                rooms_file=data.get("rooms", "rooms.json"),
                objects_file=data.get("objects", "objects.json"),
                doors_file=data.get("doors", "doors.json"),
                characters_file=data.get("characters", "characters.json"),
                vocabulary_file=data.get("vocabulary", "vocabulary.json"),
                syntax_file=data.get("syntax", "syntax.json"),
                schedules_file=data.get("schedules", "schedules.json"),
                action_modules=data.get("action_modules", ["actions"]),
                event_modules=data.get("event_modules", []),
                custom_modules=data.get("custom_modules", []),
                config=data.get("config", {})
            )
        except Exception as e:
            logger.error(f"Failed to load manifest from {json_path}: {e}")
            raise ResourceLoadError(f"Cannot load manifest: {e}")


class ActionRegistry:
    """
    Registry for action handlers that can be called by objects/rooms.
    Maps action function names to their implementations.
    """
    
    def __init__(self):
        self.actions: Dict[str, Callable] = {}
        self.object_actions: Dict[str, Dict[str, Callable]] = {}
        self.room_actions: Dict[str, Dict[str, Callable]] = {}
        
    def register_action(self, name: str, handler: Callable, 
                       object_id: Optional[str] = None,
                       room_id: Optional[str] = None) -> None:
        """
        Register an action handler.
        
        Args:
            name: Action name
            handler: Function to handle the action
            object_id: If specified, register for specific object
            room_id: If specified, register for specific room
        """
        if object_id:
            if object_id not in self.object_actions:
                self.object_actions[object_id] = {}
            self.object_actions[object_id][name] = handler
            logger.debug(f"Registered action {name} for object {object_id}")
            
        elif room_id:
            if room_id not in self.room_actions:
                self.room_actions[room_id] = {}
            self.room_actions[room_id][name] = handler
            logger.debug(f"Registered action {name} for room {room_id}")
            
        else:
            self.actions[name] = handler
            logger.debug(f"Registered global action {name}")
    
    def get_action(self, name: str, object_id: Optional[str] = None,
                  room_id: Optional[str] = None) -> Optional[Callable]:
        """
        Get an action handler.
        
        Args:
            name: Action name
            object_id: Object ID for object-specific actions
            room_id: Room ID for room-specific actions
            
        Returns:
            Action handler function or None
        """
        # Check object-specific actions first
        if object_id and object_id in self.object_actions:
            if name in self.object_actions[object_id]:
                return self.object_actions[object_id][name]
        
        # Then check room-specific actions
        if room_id and room_id in self.room_actions:
            if name in self.room_actions[room_id]:
                return self.room_actions[room_id][name]
        
        # Finally check global actions
        return self.actions.get(name)


class ResourceLoader:
    """
    Main resource loader that handles loading all game resources
    and wiring them together.
    """
    
    def __init__(self, game: Game):
        """
        Initialize the resource loader.
        
        Args:
            game: Game instance to load resources into
        """
        self.game = game
        self.action_registry = ActionRegistry()
        self.loaded_modules: Dict[str, Any] = {}
        self.module_path: Optional[Path] = None
        
    def load_game_module(self, module_path: Union[str, Path]) -> bool:
        """
        Load a complete game module with all its resources.
        
        Args:
            module_path: Path to the game module directory
            
        Returns:
            True if successful
        """
        try:
            self.module_path = Path(module_path)
            
            # Load the manifest
            manifest_path = self.module_path / "game.json"
            if not manifest_path.exists():
                logger.error(f"No game.json found in {self.module_path}")
                return False
            
            manifest = ResourceManifest.from_json(manifest_path)
            logger.info(f"Loading game module: {manifest.game_name} v{manifest.version}")
            
            # Load resources in order
            success = True
            
            # 1. Load vocabulary first (needed by parser)
            if not self._load_vocabulary(self.module_path / manifest.vocabulary_file):
                logger.warning("Failed to load vocabulary")
                success = False
            
            # 2. Load syntax rules
            if not self._load_syntax(self.module_path / manifest.syntax_file):
                logger.warning("Failed to load syntax rules")
                success = False
            
            # 3. Load Python modules (action handlers)
            for module_name in manifest.action_modules:
                if not self._load_python_module(module_name, "actions"):
                    logger.warning(f"Failed to load action module: {module_name}")
                    success = False
            
            for module_name in manifest.event_modules:
                if not self._load_python_module(module_name, "events"):
                    logger.warning(f"Failed to load event module: {module_name}")
                    success = False
            
            for module_name in manifest.custom_modules:
                if not self._load_python_module(module_name, "custom"):
                    logger.warning(f"Failed to load custom module: {module_name}")
                    success = False
            
            # 4. Load game data (rooms, objects, etc.)
            if not self._load_rooms(self.module_path / manifest.rooms_file):
                logger.error("Failed to load rooms")
                success = False
            
            if not self._load_objects(self.module_path / manifest.objects_file):
                logger.error("Failed to load objects")
                success = False
            
            if not self._load_doors(self.module_path / manifest.doors_file):
                logger.warning("Failed to load doors")
                success = False
            
            if not self._load_characters(self.module_path / manifest.characters_file):
                logger.warning("Failed to load characters")
                success = False
            
            # 5. Load schedules and events
            if not self._load_schedules(self.module_path / manifest.schedules_file):
                logger.warning("Failed to load schedules")
                success = False
            
            # 6. Wire actions to objects/rooms
            self._wire_actions()
            
            # 7. Apply additional configuration
            self._apply_config(manifest.config)
            
            logger.info(f"Game module loaded: {success}")
            return success
            
        except Exception as e:
            logger.error(f"Error loading game module: {e}")
            return False
    
    def _load_vocabulary(self, vocab_path: Path) -> bool:
        """Load vocabulary data"""
        try:
            if not vocab_path.exists():
                logger.debug(f"Vocabulary file not found: {vocab_path}")
                return False
            
            with open(vocab_path, 'r') as f:
                data = json.load(f)
            
            # Store vocabulary in game
            if isinstance(data, dict):
                self.game.vocabulary.update(data)
            elif isinstance(data, list):
                # Convert list format to dict
                for entry in data:
                    if "word" in entry and "type" in entry:
                        word = entry["word"]
                        word_type = entry["type"]
                        if word_type not in self.game.vocabulary:
                            self.game.vocabulary[word_type] = []
                        self.game.vocabulary[word_type].append(word)
            
            logger.info(f"Loaded vocabulary from {vocab_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading vocabulary: {e}")
            return False
    
    def _load_syntax(self, syntax_path: Path) -> bool:
        """Load syntax rules"""
        try:
            if not syntax_path.exists():
                logger.debug(f"Syntax file not found: {syntax_path}")
                return False
            
            with open(syntax_path, 'r') as f:
                data = json.load(f)
            
            # Store syntax rules (parser will use these)
            self.game.globals["SYNTAX_RULES"] = data
            
            logger.info(f"Loaded syntax rules from {syntax_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading syntax rules: {e}")
            return False
    
    def _load_rooms(self, rooms_path: Path) -> bool:
        """Load room data"""
        try:
            if not rooms_path.exists():
                logger.debug(f"Rooms file not found: {rooms_path}")
                return False
            
            with open(rooms_path, 'r') as f:
                data = json.load(f)
            
            # Create Room objects
            for room_id, room_data in data.items():
                room = Room(
                    id=room_id,
                    name=room_data.get("name", room_id),
                    description=room_data.get("description", ""),
                    exits=room_data.get("exits", {}),
                    contents=room_data.get("contents", []),
                    flags=set(room_data.get("flags", [])),
                    properties=room_data.get("properties", {})
                )
                
                # Store action handler name if specified
                if "action" in room_data:
                    room.properties["__action_handler__"] = room_data["action"]
                
                self.game.rooms[room_id] = room
            
            logger.info(f"Loaded {len(self.game.rooms)} rooms from {rooms_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading rooms: {e}")
            return False
    
    def _load_objects(self, objects_path: Path) -> bool:
        """Load object data"""
        try:
            if not objects_path.exists():
                logger.debug(f"Objects file not found: {objects_path}")
                return False
            
            with open(objects_path, 'r') as f:
                data = json.load(f)
            
            # Create GameObject instances
            for obj_id, obj_data in data.items():
                obj = GameObject(
                    id=obj_id,
                    name=obj_data.get("name", obj_id),
                    description=obj_data.get("description", ""),
                    location=obj_data.get("location"),
                    flags=set(obj_data.get("flags", [])),
                    properties=obj_data.get("properties", {}),
                    contents=obj_data.get("contents", [])
                )
                
                # Store action handler name if specified
                if "action" in obj_data:
                    obj.properties["__action_handler__"] = obj_data["action"]
                
                self.game.objects[obj_id] = obj
            
            logger.info(f"Loaded {len(self.game.objects)} objects from {objects_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading objects: {e}")
            return False
    
    def _load_doors(self, doors_path: Path) -> bool:
        """Load door data"""
        try:
            if not doors_path.exists():
                logger.debug(f"Doors file not found: {doors_path}")
                return False
            
            with open(doors_path, 'r') as f:
                data = json.load(f)
            
            # Doors are special objects
            for door_id, door_data in data.items():
                door = GameObject(
                    id=door_id,
                    name=door_data.get("name", door_id),
                    description=door_data.get("description", ""),
                    location=door_data.get("location"),
                    flags=set(door_data.get("flags", ["DOORBIT"])),
                    properties=door_data.get("properties", {})
                )
                
                # Store connections
                if "connects" in door_data:
                    door.properties["connects"] = door_data["connects"]
                
                # Store action handler name if specified
                if "action" in door_data:
                    door.properties["__action_handler__"] = door_data["action"]
                
                self.game.objects[door_id] = door
            
            logger.info(f"Loaded {len(data)} doors from {doors_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading doors: {e}")
            return False
    
    def _load_characters(self, chars_path: Path) -> bool:
        """Load character data"""
        try:
            if not chars_path.exists():
                logger.debug(f"Characters file not found: {chars_path}")
                return False
            
            with open(chars_path, 'r') as f:
                data = json.load(f)
            
            # Characters are special objects with additional properties
            for char_id, char_data in data.items():
                character = GameObject(
                    id=char_id,
                    name=char_data.get("name", char_id),
                    description=char_data.get("description", ""),
                    location=char_data.get("location"),
                    flags=set(char_data.get("flags", ["CHARACTER"])),
                    properties=char_data.get("properties", {})
                )
                
                # Store dialogue, schedule, etc.
                if "dialogue" in char_data:
                    character.properties["dialogue"] = char_data["dialogue"]
                if "schedule" in char_data:
                    character.properties["schedule"] = char_data["schedule"]
                if "knowledge" in char_data:
                    character.properties["knowledge"] = char_data["knowledge"]
                
                # Store action handler name if specified
                if "action" in char_data:
                    character.properties["__action_handler__"] = char_data["action"]
                
                self.game.objects[char_id] = character
            
            logger.info(f"Loaded {len(data)} characters from {chars_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading characters: {e}")
            return False
    
    def _load_schedules(self, schedules_path: Path) -> bool:
        """Load schedule/event data"""
        try:
            if not schedules_path.exists():
                logger.debug(f"Schedules file not found: {schedules_path}")
                return False
            
            with open(schedules_path, 'r') as f:
                data = json.load(f)
            
            # Store schedules for later processing
            self.game.globals["SCHEDULES"] = data
            
            logger.info(f"Loaded schedules from {schedules_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading schedules: {e}")
            return False
    
    def _load_python_module(self, module_name: str, module_type: str) -> bool:
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
            module_file = self.module_path / f"{module_name}.py"
            
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
                
                # Register action handlers based on module type
                if module_type == "actions":
                    self._register_action_handlers(module)
                elif module_type == "events":
                    self._register_event_handlers(module)
                elif module_type == "custom":
                    self._register_custom_handlers(module)
                
                logger.info(f"Loaded Python module: {module_name}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error loading Python module {module_name}: {e}")
            return False
    
    def _register_action_handlers(self, module: Any) -> None:
        """
        Register action handlers from a module.
        Looks for functions ending with _F (ZIL convention).
        """
        try:
            for name, obj in inspect.getmembers(module):
                # Look for functions ending with _F
                if callable(obj) and name.endswith("_F"):
                    # Extract the object/room name
                    base_name = name[:-2]  # Remove _F suffix
                    
                    # Register the handler
                    self.action_registry.register_action(name, obj)
                    
                    # Also register with cleaner name
                    self.action_registry.register_action(base_name, obj)
                    
                    logger.debug(f"Registered action handler: {name}")
                    
        except Exception as e:
            logger.error(f"Error registering action handlers: {e}")
    
    def _register_event_handlers(self, module: Any) -> None:
        """
        Register event handlers from a module.
        Looks for functions starting with I_ (interrupt/event convention).
        """
        try:
            for name, obj in inspect.getmembers(module):
                # Look for functions starting with I_
                if callable(obj) and name.startswith("I_"):
                    # Register as event handler
                    self.action_registry.register_action(name, obj)
                    logger.debug(f"Registered event handler: {name}")
                    
        except Exception as e:
            logger.error(f"Error registering event handlers: {e}")
    
    def _register_custom_handlers(self, module: Any) -> None:
        """
        Register custom handlers from a module.
        Registers all callable objects that don't follow standard conventions.
        """
        try:
            for name, obj in inspect.getmembers(module):
                if callable(obj) and not name.startswith("_"):
                    # Register custom handler
                    self.action_registry.register_action(name, obj)
                    logger.debug(f"Registered custom handler: {name}")
                    
        except Exception as e:
            logger.error(f"Error registering custom handlers: {e}")
    
    def _wire_actions(self) -> None:
        """
        Wire action handlers to objects and rooms.
        Connects the __action_handler__ property to actual functions.
        """
        try:
            # Wire object actions
            for obj_id, obj in self.game.objects.items():
                if "__action_handler__" in obj.properties:
                    handler_name = obj.properties["__action_handler__"]
                    
                    # Try to find the handler
                    handler = self.action_registry.get_action(handler_name)
                    if not handler:
                        # Try with _F suffix
                        handler = self.action_registry.get_action(f"{handler_name}_F")
                    
                    if handler:
                        obj.action_handler = handler
                        logger.debug(f"Wired action {handler_name} to object {obj_id}")
                    else:
                        logger.warning(f"Action handler {handler_name} not found for object {obj_id}")
            
            # Wire room actions
            for room_id, room in self.game.rooms.items():
                if "__action_handler__" in room.properties:
                    handler_name = room.properties["__action_handler__"]
                    
                    # Try to find the handler
                    handler = self.action_registry.get_action(handler_name)
                    if not handler:
                        # Try with _F suffix
                        handler = self.action_registry.get_action(f"{handler_name}_F")
                    
                    if handler:
                        room.action_handler = handler
                        logger.debug(f"Wired action {handler_name} to room {room_id}")
                    else:
                        logger.warning(f"Action handler {handler_name} not found for room {room_id}")
                        
        except Exception as e:
            logger.error(f"Error wiring actions: {e}")
    
    def _apply_config(self, config: Dict[str, Any]) -> None:
        """
        Apply additional configuration from the manifest.
        
        Args:
            config: Configuration dictionary
        """
        try:
            # Set game configuration
            for key, value in config.items():
                self.game.globals[f"CONFIG_{key.upper()}"] = value
            
            # Set specific configuration items
            if "start_room" in config:
                self.game.HERE = config["start_room"]
            
            if "start_time" in config:
                self.game.PRESENT_TIME = config["start_time"]
            
            if "max_score" in config:
                self.game.globals["MAX_SCORE"] = config["max_score"]
            
            if "debug" in config:
                self.game.globals["DEBUG_MODE"] = config["debug"]
            
            logger.info("Applied game configuration")
            
        except Exception as e:
            logger.error(f"Error applying configuration: {e}")
    
    def get_action(self, name: str, context: Optional[Union[GameObject, Room]] = None) -> Optional[Callable]:
        """
        Get an action handler with context.
        
        Args:
            name: Action name
            context: Object or room for context-specific actions
            
        Returns:
            Action handler or None
        """
        if context:
            if isinstance(context, GameObject):
                return self.action_registry.get_action(name, object_id=context.id)
            elif isinstance(context, Room):
                return self.action_registry.get_action(name, room_id=context.id)
        
        return self.action_registry.get_action(name)
    
    def reload_module(self, module_name: str) -> bool:
        """
        Reload a Python module (useful for development).
        
        Args:
            module_name: Name of module to reload
            
        Returns:
            True if successful
        """
        try:
            if module_name in self.loaded_modules:
                module = self.loaded_modules[module_name]
                importlib.reload(module)
                
                # Re-register handlers
                self._register_action_handlers(module)
                
                # Re-wire actions
                self._wire_actions()
                
                logger.info(f"Reloaded module: {module_name}")
                return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error reloading module {module_name}: {e}")
            return False


def load_game_module(game: Game, module_path: Union[str, Path]) -> ResourceLoader:
    """
    Convenience function to load a game module.
    
    Args:
        game: Game instance
        module_path: Path to game module
        
    Returns:
        ResourceLoader instance with loaded resources
    """
    loader = ResourceLoader(game)
    loader.load_game_module(module_path)
    return loader