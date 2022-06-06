import importlib
import importlib.util
from types import ModuleType

def import_path(path: str, name=None) -> ModuleType | None:
    if name is None:
        name = path.split('/')[-1].removesuffix('.py')

    print(f'importing module {name} at {path}')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except FileNotFoundError:
        return None
    return mod


def import_global(name: str) -> ModuleType | None:

    print(f'importing global module {name}')
    try:
        return importlib.import_module(name)
    except ImportError:
        return None