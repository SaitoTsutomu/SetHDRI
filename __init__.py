import webbrowser

import bpy

bl_info = {
    "name": "OpenURL",
    "author": "tsutomu",
    "version": (0, 1),
    "blender": (3, 1, 0),
    "support": "TESTING",
    "category": "Object",
    "description": "",
    "location": "View3D > Object",
    "warning": "",
    "doc_url": "https://github.com/SaitoTsutomu/OpenURL",
}


class COU_OT_open_url(bpy.types.Operator):
    bl_idname = "object.open_url"
    bl_label = "Open URL"
    bl_description = "Open the URL of a text object."

    def execute(self, context):
        obj = context.view_layer.objects.active
        if obj and obj.type == "FONT" and obj.data.body.startswith("http"):
            webbrowser.open(obj.data.body)
        return {"FINISHED"}


def draw_item(self, context):
    self.layout.operator(COU_OT_open_url.bl_idname)


def register():
    bpy.utils.register_class(COU_OT_open_url)
    bpy.types.VIEW3D_MT_object.append(draw_item)


def unregister():
    bpy.utils.unregister_class(COU_OT_open_url)
    bpy.types.VIEW3D_MT_object.remove(draw_item)


if __name__ == "__main__":
    register()
