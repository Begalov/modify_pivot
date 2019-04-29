import bpy
from bpy.types import Menu, Panel, UIList


class BSModifyPivot_PT_Panel(bpy.types.Panel):
    bl_category = "Tools"
    bl_context = "objectmode"
    bl_label = "Modify Pivot"
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        layout.operator("object.bsmodify_pivot_create", text="Modify Pivot", icon="OUTLINER_DATA_EMPTY")
        layout.operator("object.bsmodify_pivot_commit", text="Commit Pivot", icon="OUTLINER_OB_EMPTY")
        layout.operator("object.bsmodify_pivot_reset_orientation", text="Reset Pivot Orientation", icon="FILE_REFRESH")
        layout.operator("object.bsmodify_reset_zero_location", text="Reset Zero Location", icon="FILE_REFRESH")
        layout.operator("object.bsdelta_to_transform", text="Delta To Transform", icon="FILE_REFRESH")

def register():
    bpy.utils.register_class(BSModifyPivot_PT_Panel)


def unregister():
    bpy.utils.unregister_class(BSModifyPivot_PT_Panel)