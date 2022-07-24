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


def set_3dview_shading(shading_type):
    for area in bpy.context.screen.areas:
        if area.type == "VIEW_3D":
            for space in area.spaces:
                if space.type == "VIEW_3D":
                    space.shading.type = shading_type


class CSH_OT_set_hdri(bpy.types.Operator):
    bl_idname = "object.set_hdri"
    bl_label = "Set HDRI"
    bl_description = "Set the world image."

    filepath: bpy.props.StringProperty()  # type: ignore # noqa

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}

    def execute(self, context):
        bpy.context.scene.world.use_nodes = True
        nt = bpy.context.scene.world.node_tree
        et = nt.nodes.get("Environment Texture")
        if not et:
            et = nt.nodes.new("ShaderNodeTexEnvironment")
            nt.links.new(et.outputs[0], nt.nodes["Background"].inputs[0])
        et.image = bpy.data.images.load(filepath=self.filepath)
        set_3dview_shading("RENDERED")
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
