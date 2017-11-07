from pyffi.formats.nif import *
root = NifFormat.NiNode()
cld = NifFormat.NiNode()
nts = NifFormat.NiTriShape()
bsl = NifFormat.BSLightingShaderProperty()
nts.bs_properties[0] = bsl
root.add_child(cld)
root.add_child(nts)
stream = open('test2.nif','wb')
nifdata = NifFormat.Data(version=0x14010003, user_version=10)
nifdata.header.user_version = 13
nifdata.roots = [root]
print(nifdata.header.user_version )
nifdata.write(stream)
print(nifdata.header.user_version )
stream.close()