bl_info = {
    "name": "网格处理工具",
    "author": "Your Name",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Tool Tab",
    "description": "三角化和细分网格",
    "category": "Mesh",
}

import bpy
import bmesh

class MESH_OT_triangulate(bpy.types.Operator):
    bl_idname = "mesh.custom_triangulate"
    bl_label = "三角化"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj and obj.type == 'MESH':
            bm = bmesh.new()
            bm.from_mesh(obj.data)
            bmesh.ops.triangulate(bm, faces=bm.faces[:])
            bm.to_mesh(obj.data)
            bm.free()
            obj.data.update()
            self.report({'INFO'}, "物体已成功三角化")
        else:
            self.report({'ERROR'}, "请选择一个网格物体")
        return {'FINISHED'}

class MESH_OT_subdivide(bpy.types.Operator):
    bl_idname = "mesh.custom_subdivide"
    bl_label = "Catmull-Clark细分"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj and obj.type == 'MESH':
            levels = context.scene.subdivision_levels
            modifier = obj.modifiers.new(name="Subdivision", type='SUBSURF')
            modifier.levels = levels
            modifier.render_levels = levels
            modifier.subdivision_type = 'CATMULL_CLARK'
            bpy.ops.object.modifier_apply(modifier="Subdivision")
            self.report({'INFO'}, f"已应用{levels}级Catmull-Clark细分")
        else:
            self.report({'ERROR'}, "请选择一个网格物体")
        return {'FINISHED'}

class VIEW3D_PT_mesh_tools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_label = "ustc网格处理工具"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.operator("mesh.custom_triangulate")
        
        layout.prop(scene, "subdivision_levels", slider=True)
        layout.operator("mesh.custom_subdivide")

def register():
    bpy.utils.register_class(MESH_OT_triangulate)
    bpy.utils.register_class(MESH_OT_subdivide)
    bpy.utils.register_class(VIEW3D_PT_mesh_tools)
    bpy.types.Scene.subdivision_levels = bpy.props.IntProperty(
        name="细分级别",
        default=1,
        min=1,
        max=6,
        description="设置Catmull-Clark细分的级别"
    )

def unregister():
    bpy.utils.unregister_class(MESH_OT_triangulate)
    bpy.utils.unregister_class(MESH_OT_subdivide)
    bpy.utils.unregister_class(VIEW3D_PT_mesh_tools)
    del bpy.types.Scene.subdivision_levels

if __name__ == "__main__":
    register()