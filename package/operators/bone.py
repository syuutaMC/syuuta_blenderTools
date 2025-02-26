import bpy

# アバターの頂点グループの差分を作成し、辞書を作成する
def compare_list(before, after):
    dict = {}
    for i in range(len(before)):
        if before[i] != after[i]:
            if before[i] != "":
                dict[before[i]] = after[i]
    return dict

# 頂点グループ名を変更する
def mark_old_vertex_groups(data, obj):
    for i in obj.vertex_groups:
        if i.name in data:
            if data[i.name] != "":
                i.name = i.name + "_old"

def rename_vertex_groups(data, obj):
    # print("rename_vertex_groups")
    for v in obj.vertex_groups:
        clean_name = v.name.replace("_old", "")
        if v.name in data or clean_name in data:
            key = v.name if v.name in data else clean_name
            # print(v.name)
            if data[key] != "":
                v.name = data[key]
            else:
                # print(obj.vertex_groups.items())
                obj.vertex_groups.remove(v)

def change_vertex_groups_name(data, objs):
    for obj in objs:
        if obj.type == "MESH":
            # print("before mark_old_bones")
            # print(obj.vertex_groups.items())
            mark_old_vertex_groups(data, obj)
            # print("after mark_old_bones")
            # print(obj.vertex_groups.items())
            rename_vertex_groups(data, obj)

# ボーン名を変更する
def mark_old_bones(data, obj):
    for i in obj.data.bones:
        if i.name in data:
            if data[i.name] != "":
                i.name = i.name + "_old"

def rename_bones(data, obj):
    for b in obj.data.bones:
        clean_name = b.name.replace("_old", "")
        if b.name in data or clean_name in data:
            key = b.name if b.name in data else clean_name
            if data[key] != "":
                b.name = data[key]
            else:
                obj.data.bones.remove(b)

def change_bones_name(data, objs):
    for obj in objs:
        if obj.type == "ARMATURE":
            mark_old_bones(data, obj)
            rename_bones(data, obj)


class OBJECT_OT_change_vertex_group_name(bpy.types.Operator):
    bl_idname = "object.change_vertex_group_name"
    bl_label = "Change Vertex Group Name"
    bl_description = "Change Vertex Group Name"

    global csv_data
    def execute(self, context):
        global csv_data
        avater_from = csv_data[int(context.scene.SyuutaTools.avatar_from)]
        avater_to = csv_data[int(context.scene.SyuutaTools.avatar_to)]
        data = compare_list(avater_from, avater_to)
        objs = bpy.context.selected_objects

        match(int(context.scene.SyuutaTools.set_mode)):
            case 0:
                change_vertex_groups_name(data, objs)
            case 1:
                change_bones_name(data, objs)

        return {'FINISHED'}
    
classes = [
    OBJECT_OT_change_vertex_group_name,
]
    

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)