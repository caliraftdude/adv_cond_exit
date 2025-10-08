###############################################################################
#   core/exceptions.py
#
#   Custome excpetions for the game core module
#   
###############################################################################

class GameException(Exception):
    """Base exception for game-related errors"""
    pass

class ParserException(GameException):
    """Exception raised during parsing"""
    pass

class CommandException(GameException):
    """Exception raised during command execution"""
    pass

class SaveLoadException(GameException):
    """Exception raised during save/load operations"""
    pass

class InvalidStateException(GameException):
    """Exception raised when game state is invalid"""
    pass

class TimeException(GameException):
    """Exception raised for time-related errors"""
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

class ResourceLoadError(GameException):
    """Exception raised when resource loading fails"""
    pass


class ActionRegistryError(GameException):
    """Exception raised when action registration fails"""
    pass

class AttributeNotFoundButInJSON(GameException):
    """Exception raised when deserializing a JSON file and finding that the corresponding class is missing an attribute"""
    pass