import bpy

traslation_dict = {
    "ja_JP" : {
    }
}

def register(name):
    bpy.app.translations.unregister(name)
    bpy.app.translations.register(name, traslation_dict)

def unregister(name):
    bpy.app.translations.unregister(name)
    