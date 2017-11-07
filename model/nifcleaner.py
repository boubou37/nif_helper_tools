from pyffi.formats.nif import *
import os


class NifConverter:
    def __init__(self):
        self.pathname = ''
        self.errorfile = ''
        self.files = []

    def convert_nif(self, path):
        stream = open(path, 'rb')
        data = NifFormat.Data()
        retcode = 0
        if self.pathname != '' and os.path.isdir(self.pathname):
            for astream, adata in NifFormat.walkData(self.pathname):
                retcode = self.__do_convert(astream,adata)
                if retcode > 0:
                    break
        elif self.files:
            print
        return retcode

    def __do_convert(self, stream, data):
        data.read(stream)
        for root in data.roots:
            for block in root.tree():
                if type(block) == NifFormat.NiTriShape:
                    if type(block.bs_properties[0]) == NifFormat.BSLightingShaderProperty:
                        block.bs_properties[0] = None
                    if block.bs_properties[1] is not None:
                        block.bs_properties[1] = None

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


if __name__ == '__main__':
    converter = NifConverter()
    for astream, adata in NifFormat.walkData('C:/Users/lrhmf/Desktop/3D/skyrim/character assets'):
        try:
            converter.__skyrim_to_blender(astream, adata)
        except Exception:
            print('error occurred during conversion')
