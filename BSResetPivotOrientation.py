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
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            obj.delta_rotation_euler.x = 0.0
            obj.delta_rotation_euler.y = 0.0
            obj.delta_rotation_euler.z = 0.0

    """
    With this operator we reset pivot orientation and avoid disparities produced by delta values 
    """
    
class BSResetPivotOrientation(bpy.types.Operator):
    bl_idname = "object.bsmodify_pivot_reset_orientation"
    bl_label = "BS Modify Reset Pivot Orientation"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(BSResetPivotOrientation)
    
def unregister():
    bpy.utils.unregister_class(BSResetPivotOrientation)