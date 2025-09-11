###############################################################################
#   core/flags.py
#
#   Object flags - translated from ZIL FLAGS
#   
###############################################################################
from enum import Flag, auto

class ObjectFlag(Flag):
    """
    Object flags - equivalent to ZIL FLAGS
    These determine object behaviors and properties
    """
    NONE = 0
    CONTAINER = auto()      # Can contain other objects (CONTBIT)
    CONTBIT = auto()        # Can contain objects (e.g., mail slot)
    DOORBIT = auto()        # Object is a door
    DRINKABLE = auto()      # Can be drunk (DRINKBIT)
    EDIBLE = auto()         # Can be eaten (FOODBIT)
    EVIDENCE = auto()       # Is evidence (custom for Deadline)
    FEMALE = auto()         # Character is female (FEMALEBIT)
    FIXED = auto()          # Cannot be moved
    HIDDEN = auto()         # Not visible until found
    INVISIBLE = auto()      # Cannot be seen normally (INVISIBLE)
    LIGHT = auto()          # Provides light (LIGHTBIT)
    LOCKED = auto()         # Container is locked (LOCKEDBIT)
    LOCKEDBIT = auto()      # Door is locked
    NARTICLE = auto()       # No article needed (NARTICLEBIT)
    ONBIT = auto()             # Device is on (ONBIT)
    OPEN = auto()           # Container is open (OPENBIT)
    OPENBIT = auto()        # Door is currently open
    PERSON = auto()         # Is a person/character (PERSONBIT)
    PLURAL = auto()         # Object is plural (PLURALBIT)
    PROPER = auto()         # Proper noun (PROPERBIT)
    READABLE = auto()       # Can be read (READBIT)
    RLANDBIT = auto()        # Room has been visited (RLANDBIT)
    SACRED = auto()         # Cannot be dropped (SACREDBIT)
    SEARCHED = auto()       # Has been searched
    SURFACE = auto()        # Objects can be placed on it (SURFACEBIT)
    TAKEABLE = auto()       # Can be picked up (TAKEBIT)
    TOOL = auto()           # Is a tool (TOOLBIT)
    TOUCHABLE = auto()      # Can be touched (TOUCHBIT)
    TRANSBIT = auto()       # Can see through (glass door, window)
    TRANSPARENT = auto()    # Can see through it (TRANSBIT)
    VEHICLE = auto()        # Can be ridden/entered (VEHBIT)
    WEAPON = auto()         # Is a weapon (WEAPONBIT)
    WEARABLE = auto()       # Can be worn (WEARBIT)