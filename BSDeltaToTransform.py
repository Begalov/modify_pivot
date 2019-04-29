import bpy
import mathutils

objAxis = None
objTarget = None
rotAxis = None
locAxis = None
checkParams = ["BSAxis_"]

def main(context):
    
    if bpy.context.active_object != None:
        for obj in context.selected_objects:

            obj.location.x = obj.location.x +obj.delta_location.x
            obj.location.y = obj.location.y + obj.delta_location.y
            obj.location.z = obj.location.z + obj.delta_location.z

            obj.rotation_euler.x = obj.rotation_euler.x + obj.delta_rotation_euler.x
            obj.rotation_euler.y = obj.rotation_euler.y + obj.delta_rotation_euler.y
            obj.rotation_euler.z = obj.rotation_euler.z + obj.delta_rotation_euler.z

            obj.delta_rotation_euler.x = 0.0
            obj.delta_rotation_euler.y = 0.0
            obj.delta_rotation_euler.z = 0.0

            obj.delta_location.x = 0.0
            obj.delta_location.y = 0.0
            obj.delta_location.z = 0.0
            ##bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)


    """
    With this operator we reset pivot orientation and avoid disparities produced by delta values 
    """
    
class BSDeltaToTransform(bpy.types.Operator):
    bl_idname = "object.bsdelta_to_transform"
    bl_label = "BS Delta to transform"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(BSDeltaToTransform)
    
def unregister():
    bpy.utils.unregister_class(BSDeltaToTransform)