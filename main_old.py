from typing import Dict, Any, Optional, Union, Callable
from dataclasses import dataclass
from enum import Enum
import json


class ExitType(Enum):
    """Types of exits as defined in ZIL handbook"""
    UNCONDITIONAL = "unconditional"          # (NORTH TO ROUND-ROOM)
    NON_EXIT = "non_exit"                     # (SOUTH "You would be killed...")
    CONDITIONAL = "conditional"               # (EAST TO STRANGE-PASSAGE IF CYCLOPS-FLAG)
    DOOR = "door"                            # (EAST TO RED-DOCK IF AIRLOCK-DOOR IS OPEN)
    FLEXIBLE = "flexible"                    # (WEST PER BRIDGE-EXIT-F)


@dataclass
class ExitDefinition:
    """Represents any type of exit from ZIL"""
    exit_type: ExitType
    destination: Optional[str] = None        # Target room
    condition_var: Optional[str] = None      # Global variable name for conditional exits
    door_object: Optional[str] = None        # Door object name for door exits
    routine_name: Optional[str] = None       # Routine name for flexible exits
    failure_message: Optional[str] = None    # Custom failure message
    default_message: str = "You can't go that way."


class ZilExitEvaluator:
    """Evaluates ZIL-style exits against game state"""
    
    def __init__(self, world_manager):
        self.world_manager = world_manager
        
    def evaluate_exit(self, direction: str, exit_def: ExitDefinition) -> tuple[bool, Optional[str], str]:
        """
        Evaluate an exit and return (can_go, destination, message)
        
        Returns:
            tuple: (success: bool, destination: str|None, message: str)
        """
        
        if exit_def.exit_type == ExitType.UNCONDITIONAL:
            return self._evaluate_unconditional(exit_def)
            
        elif exit_def.exit_type == ExitType.NON_EXIT:
            return self._evaluate_non_exit(exit_def)
            
        elif exit_def.exit_type == ExitType.CONDITIONAL:
            return self._evaluate_conditional(exit_def)
            
        elif exit_def.exit_type == ExitType.DOOR:
            return self._evaluate_door(exit_def)
            
        elif exit_def.exit_type == ExitType.FLEXIBLE:
            return self._evaluate_flexible(direction, exit_def)
            
        return False, None, exit_def.default_message
    
    def _evaluate_unconditional(self, exit_def: ExitDefinition) -> tuple[bool, Optional[str], str]:
        """Handle unconditional exits: (NORTH TO ROUND-ROOM)"""
        return True, exit_def.destination, ""
    
    def _evaluate_non_exit(self, exit_def: ExitDefinition) -> tuple[bool, Optional[str], str]:
        """Handle non-exits: (SOUTH "You would be killed by the pounding surf!")"""
        return False, None, exit_def.failure_message or exit_def.default_message
    
    def _evaluate_conditional(self, exit_def: ExitDefinition) -> tuple[bool, Optional[str], str]:
        """Handle conditional exits: (EAST TO STRANGE-PASSAGE IF CYCLOPS-FLAG)"""
        # Check global variable/flag
        condition_value = self.world_manager.get_global_variable(exit_def.condition_var)
        
        if condition_value:
            return True, exit_def.destination, ""
        else:
            message = exit_def.failure_message or exit_def.default_message
            return False, None, message
    
    def _evaluate_door(self, exit_def: ExitDefinition) -> tuple[bool, Optional[str], str]:
        """Handle door exits: (EAST TO RED-DOCK IF AIRLOCK-DOOR IS OPEN)"""
        door = self.world_manager.get_object(exit_def.door_object)
        
        if door and door.has_flag("OPENBIT"):
            return True, exit_def.destination, ""
        else:
            # Generate door-specific message: "The airlock door is closed."
            door_desc = door.get_short_description() if door else exit_def.door_object
            message = f"The {door_desc} is closed."
            return False, None, message
    
    def _evaluate_flexible(self, direction: str, exit_def: ExitDefinition) -> tuple[bool, Optional[str], str]:
        """Handle flexible exits: (WEST PER BRIDGE-EXIT-F)"""
        routine = getattr(self.world_manager, exit_def.routine_name, None)
        
        if routine and callable(routine):
            result = routine(direction)
            
            if result is False or result is None:
                # Routine should have printed its own message
                return False, None, ""
            elif isinstance(result, str):
                # Routine returned new location
                return True, result, ""
            else:
                # Assume success, routine handled everything
                return True, str(result), ""
        
        return False, None, f"Exit routine {exit_def.routine_name} not found."


class ZilRoom:
    """Room class that handles all ZIL exit types"""
    
    def __init__(self, room_id: str, data: Dict[str, Any]):
        self.id = room_id
        self.name = data["name"]
        self.description = data["description"]
        self.exits = self._load_exits(data.get("exits", {}))
        
    def _load_exits(self, exits_data: Dict[str, Any]) -> Dict[str, ExitDefinition]:
        """Load exits from JSON data supporting all ZIL exit types"""
        exits = {}
        
        for direction, exit_info in exits_data.items():
            if isinstance(exit_info, str):
                # Simple unconditional exit: "north": "ROUND-ROOM"
                exits[direction] = ExitDefinition(
                    exit_type=ExitType.UNCONDITIONAL,
                    destination=exit_info
                )
                
            elif isinstance(exit_info, dict):
                exit_type = ExitType(exit_info["type"])
                
                if exit_type == ExitType.UNCONDITIONAL:
                    exits[direction] = ExitDefinition(
                        exit_type=ExitType.UNCONDITIONAL,
                        destination=exit_info["destination"]
                    )
                    
                elif exit_type == ExitType.NON_EXIT:
                    exits[direction] = ExitDefinition(
                        exit_type=ExitType.NON_EXIT,
                        failure_message=exit_info["message"]
                    )
                    
                elif exit_type == ExitType.CONDITIONAL:
                    exits[direction] = ExitDefinition(
                        exit_type=ExitType.CONDITIONAL,
                        destination=exit_info["destination"],
                        condition_var=exit_info["condition_var"],
                        failure_message=exit_info.get("failure_message")
                    )
                    
                elif exit_type == ExitType.DOOR:
                    exits[direction] = ExitDefinition(
                        exit_type=ExitType.DOOR,
                        destination=exit_info["destination"],
                        door_object=exit_info["door_object"]
                    )
                    
                elif exit_type == ExitType.FLEXIBLE:
                    exits[direction] = ExitDefinition(
                        exit_type=ExitType.FLEXIBLE,
                        routine_name=exit_info["routine_name"]
                    )
                    
        return exits
    
    def try_exit(self, direction: str, evaluator: ZilExitEvaluator) -> tuple[bool, Optional[str], str]:
        """Attempt to use an exit in the given direction"""
        exit_def = self.exits.get(direction.lower())
        
        if not exit_def:
            return False, None, "You can't go that way."
            
        return evaluator.evaluate_exit(direction, exit_def)
    
    def get_available_exits(self, evaluator: ZilExitEvaluator) -> Dict[str, str]:
        """Get all currently available exits (excludes non-exits and failed conditionals)"""
        available = {}
        
        for direction, exit_def in self.exits.items():
            if exit_def.exit_type != ExitType.NON_EXIT:
                can_go, destination, _ = evaluator.evaluate_exit(direction, exit_def)
                if can_go and destination:
                    available[direction] = destination
                    
        return available


# Example JSON definitions demonstrating all exit types
EXAMPLE_ROOM_DATA = {
    "COMPLEX-ROOM": {
        "name": "Complex Room",
        "description": "A room demonstrating all types of ZIL exits.",
        "exits": {
            # Unconditional Exit: (NORTH TO ROUND-ROOM)
            "north": "ROUND-ROOM",
            
            # Alternative unconditional syntax
            "northeast": {
                "type": "unconditional",
                "destination": "ANOTHER-ROOM"
            },
            
            # Non-Exit: (SOUTH "You would be killed by the pounding surf!")
            "south": {
                "type": "non_exit",
                "message": "You would be killed by the pounding surf!"
            },
            
            # Conditional Exit: (EAST TO STRANGE-PASSAGE IF CYCLOPS-FLAG)
            "east": {
                "type": "conditional",
                "destination": "STRANGE-PASSAGE",
                "condition_var": "CYCLOPS-FLAG"
            },
            
            # Conditional Exit with custom message: (WEST TO SECRET IF FLAG ELSE "No!")
            "west": {
                "type": "conditional", 
                "destination": "SECRET-ROOM",
                "condition_var": "SECRET-FLAG",
                "failure_message": "The way is blocked!"
            },
            
            # Door Exit: (UP TO RED-DOCK IF AIRLOCK-DOOR IS OPEN)
            "up": {
                "type": "door",
                "destination": "RED-DOCK", 
                "door_object": "AIRLOCK-DOOR"
            },
            
            # Flexible Exit: (DOWN PER BRIDGE-EXIT-F)
            "down": {
                "type": "flexible",
                "routine_name": "bridge_exit_routine"
            }
        }
    }
}


# Example usage and comprehensive testing
def example_usage():
    """Demonstrate all ZIL exit types"""
    
    # Mock world manager with all necessary components
    class MockWorldManager:
        def __init__(self):
            self.global_variables = {
                "CYCLOPS-FLAG": True,   # Conditional exit will work
                "SECRET-FLAG": False    # Conditional exit will fail
            }
            self.objects = {
                "AIRLOCK-DOOR": MockGameObject("AIRLOCK-DOOR", 
                    flags={"OPENBIT"}, 
                    short_desc="airlock door")
            }
        
        def get_global_variable(self, var_name):
            return self.global_variables.get(var_name, False)
        
        def get_object(self, obj_id):
            return self.objects.get(obj_id)
        
        def bridge_exit_routine(self, direction):
            """Example flexible exit routine"""
            print("The bridge creaks ominously as you cross...")
            # Return new location or False
            return "ACROSS-BRIDGE" if direction == "down" else False
    
    class MockGameObject:
        def __init__(self, obj_id, flags=None, short_desc=None):
            self.id = obj_id
            self.flags = flags or set()
            self.short_desc = short_desc or obj_id.lower().replace("-", " ")
            
        def has_flag(self, flag):
            return flag in self.flags
            
        def get_short_description(self):
            return self.short_desc
    
    # Create world manager and evaluator
    world_manager = MockWorldManager()
    evaluator = ZilExitEvaluator(world_manager)
    
    # Create test room
    room = ZilRoom("COMPLEX-ROOM", EXAMPLE_ROOM_DATA["COMPLEX-ROOM"])
    
    print("=== ZIL Exit System Test ===\n")
    
    # Test all exit types
    directions_to_test = ["north", "northeast", "south", "east", "west", "up", "down", "invalid"]
    
    for direction in directions_to_test:
        can_go, destination, message = room.try_exit(direction, evaluator)
        
        print(f"Direction: {direction}")
        print(f"  Can go: {can_go}")
        print(f"  Destination: {destination}")
        print(f"  Message: {message}")
        
        # Identify exit type for demonstration
        exit_def = room.exits.get(direction)
        if exit_def:
            print(f"  Exit Type: {exit_def.exit_type.value}")
        print()
    
    print("=== Available Exits ===")
    available = room.get_available_exits(evaluator)
    for direction, destination in available.items():
        print(f"  {direction}: {destination}")
    
    print("\n=== Testing State Changes ===")
    
    # Close the door and test again
    print("Closing airlock door...")
    world_manager.objects["AIRLOCK-DOOR"].flags.remove("OPENBIT")
    can_go, destination, message = room.try_exit("up", evaluator)
    print(f"UP (door closed): can_go={can_go}, message='{message}'")
    
    # Enable secret flag
    print("Enabling secret flag...")
    world_manager.global_variables["SECRET-FLAG"] = True
    can_go, destination, message = room.try_exit("west", evaluator)
    print(f"WEST (flag enabled): can_go={can_go}, destination={destination}")


# Additional JSON examples for complex scenarios
ADVANCED_EXAMPLES = {
    "FOYER": {
        "name": "Foyer", 
        "description": "The entrance hall of the house.",
        "exits": {
            # Multiple door conditions
            "north": {
                "type": "door",
                "destination": "LIVING-ROOM",
                "door_object": "FRONT-DOOR"
            },
            # Conditional with time-based flag
            "east": {
                "type": "conditional",
                "destination": "DINING-ROOM", 
                "condition_var": "DINNER-TIME",
                "failure_message": "The dining room is not ready yet."
            }
        }
    },
    
    "BRIDGE": {
        "name": "Rickety Bridge",
        "description": "A dangerous looking bridge spans a chasm.",
        "exits": {
            "back": "CANYON-ENTRANCE",
            "across": {
                "type": "flexible",
                "routine_name": "cross_bridge_routine"  # Complex logic for bridge crossing
            },
            "down": {
                "type": "non_exit",
                "message": "The chasm is far too deep and dangerous!"
            }
        }
    }
}


if __name__ == "__main__":
    example_usage()