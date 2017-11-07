import bpy
import Blender
from Blender import Material,Texture,Image
i = 0
for mesh in bpy.data.meshes:
	if not mesh.materials:
		i+=1
		print(mesh.materials)
		texture = Texture.New('Yoo0')
		texture.setType('Image')
		material = Material.New('mat'+str(i))
		material.setTexture(0,texture,Texture.TexCo.UV)
		mesh.materials += [material]
		print(mesh.materials[0].getTextures())
#	mesh.materials = []
#	if mesh.materials:
#		print(mesh.materials[0].getTextures()[0].tex)