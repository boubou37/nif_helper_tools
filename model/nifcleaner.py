from pyffi.formats.nif import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox


# todo error handling
class NifCleaner:
    def __init__(self):
        self.pathname = ''
        self.data = NifFormat.Data()
        self.errorfile = ''
        self.files = []
        self.progressBar = None
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
        numfiles = 0
        i = 0
        self.progressBar.show()
        print(numfiles)
        if self.pathname != '' and os.path.isdir(self.pathname):
            numfiles = len(list(NifFormat.walkData(self.pathname)))
            for astream, adata in NifFormat.walkData(self.pathname):
                self.progressBar.setValue(100 * i / numfiles)
                retcode = self.convert_nif(astream, adata)
                i += 1
                if retcode > 0:
                    break
        # lookup by file names
        elif self.files:
            numfiles = len(self.files)
            for file in self.files:
                stream = open(file,'rb')
                self.progressBar.setValue(100 * i / numfiles)
                retcode = self.convert_nif(stream, self.data)
                i += 1

        self.progressBar.setValue(0)
        self.progressBar.hide()
        return retcode

    def convert_nif(self,stream,data):
        raise NotImplementedError('this is an abstract method and should not be called from this class')

    def clean_check(self):
        ok = True
        if self.pathname == '' and not self.files:
            ok = False
        return ok
