import bpy
import mathutils


objAxis = None
objTarget = None
checkParams = ["BSAxis_"]

def main(context):
    
    if bpy.context.active_object != None:
        if any(x in bpy.context.active_object.name for x in checkParams):
            print("Active object cannot be a BSAxis Object") 
        else:
            objTarget = bpy.context.active_object
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern="BSAxis_*")
            bpy.ops.object.delete()
            objTarget.select = True
            bpy.ops.object.empty_add(type='ARROWS')
            objAxis= bpy.context.active_object
            objAxis.location = objTarget.location + objTarget.delta_location
            objAxis.show_x_ray = True
            euRotationMX = objTarget.rotation_euler.to_matrix()
            euRotationDeltaMX = objTarget.delta_rotation_euler.to_matrix()
            RotationFullMX = euRotationMX * euRotationDeltaMX
            euRotationFull = RotationFullMX.to_euler()
            objAxis.rotation_euler = euRotationFull
            objAxis.name = "BSAxis_"+objTarget.name
            bpy.ops.object.select_all(action='DESELECT')
            objAxis.select = True
            bpy.context.scene.objects.active = objAxis
            #objAxis.select = True


    """
    With this operator we create an axis object wich we will use to define the new object pivot 
    """

class BSModifyPivotCreate(bpy.types.Operator):
    bl_idname = "object.bsmodify_pivot_create"
    bl_label = "BS Modify Object Pivot Create"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(BSModifyPivotCreate)
    
def unregister():
    bpy.utils.unregister_class(BSModifyPivotCreate)
