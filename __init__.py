import webbrowser

import bpy

bl_info = {
    "name": "SetHDRI",
    "author": "tsutomu",
    "version": (0, 1),
    "blender": (3, 1, 0),
    "support": "TESTING",
    "category": "Object",
    "description": "",
    "location": "View3D > Object",
    "warning": "",
    "doc_url": "https://github.com/SaitoTsutomu/SetHDRI",
}


class CSH_OT_set_hdri(bpy.types.Operator):
    bl_idname = "object.set_hdri"
    bl_label = "Set HDRI"
    bl_description = "Set the world image."

    def execute(self, context):
        return {"FINISHED"}


ui_classes = (CSH_OT_set_hdri,)


def draw_item(self, context):
    for ui_class in ui_classes:
        self.layout.operator(ui_class.bl_idname)


def register():
    for ui_class in ui_classes:
        bpy.utils.register_class(ui_class)
    bpy.types.VIEW3D_MT_object.append(draw_item)


def unregister():
    for ui_class in ui_classes:
        bpy.utils.unregister_class(ui_class)
    bpy.types.VIEW3D_MT_object.remove(draw_item)


if __name__ == "__main__":
    register()
