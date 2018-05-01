import os

__all__ = []
for module in os.listdir(os.path.dirname(__file__)):
    if module[-8:] == '_test.py' and module != '__init__.py':
        __all__.append(module[0:-3])

from . import *
