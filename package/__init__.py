from . import property
from . import translation

from .operators import bone

from .ui import ui_main

bl_info = {
    "name": "Syuuta Blender Tools",
    "author": "Syuuta",
    "blender": (2, 80, 0),
    "version": (0, 1, 1),
    "description": "syuuta test",
    "support": "TESTING",
    "category": "Object"
}

modules = [
    ui_main,
    bone,
    property
]

def register():
    translation.register(__name__)
    for module in modules:
        module.register()

def unregister():
    for module in modules:
        module.unregister()
    translation.register(__name__)

if __name__ == "__main__":
    register()