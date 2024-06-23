import bpy
import sys
import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.realpath(__file__))

# 添加插件脚本所在目录到Python路径
sys.path.append(current_dir)

# 导入插件模块
import mesh_processing_tools

# 注册插件
mesh_processing_tools.register()

# 确保场景中有一个立方体（如果没有，创建一个）
if 'Cube' not in bpy.data.objects:
    bpy.ops.mesh.primitive_cube_add()

# 选择立方体
cube = bpy.data.objects['Cube']
bpy.context.view_layer.objects.active = cube
cube.select_set(True)

# 执行三角化
bpy.ops.mesh.custom_triangulate()

# 设置细分级别为1并执行细分
bpy.context.scene.subdivision_levels = 1
bpy.ops.mesh.custom_subdivide()

# 打印最终面数
final_face_count = len(cube.data.polygons)
print(f"最终面数: {final_face_count}")

# 保存为Blender文件
output_file = os.path.join(current_dir, "result.blend")
bpy.ops.wm.save_as_mainfile(filepath=output_file)
print(f"结果已保存到: {output_file}")

# 取消注册插件（可选，但是好习惯）
mesh_processing_tools.unregister()