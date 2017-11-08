from pyffi.formats.nif import *


# todo error handling
class NifCleaner:
    def __init__(self):
        self.pathname = ''
        self.data = NifFormat.Data()
        self.errorfile = ''
        self.files = []
        self.radioDirCheck = False
        self.radioFileCheck = False

    def clean_nif(self):
        raise NotImplementedError('this is an abstract method')