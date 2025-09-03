from typing import Dict, Any, Optional, Union, Callable
from dataclasses import dataclass
from enum import Enum
import json


class ConditionType(Enum):
    """Types of conditions that can be evaluated"""
    FLAG_CHECK = "flag_check"
    PROPERTY_CHECK = "property_check" 
    OBJECT_LOCATION = "object_location"
    CALLABLE = "callable"
    AND = "and"
    OR = "or"
    NOT = "not"


@dataclass
class ExitCondition:
    """Represents a conditional exit requirement"""
    type: ConditionType
    object_id: Optional[str] = None
    flag: Optional[str] = None
    property_name: Optional[str] = None
    value: Any = None
    conditions: Optional[list] = None  # For AND/OR/NOT operations
    callable_name: Optional[str] = None


class ConditionalEvaluator:
    """Evaluates conditional expressions against game state"""
    
    def __init__(self, world_manager):
        self.world_manager = world_manager
        
    def evaluate(self, condition: Union[ExitCondition, Dict[str, Any]]) -> bool:
        """Evaluate a condition and return True/False"""
        
        # Handle dict format from JSON
        if isinstance(condition, dict):
            condition = self._dict_to_condition(condition)
            
        if condition.type == ConditionType.FLAG_CHECK:
            return self._check_flag(condition)
        elif condition.type == ConditionType.PROPERTY_CHECK:
            return self._check_property(condition)
        elif condition.type == ConditionType.OBJECT_LOCATION:
            return self._check_location(condition)
        elif condition.type == ConditionType.CALLABLE:
            return self._call_function(condition)
        elif condition.type == ConditionType.AND:
            return all(self.evaluate(c) for c in condition.conditions)
        elif condition.type == ConditionType.OR:
            return any(self.evaluate(c) for c in condition.conditions)
        elif condition.type == ConditionType.NOT:
            return not self.evaluate(condition.conditions[0])
        
        return False
    
    def _dict_to_condition(self, data: Dict[str, Any]) -> ExitCondition:
        """Convert dictionary to ExitCondition object"""
        return ExitCondition(
            type=ConditionType(data["type"]),
            object_id=data.get("object"),
            flag=data.get("flag"),
            property_name=data.get("property"),
            value=data.get("value"),
            conditions=data.get("conditions"),
            callable_name=data.get("callable")
        )
    
    def _check_flag(self, condition: ExitCondition) -> bool:
        """Check if an object has a specific flag set"""
        obj = self.world_manager.get_object(condition.object_id)
        if not obj:
            return False
        return obj.has_flag(condition.flag) == condition.value
    
    def _check_property(self, condition: ExitCondition) -> bool:
        """Check if an object property matches a value"""
        obj = self.world_manager.get_object(condition.object_id)
        if not obj:
            return False
        return obj.get_property(condition.property_name) == condition.value
    
    def _check_location(self, condition: ExitCondition) -> bool:
        """Check if an object is in a specific location"""
        obj = self.world_manager.get_object(condition.object_id)
        if not obj:
            return False
        return obj.location == condition.value
    
    def _call_function(self, condition: ExitCondition) -> bool:
        """Call a custom function for complex conditions"""
        func = getattr(self.world_manager, condition.callable_name, None)
        if func and callable(func):
            return func()
        return False


class Exit:
    """Represents a room exit with optional conditions"""
    
    def __init__(self, destination: str, condition: Optional[Union[Dict, ExitCondition]] = None, 
                 failure_message: str = "You can't go that way."):
        self.destination = destination
        self.condition = condition
        self.failure_message = failure_message
    
    def is_available(self, evaluator: ConditionalEvaluator) -> bool:
        """Check if this exit is currently available"""
        if not self.condition:
            return True
        return evaluator.evaluate(self.condition)
    
    def get_destination(self, evaluator: ConditionalEvaluator) -> Optional[str]:
        """Get destination if exit is available, None otherwise"""
        return self.destination if self.is_available(evaluator) else None


class Room:
    """Room class with conditional exits"""
    
    def __init__(self, room_id: str, data: Dict[str, Any]):
        self.id = room_id
        self.name = data["name"]
        self.description = data["description"]
        self.exits = self._load_exits(data.get("exits", {}))
        self.navigation = data.get("navigation", {})
        
    def _load_exits(self, exits_data: Dict[str, Any]) -> Dict[str, Exit]:
        """Load exits from JSON data"""
        exits = {}
        
        for direction, exit_info in exits_data.items():
            if isinstance(exit_info, str):
                # Simple exit: "north": "OTHER-ROOM"
                exits[direction] = Exit(destination=exit_info)
            elif isinstance(exit_info, dict):
                # Conditional exit with full specification
                exits[direction] = Exit(
                    destination=exit_info["destination"],
                    condition=exit_info.get("condition"),
                    failure_message=exit_info.get("failure_message", "You can't go that way.")
                )
                
        return exits
    
    def get_exit(self, direction: str, evaluator: ConditionalEvaluator) -> Optional[str]:
        """Get destination for a direction, checking conditions"""
        exit_obj = self.exits.get(direction.lower())
        if not exit_obj:
            return None
        return exit_obj.get_destination(evaluator)
    
    def get_available_exits(self, evaluator: ConditionalEvaluator) -> Dict[str, str]:
        """Get all currently available exits"""
        available = {}
        for direction, exit_obj in self.exits.items():
            destination = exit_obj.get_destination(evaluator)
            if destination:
                available[direction] = destination
        return available


# Example usage and testing
def example_usage():
    """Demonstrate the conditional exit system"""
    
    # Mock world manager for testing
    class MockWorldManager:
        def __init__(self):
            self.objects = {
                "FRONT-DOOR": MockGameObject("FRONT-DOOR", flags={"OPENBIT"})
            }
        
        def get_object(self, obj_id):
            return self.objects.get(obj_id)
    
    class MockGameObject:
        def __init__(self, obj_id, flags=None, properties=None):
            self.id = obj_id
            self.flags = flags or set()
            self.properties = properties or {}
            self.location = None
            
        def has_flag(self, flag):
            return flag in self.flags
            
        def get_property(self, prop):
            return self.properties.get(prop)
    
    # Create world manager and evaluator
    world_manager = MockWorldManager()
    evaluator = ConditionalEvaluator(world_manager)
    
    # Test room data
    room_data = {
        "name": "Front Path",
        "description": "You are on the front path of the house.",
        "exits": {
            "in": {
                "destination": "FOYER",
                "condition": {
                    "type": "flag_check",
                    "object": "FRONT-DOOR",
                    "flag": "OPENBIT", 
                    "value": True
                },
                "failure_message": "The front door is closed."
            },
            "north": {
                "destination": "FOYER",
                "condition": {
                    "type": "flag_check",
                    "object": "FRONT-DOOR",
                    "flag": "OPENBIT",
                    "value": True
                }
            },
            "south": "SOUTH-LAWN"
        }
    }
    
    # Create room
    room = Room("FRONT-PATH", room_data)
    
    # Test exits
    print("Available exits:")
    available = room.get_available_exits(evaluator)
    for direction, destination in available.items():
        print(f"  {direction}: {destination}")
    
    # Test specific exit
    can_go_in = room.get_exit("in", evaluator)
    print(f"\nCan go 'in': {can_go_in}")
    
    # Close the door and test again
    world_manager.objects["FRONT-DOOR"].flags.remove("OPENBIT")
    can_go_in = room.get_exit("in", evaluator)
    print(f"Can go 'in' (door closed): {can_go_in}")


# More complex condition examples for JSON
COMPLEX_CONDITIONS_EXAMPLES = {
    "multiple_conditions": {
        "destination": "SECRET-ROOM",
        "condition": {
            "type": "and",
            "conditions": [
                {
                    "type": "flag_check",
                    "object": "HIDDEN-DOOR",
                    "flag": "OPENBIT",
                    "value": True
                },
                {
                    "type": "property_check", 
                    "object": "PLAYER",
                    "property": "has_key",
                    "value": True
                }
            ]
        }
    },
    "time_based": {
        "destination": "GARDEN",
        "condition": {
            "type": "callable",
            "callable": "is_daytime"
        }
    },
    "complex_logic": {
        "destination": "VAULT",
        "condition": {
            "type": "or",
            "conditions": [
                {
                    "type": "flag_check",
                    "object": "VAULT-DOOR",
                    "flag": "OPENBIT", 
                    "value": True
                },
                {
                    "type": "and",
                    "conditions": [
                        {
                            "type": "object_location",
                            "object": "CROWBAR",
                            "value": "PLAYER"
                        },
                        {
                            "type": "callable",
                            "callable": "player_is_strong_enough"
                        }
                    ]
                }
            ]
        }
    }
}


if __name__ == "__main__":
    example_usage()