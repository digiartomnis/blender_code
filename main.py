import bpy
import bmesh
import os

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir)
# 清空默认场景
bpy.ops.wm.read_factory_settings(use_empty=True)

# 导入OBJ文件
obj_path = os.path.join(script_dir, "D:\\code\\blender_code\\bunny.obj")
bpy.ops.wm.obj_import(filepath=obj_path)

# 获取当前场景中的对象
obj = bpy.context.selected_objects[0]

# 创建bmesh对象
bm = bmesh.new()
bm.from_mesh(obj.data)

# 使用半边结构工具对网格进行平滑处理
bmesh.ops.smooth_vert(bm, verts=bm.verts, factor=0.5, use_axis_x=True, use_axis_y=True, use_axis_z=True)

# 将平滑后的bmesh对象应用回原始网格
bm.to_mesh(obj.data)
obj.data.update()

# 释放bmesh对象
bm.free()

# 设置视图端口着色为Material预览模式
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.type = 'MATERIAL'

# 保存blender文件
blend_path = os.path.join(script_dir, "./smoothed_bunny.blend")
bpy.ops.wm.save_mainfile(filepath=blend_path)