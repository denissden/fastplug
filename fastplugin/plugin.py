from typing import Callable, List

COMMANDS = {}

def command(name: str, activate_on: List[str] = None):
    def decorator(f: Callable):
        f.is_command = True
        f.command = name
        f.activate_on = activate_on if activate_on is not None else [name]
        COMMANDS[name] = f
        return f
    return decorator