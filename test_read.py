from pyffi.formats.nif import *
import os
stream = open('snippets/initTextures.py','rb')

nameNoExt = os.path.basename(os.path.splitext(stream.name)[0])
print(stream.name.replace(nameNoExt,nameNoExt+'_blender'))
print(os.path.basename(stream.name))
