###############################################################################
#   core/engine.py
#
#   Integrated game engine to load and run text adventure games
#   
###############################################################################
from typing import Optional, Dict, Any
from enum import Flag, auto, Enum
import logging
from pathlib import Path
import json
from dataclasses import dataclass

from core.game_object import Manifest
from world.world_manager import WorldManager

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



        except Exception as e:
            pass

    def load_game(self, filename: str) -> bool:
        """
        Load a saved game state  -  Equivalent to ZIL's RESTORE routine
        """
        try:
            print(f"Loading game from {filename}...")
            return True
            #return self.save_manager.load(filename)
        except Exception as e:
            logger.error(f"Load failed: {e}")
            return False

    def start_game(self) -> None:
        """Start the main game loop"""
        print("Starting game loop...")
        pass


