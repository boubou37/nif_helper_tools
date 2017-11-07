from pyffi.formats.nif import *
import os
stream = open('skeleton.nif','rb')
data = NifFormat.Data()
data.read(stream)
for root in data.roots:
    print(root.extra_data_list)
