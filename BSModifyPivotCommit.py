import bpy
import mathutils

objAxis = None
objTarget = None
rotAxis = None
locAxis = None
checkParams = ["BSAxis_"]

def main(context):
    
    if bpy.context.active_object != None:
        if any(x in bpy.context.active_object.name for x in checkParams):
            objAxis = bpy.context.active_object
            objName = objAxis.name
            objName = objName.replace("BSAxis_","")
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = None
            bpy.data.objects[objName].select_set(state=True)
            bpy.context.view_layer.objects.active = bpy.data.objects[objName]
            objTarget= bpy.context.active_object

            objTarget.location = objTarget.location + objTarget.delta_location
            objTarget.delta_location = (0.0, 0.0, 0.0)

            xRot = objTarget.rotation_euler.x
            xDRot = objTarget.delta_rotation_euler.x
            yRot = objTarget.rotation_euler.y
            yDRot = objTarget.delta_rotation_euler.y
            zRot = objTarget.rotation_euler.z
            zDRot = objTarget.delta_rotation_euler.z

            objTarget.rotation_euler.x = xRot + xDRot
            objTarget.rotation_euler.y = yRot + yDRot
            objTarget.rotation_euler.z = zRot + zDRot
            objTarget.delta_rotation_euler.x = 0.0
            objTarget.delta_rotation_euler.y = 0.0
            objTarget.delta_rotation_euler.z = 0.0

            newRot = objAxis.rotation_euler
            newRotMX = newRot.to_matrix()
            newRotInvMX = newRotMX.inverted()
            newRotDupMX = newRotMX @ newRotMX
            newRotDupInvMX = newRotDupMX.inverted()

            newRotMXEu = newRotMX.to_euler()
            #newRotInvMXEu = newRotInvMX.to_euler()
            #newRotDupMXEu = newRotDupMX.to_euler()
            newRotDupInvMXEu = newRotDupInvMX.to_euler()
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            
            #previousLoc = objTarget.location + objTarget.delta_location
            currentCursorLocation = bpy.context.scene.cursor.location
            bpy.context.scene.cursor.location = objAxis.location
            objTarget.location = objTarget.location + objTarget.delta_location
            objTarget.delta_location = (0.0, 0.0, 0.0)
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            #bpy.context.scene.cursor_location = currentCursorLocation

            objTarget.delta_rotation_euler = newRotMXEu
            objTarget.rotation_euler = newRotDupInvMXEu    
            
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
            objTarget.delta_location = objTarget.location
            objTarget.location = (0.0,0.0,0.0)
            bpy.ops.object.select_all(action='DESELECT')
            objAxis.select_set(state=True)
            bpy.ops.object.delete()
            objTarget.select_set(state=True)

"""
With this operator we commit the object pivot to the axis pivot and we delete the axis from the scene 
"""
class BSModifyPivot_OT_Commit(bpy.types.Operator):
    """Commit modified pivot"""
    bl_idname = "object.bsmodify_pivot_commit"
    bl_label = "BS Modify Object Pivot Commit"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {"FINISHED"}

def register():
    bpy.utils.register_class(BSModifyPivot_OT_Commit)
    
def unregister():
    bpy.utils.unregister_class(BSModifyPivot_OT_Commit)