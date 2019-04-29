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

            obj.delta_location.x = 0.0
            obj.delta_location.y = 0.0
            obj.delta_location.z = 0.0
            bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)


    """
    With this operator we reset pivot orientation and avoid disparities produced by delta values 
    """
    
class BSResetZeroLocation(bpy.types.Operator):
    bl_idname = "object.bsmodify_reset_zero_location"
    bl_label = "BS Modify Reset Zero Location"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(BSResetZeroLocation)
    
def unregister():
    bpy.utils.unregister_class(BSResetZeroLocation)