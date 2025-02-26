import bpy
from bpy.types.Panel import Panel

class SyuutaTools_PT_main(Panel):
    bl_label = "Change Vertex Group Name"
    bl_idname = "SyuutaTools_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Syuuta Tools'

    def draw(self, context):
        wm = context.scene.SyuutaTools
        layout = self.layout

        layout.prop(wm, "csv_file_path")
        layout.prop(wm, "set_mode")
        layout.separator()
        layout.prop(wm, "avatar_from")
        layout.prop(wm, "avatar_to")
        layout.operator("object.change_vertex_group_name")

classes = [
    SyuutaTools_PT_main,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

