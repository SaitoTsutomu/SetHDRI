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


class COU_OT_add_url(bpy.types.Operator):
    bl_idname = "object.add_url"
    bl_label = "Add URL"
    bl_description = "Add the a text object of URL."

    def execute(self, context):
        s = bpy.context.window_manager.clipboard
        if not (isinstance(s, str) and s.startswith("http")):
            self.report({"WARNING"}, "Copy URL")
            return {"CANCELLED"}
        bpy.ops.object.text_add(radius=0.1)
        text = bpy.context.object
        text.data.body = s
        text.name = "URL"
        text.hide_render = True
        return {"FINISHED"}


ui_classes = (
    COU_OT_open_url,
    COU_OT_add_url,
)


def draw_item(self, context):
    self.layout.operator(COU_OT_open_url.bl_idname)
    self.layout.operator(COU_OT_add_url.bl_idname)


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
