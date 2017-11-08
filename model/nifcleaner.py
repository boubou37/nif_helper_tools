from pyffi.formats.nif import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox


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
        if self.clean_check():
            return self.__do_clean_nif()
        else:
            return 1

    def __do_clean_nif(self):
        # lookup by folder name
        retcode = -1
        if self.pathname != '' and os.path.isdir(self.pathname):
            for astream, adata in NifFormat.walkData(self.pathname):
                retcode = self.convert_nif(astream, adata)
                if retcode > 0:
                    break
        # lookup by file names
        elif self.files:
            for file in self.files:
                stream = open(file,'rb')
                retcode = self.convert_nif(stream, self.data)

        return retcode

    def convert_nif(self,stream,data):
        raise NotImplementedError('this is an abstract method and should not be called directly')

    def clean_check(self):
        ok = True
        if self.pathname == '' and not self.files:
            ok = False
        return ok
