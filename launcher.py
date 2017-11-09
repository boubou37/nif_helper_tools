from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
import traceback
import os
import view.windowui
import model.sky2blender as s2b
import model.blender2sky as b2s
import model.nifcleaner as nc


class ExampleApp(QtWidgets.QMainWindow, view.windowui.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.sky_to_blender_conv = s2b.SkyToBlenderConverter()
        self.blender_to_sky_conv = b2s.BlenderToSkyConverter()
        self.setup_connections()
        self.progressBar.hide()
        self.progressBarBS.hide()

    def setup_connections(self):
        self.radioDirSearch.clicked.connect(lambda: self.set_file_mode(self.sky_to_blender_conv, 1))
        self.radioFileSearch.clicked.connect(lambda: self.set_file_mode(self.sky_to_blender_conv, 2))
        self.radioDirSearchBS.clicked.connect(lambda: self.set_file_mode(self.blender_to_sky_conv, 1))
        self.radioFileSearchBS.clicked.connect(lambda: self.set_file_mode(self.blender_to_sky_conv, 2))
        self.browseButton.clicked.connect(lambda: self.search_file(self.sky_to_blender_conv))
        self.browseBS.clicked.connect(lambda: self.search_file(self.blender_to_sky_conv))
        self.convertButton.clicked.connect(lambda: self.convert_file(self.sky_to_blender_conv, self.progressBar))
        self.convertButtonBS.clicked.connect(lambda: self.convert_file(self.blender_to_sky_conv, self.progressBarBS))

    def set_file_mode(self, converter, val):
        if val == 1:
            converter.radioDirCheck = True
        elif val == 2:
            converter.radioDirCheck = False
        converter.radioFileCheck = not converter.radioDirCheck

    def search_file(self, converter):
        # safety check to only allows file cleaners
        if not isinstance(converter, nc.NifCleaner):
            return

        display = ''
        radio_dir_checked = converter.radioDirCheck
        radio_file_checked = converter.radioFileCheck

        if radio_dir_checked:
            file_name = QFileDialog.getExistingDirectory(self, "Select directory")
            converter.pathname = file_name
            converter.files = []  # we keep mutually exclusive behavior
            display = file_name
        elif radio_file_checked:
            file_names = QFileDialog.getOpenFileNames(self, "Open Files", "", "Nif Files (*.nif)")
            # indexes -> 0: list of files, 1 : file extension
            if file_names:
                if file_names[0]:
                    converter.files = file_names[0]
                    converter.pathname = '' # we keep mutually exclusive behavior
                    display = os.path.dirname(file_names[0][0])
        if isinstance(converter,s2b.SkyToBlenderConverter):
            self.pathText.setText(display)
        else:
            self.pathTextBS.setText(display)

    def convert_file(self, converter, progressBar):
        converter.progressBar = progressBar
        try:
            exitcode = converter.clean_nif()
            if exitcode == 0:
                QMessageBox.information(self, 'Info', 'Conversion done')
            else:
                QMessageBox.information(self, 'Info', 'Error during conversion')
        except Exception:
            traceback.print_exc()


def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()
