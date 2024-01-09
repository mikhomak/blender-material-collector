bl_info = {
    "name": "Material collector",
    "blender": (2, 80, 0),
    "description": "Assing all materials to a single object from the context menu",
    "version": (0, 0, 1),
    "category": "Object",
}

import bpy

class AssingAllMaterials(bpy.types.Operator):
    bl_idname = "object.assing_all_materials"
    bl_label = "Assing all materials"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        obj_data = context.active_object.data
        obj_data.materials.clear()
        for mat in context.blend_data.materials:
            if mat.name != 'Dots Stroke':
                obj_data.materials.append(mat)
        return {'FINISHED'}

class ClearAllMaterials(bpy.types.Operator):
    bl_idname = "object.clear_all_materials"
    bl_label = "Clear all materials"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        obj_data = context.active_object.data
        obj_data.materials.clear()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(AssingAllMaterials.bl_idname)
    self.layout.operator(ClearAllMaterials.bl_idname)

def register():
    bpy.utils.register_class(AssingAllMaterials)
    bpy.utils.register_class(ClearAllMaterials)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(AssingAllMaterials)
    bpy.utils.unregister_class(ClearAllMaterials)
