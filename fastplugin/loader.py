from collections import defaultdict
from dataclasses import dataclass
import os
import importlib
import importlib.util
from types import ModuleType
from typing import List
import PySimpleGUI as sg


PLUGINS = {

}

PLUGIN_COMMANDS = defaultdict(list)


PLUGIN_UI = []

UI = [
    [
        sg.Frame(
            'Plugins', 
            [ 
                [
                    sg.Text('Main plugin ui'),
                ]
            ]
        )
    ],
    PLUGIN_UI
]


def get_names() -> List[str]:
    names = os.listdir('plugins')
    names = filter(lambda f: not f.startswith('_'), names)
    return list(names)


def import_plugin(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def load_plugin(path, name):
    mod = import_plugin(path, name)
    name = mod.NAME
    commands = mod.COMMANDS
    ui = mod.UI
    mod.init()

    scan_module(mod)

    return ui, name, commands

def scan_module(mod: ModuleType):
    for name, attr in mod.__dict__.items():
        if not getattr(attr, 'is_command', None):
            continue
        for event_name in attr.activate_on:
            PLUGIN_COMMANDS[event_name] = attr
            

def load_plugins(names: List[str]):
    for name in names:
        ui, n, commands = load_plugin(os.path.join('plugins', name), name.replace('.py', ''))
        PLUGINS[n] = commands
        append_ui(ui, n)

def append_ui(ui: List, name: str):
    frame = sg.Frame(name, ui)
    UI.append(frame)


def main():
    names = get_names()
    load_plugins(names)

if __name__ == '__main__':
    main()
    print(PLUGIN_COMMANDS)