import os
from typing import List
from .utils import import_path


CONFIG_FOLDER = '~/.fastplugin'
CONFIG_FOLDER_EXP = os.path.expanduser(CONFIG_FOLDER)
CONFIG_FILE = 'config.py'
CONFIG_PATH = os.path.join(CONFIG_FOLDER_EXP, CONFIG_FILE)

PLUGIN_PATH = os.path.join(CONFIG_FOLDER_EXP, 'plugins')

IGNORED_NAMES = [
    '__pycache__'
]


class Config:
    PLUGINS_FOLDERS: List[str]
    PLUGINS: List[str]
    
    @staticmethod
    def load() -> 'Config':
        mod = import_path(CONFIG_PATH)
        if mod is None: 
            print(f'No config at {CONFIG_PATH}. Creating from template.')
            create_config()
            return Config.load()
        
        instance = Config()
        instance.PLUGINS_FOLDERS = mod.PLUGINS_FOLDERS
        instance.PLUGINS = getattr(mod, 'PLUGINS', None)
        return instance
    
    @staticmethod
    def _get_folders(path: str):
        return [os.path.join(path, name) for name in os.listdir(path) \
                if name not in IGNORED_NAMES]
    
    def get_paths_iter(self) -> list[str]:
        for folder in self.PLUGINS_FOLDERS:
            expanded = os.path.expanduser(folder)

            if not os.path.exists(expanded):
                raise FileNotFoundError(f'No such plugin path {expanded}')
            else:
                yield from self._get_folders(expanded)
    
    def get_paths(self) -> list[str]:
        return list(self.get_paths_iter())


CONFIG_TEMPLATE = \
f"""
PLUGINS_FOLDERS = [
    '{PLUGIN_PATH}',
]

PLUGINS = [

]

"""


def create_config():
    if os.path.exists(CONFIG_PATH):
        return
    
    os.makedirs(CONFIG_FOLDER_EXP, exist_ok=True)

    with open(CONFIG_PATH, 'w+') as f:
        f.write(CONFIG_TEMPLATE)

    os.makedirs(PLUGIN_PATH, exist_ok=True)