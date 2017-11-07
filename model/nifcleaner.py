from pyffi.formats.nif import *


# todo error handling
class NifCleaner:
    def __init__(self):
        self.pathname = ''
        self.data = NifFormat.Data()
        self.errorfile = ''
        self.files = []

    def convert(self):
        raise NotImplementedError('this is an abstract method')