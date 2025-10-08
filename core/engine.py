###############################################################################
#   core/engine.py
#
#   Integrated game engine to load and run text adventure games.  Since
#   the API class is closely related and unfortunately circular, its maintained
#   here to avoid frustrating import errors and nonsense.  This might need to 
#   be refactored later - I am just not 100% sure how it would be organized at
#   this time.
#   
###############################################################################
from typing import Optional, Dict, Any, Union
from enum import Flag, auto, Enum
import logging
from pathlib import Path
import json
from dataclasses import dataclass

from core.game_object import Manifest
from world.world_manager import WorldManager
from core.exceptions import GameException

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

    


class GameState(Enum):
    """Game state enumeration - matches ZIL game states"""
    PLAYING = auto()
    PAUSED = auto()
    ENDED = auto()
    WON = auto()
    LOST = auto()
    QUIT = auto()

class Engine:
    """
    Main game engine - translated from ZIL DEADLINE.ZIL
    Manages game state, coordinates subsystems, and drives gameplay
    """
    
    def __init__(self, data_path: Path):
        self.data_path: Path = data_path
        self.debug_mode: bool = False
        
        # Core game state - equivalent to ZIL globals
        self.state: GameState = GameState.PLAYING
        # self.score = 0
        # self.moves = 0
        # self.current_time = self.config.start_time
        # self.winner: Optional[str] = None
        self.manifest: Optional[Manifest] = None
        
        # Game subsystems (will be initialized separately)
        self.world_manager: WorldManager = None
        self.api: API = None
        self.parser = None
        self.time_manager = None
        self.command_processor = None
        self.interface = None
        self.save_manager = None
        
        # Game data storage (XXX does this make sense?)
        self.game_data: Dict[str, Any] = {}
        
        # Performance tracking
        self.performance_stats = {
            'commands_processed': 0,
            'total_processing_time': 0,
            'average_response_time': 0
        }
        
        logger.info(f"Game Engine initialized with data path: {data_path}")


    def load_game_data(self)-> bool:
        """
        Load game data from JSON files
        Equivalent to ZIL's compile-time object definitions
        
        Returns:
            True if data loaded successfully
        """
        print("Loading game manifest...")

        try:
            manifestfile = self.data_path / "game.json"
            if not manifestfile.exists():
                logger.error(f"Manifest file not found: {manifestfile}")
                return False
            
            # Load main game data
            self.manifest = Manifest.from_json(manifestfile)
            if not self.manifest:
                logger.error("Failed to parse game manifest.")
                return False
            
            # Log and print manifest info if found
            logger.info(f"Loaded manifest for game: {self.manifest.game_name} v{self.manifest.version}")
            print(f"Found game: {self.manifest.game_name} v{self.manifest.version}")

            return True
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in game data: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to load game data: {e}")
            return False


    def initialize_subsystems(self)-> bool:
        """Initialize game state and objects"""
        print("Initializing game...")

        try:
            # Initialize world manager
            self.world_manager = WorldManager(self.manifest, self.data_path)
            self.world_manager.initialize_world() # should deal with init failure

            self.api = API(self)
            # XXX porting starts here..
            # from parser.parser import GameParser

            # from game_time.time_manager import TimeManager
            # from commands.base_command import CommandProcessor
            # from game_io.interface import GameInterface
            # from game_io.save_system import SaveManager
            
            # # Initialize world from data
            # self.world_manager = WorldManager(self.game_data)
            # self.world_manager.initialize_world()
            
            # # Initialize parser with vocabulary
            # self.parser = GameParser(self.vocabulary, self.syntax_rules)
            
            # # Initialize time system
            # self.time_manager = TimeManager(self.current_time)
            # schedules_file = self.data_path / "schedules.json"
            # if schedules_file.exists():
            #     self.time_manager.load_schedules(schedules_file)
            
            # # Initialize command processor
            # self.command_processor = CommandProcessor(self)
            
            # # Initialize user interface
            # self.interface = GameInterface(self)
            
            # # Initialize save system
            # self.save_manager = SaveManager(self)
        
            logger.info("All subsystems initialized")

        # XXX Need a better exception...
        except Exception as e:
            pass

    def load_game(self, filename: str) -> bool:
        """
        Load a saved game state  -  Equivalent to ZIL's RESTORE routine
        """
        try:
            # XXX Nothing here - a lot of work to implement this
            print(f"Loading game from {filename}...")
            return True
            #return self.save_manager.load(filename)
        except Exception as e:
            logger.error(f"Load failed: {e}")
            return False

    def start_game(self) -> None:
        """Start the main game loop"""
        print("Starting game loop...")

        print("##############################################################################################")
        print("#\tTesting API calls and so on here...")
        print("##############################################################################################")

        function = self.world_manager.function_registry.get("init_globals")(self.api)
        
        print("AGGHHAA!!!")
        
        pass



class API:
    """
    Main Game API class providing all game.* functions for action scripts.  This class maintains all 
    game state and provides the interface for game actions to interact with the game world.
    """
    
    def __init__(self, engine: Engine = None):
        self.engine = engine

    # ========== OUTPUT FUNCTIONS ==========
    def TELL(self, text: str, end: str = "\n") -> None:
        """
        Output text to the player.
        Equivalent to ZIL's TELL.
        
        Args:
            text: Text to output
            end: End character (default newline)
        """
        try:
            self.output_buffer.append(text)
            if end == "\n":
                print(''.join(self.output_buffer))
                self.output_buffer.clear()
            logger.debug(f"TELL: {text}")
        except Exception as e:
            logger.error(f"Error in TELL: {e}")
            raise GameException(f"Output error: {e}")
    
    def TELL_N(self, number: Union[int, float]) -> None:
        """
        Output a number to the player.
        Equivalent to ZIL's PRINTN.
        
        Args:
            number: Number to output
        """
        try:
            self.TELL(str(number), end="")
            logger.debug(f"TELL_N: {number}")
        except Exception as e:
            logger.error(f"Error in TELL_N: {e}")
            raise GameException(f"Output number error: {e}")


    # ========== GLOBAL VARIABLE FUNCTIONS ==========
    def SETG(self, name: str, value: Any) -> None:
        """
        Set a global variable.
        Equivalent to ZIL's SETG.
        
        Args:
            name: Variable name
            value: Value to set
        """
        try:
            self.engine.world_manager.global_vars[name] = value
            logger.debug(f"SETG: {name} = {value}")
        except Exception as e:
            logger.error(f"Error setting global {name}: {e}")
            raise GameException(f"Cannot set global variable {name}: {e}")
    
    def GETG(self, name: str, default: Any = None) -> Any:
        """
        Get a global variable value.
        Equivalent to ZIL's GVAL.
        
        Args:
            name: Variable name
            default: Default value if not found
            
        Returns:
            The global variable value or default
        """
        try:
            value = self.engine.world_manager.global_objects.get(name, None)
            logger.debug(f"GETG: {name} = {value}")
            return value
        except Exception as e:
            logger.error(f"Error getting global {name}: {e}")
            raise GameException(f"Cannot get global variable {name}: {e}")


