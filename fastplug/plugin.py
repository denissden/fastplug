from typing import Callable, List
from PySimpleGUI import Element

COMMANDS = {}

def _add_command(f: Callable, event_name: str):
    COMMANDS[event_name] = f

def command(name: str, activate_on: List[str] = None):
    def decorator(f: Callable):
        f.is_command = True
        f.command = name
        f.activate_on = activate_on if activate_on is not None else [name]
        _add_command(f, name)
        return f
    return decorator

def reg(element: Element):
    def decorator(f: Callable):
        print("Key", element.Key)
        _add_command(f, element.Key)
        return f
    # enable events
    element.ChangeSubmits = True
    return decorator