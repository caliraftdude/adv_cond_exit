"""
Game interface - handles input/output with the player
"""

from core.engine import Engine


class GameInterface:
    """
    Main interface for player interaction.  Handles input, output, and display formatting
    XXX A LOT needs to be done in here - but stub this out until things start working...
    """
    
    def __init__(self, engine:Engine):
        """Initialize interface with game engine reference"""
        self.engine = engine

    