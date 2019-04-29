import bpy
from bpy.types import Menu, Panel, UIList


class BSModifyPivotPanel(bpy.types.Panel):
    bl_label = "Modify Pivot"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
    bl_category = "Tools"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        layout.operator("object.bsmodify_pivot_create", text="Modify Pivot", icon="OUTLINER_DATA_EMPTY")
        layout.operator("object.bsmodify_pivot_commit", text="Commit Pivot", icon="OUTLINER_OB_EMPTY")
        layout.operator("object.bsmodify_pivot_reset_orientation", text="Reset Pivot Orientation", icon="FILE_REFRESH")
        layout.operator("object.bsmodify_reset_zero_location", text="Reset Zero Location", icon="FILE_REFRESH")
        layout.operator("object.bsdelta_to_transform", text="Delta To Transform", icon="FILE_REFRESH")

def register():
    bpy.utils.register_class(BSModifyPivotPanel)


def unregister():
    bpy.utils.unregister_class(BSModifyPivotPanel)

"""
if __name__ == "__main__":
    register()
    
    print ("GUI Loaded")
"""