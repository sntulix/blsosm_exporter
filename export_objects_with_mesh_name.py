import os
from math import *
import bpy

#save_dir = "c:\\users\\username\\OneDrive\\3D\\blender\\script\\blsosm_exporter\\models\\"
save_dir = "/Users/takahiro/Downloads/blender/assets/blsosm_exporter/"
infofile_path = save_dir+"modellist.tsv"

def export_active_object2glb(save_dir, infofile_path, obj):
	obj.select_set(True)
	save_filename = obj.name+".glb"
	save_path = save_dir + save_filename
	print(save_filename)
	rot = obj.rotation_euler
	f = open(infofile_path, "a")
	f.write(obj.name + "\t"
		+ str(obj.location[0]) + "\t" + str(obj.location[1]) + "\t" + str(obj.location[2]) + "\t"
		+ str(degrees(rot[0])) + "\t" + str(degrees(rot[1])) + "\t" + str(degrees(rot[2])) + "\t"
		+ str(obj.scale[0]) + "\t" + str(obj.scale[1]) + "\t" + str(obj.scale[2]) + "\t"
		+ str(obj.dimensions[0]) + "\t" + str(obj.dimensions[1]) + "\t" + str(obj.dimensions[2])
		+"\n"
	)
	f.close()
	tmp_loc = obj.location[::]
	obj.location[0] = 0
	obj.location[1] = 0
	obj.location[2] = 0
	bpy.ops.export_scene.gltf(filepath=save_path, export_current_frame=True, export_format='GLTF_EMBEDDED', export_image_format='JPEG', export_jpeg_quality=80, use_selection=True)
	obj.location = tmp_loc

if os.path.exists(infofile_path):
	os.remove(infofile_path)

for o in bpy.context.scene.objects:
	if o.type == 'MESH':
		bpy.ops.object.select_all(action='DESELECT')
		export_active_object2glb(save_dir, infofile_path, o)