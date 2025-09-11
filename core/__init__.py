###############################################################################
#   core/__init__.py
#
#   Core game engine and object system
#   
###############################################################################
from .exceptions import (
    GameException,
    ParserException,
    CommandException,
    SaveLoadException,
    InvalidStateException,
    TimeException
)
from .flags import ObjectFlag

__all__ = [
    # Exceptions
    'GameException',
    'ParserException',
    'CommandException',
    'SaveLoadException',
    'InvalidStateException',
    'TimeException'

    # Systems
    'ObjectFlag',
]

"""
from .game_engine import GameEngine, GameState, GameConfig
from .game_object import (
    GameObject, 
    Room, 
    Item, 
    Container, 
    Character, 
    Player
)

from .property_system import PropertyManager
from .container_system import ContainerSystem


__all__ = [
    # Engine
    'GameEngine',
    'GameState', 
    'GameConfig',
    
    # Objects
    'GameObject',
    'Room',
    'Item',
    'Container',
    'Character',
    'Player',
    
    # Systems
    'PropertyManager',
    'ContainerSystem',
]
"""