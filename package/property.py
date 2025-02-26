import bpy
from bpy.props import StringProperty, PointerProperty, EnumProperty
import csv
from pathlib import Path

avater_name_list = []
csv_data =[]

def get_avaterlist_callback(self, context):
    global avater_name_list
    avater_name_list = []
    if context.scene.SyuutaTools.csv_file_path == "":
        return avater_name_list
    
    data = load_csv(context.scene.SyuutaTools.csv_file_path)

    for i in range(len(data)):
        if i == 0:
            continue
        avater_name_list.append((str(i), str(data[i][0]), ""))
    
    return avater_name_list

# 読み込んだCSVから Avatar From と Avatar To を 1行目のデータをもとにリストを作成する
def load_csv(csv_file_path):
    global csv_data
    if Path(csv_file_path).is_absolute() == False:
        csv_file_path = bpy.path.abspath(csv_file_path)
        print(csv_file_path)

    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    csv_data = data
    return data

# プロパティの追加  
class SyuutaToolsProperties(bpy.types.PropertyGroup):
    csv_file_path: StringProperty(
        name="CSV File",
        description="Select the CSV file",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    ) # type: ignore
    set_mode: EnumProperty(
        name="Set Mode",
        description="Select set mode",
        items=[
            ('0', 'Vertex Groups', ''),
            ('1', 'Bone', ''),
        ],
    ) # type: ignore
    avatar_from: EnumProperty(
        name="Avatar From",
        description="Choose the type of avatar",
        items=get_avaterlist_callback,
    ) # type: ignore
    avatar_to: EnumProperty(
        name="Avatar To",
        description="Choose the type of avatar",
        items=get_avaterlist_callback,
    ) # type: ignore


classes = [
    SyuutaToolsProperties,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.SyuutaTools = PointerProperty(type=SyuutaToolsProperties)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.SyuutaTools