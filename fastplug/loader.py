from collections import defaultdict
from dataclasses import dataclass
import os
import importlib
import importlib.util
from types import ModuleType
from typing import List
import PySimpleGUI as sg
from .utils import import_path

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
    ]
]


def get_names() -> List[str]:
    names = os.listdir('plugins')
    names = filter(lambda f: not f.startswith('_'), names)
    return list(names)

def load_plugin(path):
    mod = import_path(path)
    name = mod.NAME
    ui = mod.UI
    mod.init()

    return ui, name

def load_plugins(paths: List[str]):
    for path in paths:
        ui, name = load_plugin(path)
        append_ui(ui, name)

def append_ui(ui: List, name: str):
    frame = sg.Frame(name, ui)
    UI.append(frame)
