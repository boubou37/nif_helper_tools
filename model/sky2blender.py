from pyffi.formats.nif import *
import os
import model.nifcleaner as nc


class SkyToBlenderConverter(nc.NifCleaner):
    def clean_nif(self):
        return self.nif_to_blender()

    def __init__(self):
        super().__init__()

    def nif_to_blender(self):
        # lookup by folder name
        if self.pathname != '' and os.path.isdir(self.pathname):
            for astream, adata in NifFormat.walkData(self.pathname):
                retcode = self.__do_convert_nif_to_blender(astream, adata)
                if retcode > 0:
                    break
        # lookup by file names
        elif self.files:
            for file in self.files:
                stream = open(file,'rb')
                retcode = self.__do_convert_nif_to_blender(stream,self.data)

        return retcode

    def __do_convert_nif_to_blender(self, stream, data):
        data.inspect(stream)
        # we dont open fallout3/nv files as they are already blender compatible
        if data.header.user_version == 11 and data.header.user_version_2 == 34:
            return 0

        data.read(stream)
        for root in data.roots:
            # special handling of skeleton.nif
            # could not use list comprehension due to AttributeError and the fact we can't set the extra_data_list attr
            size = root.num_extra_data_list
            if size > 0:
                size = root.num_extra_data_list
                if size > 0:
                    index = 0
                    for i in range(size):
                        if type(root.extra_data_list[i]) == NifFormat.BSBoneLODExtraData:
                            index = i
                            break
                    root.extra_data_list[index] = None

            # removal of BSLightingShaderProperty nodes
            for block in root.tree():
                if type(block) == NifFormat.NiTriShape:
                    if type(block.bs_properties[0]) == NifFormat.BSLightingShaderProperty:
                        block.bs_properties[0] = None
                    if block.bs_properties[1] is not None:
                        block.bs_properties[1] = None

        # we append '_blender' to the file name
        namenoext = os.path.basename(os.path.splitext(stream.name)[0])
        stream = open(stream.name.replace(namenoext, namenoext + '_blender'), 'wb')

        data.user_version = 11
        data.user_version_2 = 34

        try:
            data.write(stream)
        except Exception:
            self.errorfile = stream.name
            return 1

        stream.close()
        return 0


