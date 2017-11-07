from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
import traceback
import os
import view.windowui
import model.nifcleaner as nif


class ExampleApp(QtWidgets.QMainWindow, view.windowui.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.nifconverter = nif.NifConverter()
        self.browseButton.clicked.connect(self.search_file)
        self.convertButton.clicked.connect(self.convert_file)

    def search_file(self):
        display = ''
        if self.radioDirSearch.isChecked():
            file_name = QFileDialog.getExistingDirectory(self, "Select directory")
            self.nifconverter.pathname = file_name
            display = file_name
        elif self.radioFileSearch.isChecked():
            file_names = QFileDialog.getOpenFileNames(self, "Open Files", "", "Nif Files (*.nif)")
            # indexes -> 0: list of files, 1 : file extension
            if file_names:
                if file_names[0]:
                    self.nifconverter.files = file_names[0]
                    display = os.path.dirname(file_names[0][0])
        self.pathText.setText(display)

    def convert_file(self):
        try:
            exitcode = self.nifconverter.nif_to_blender()
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
