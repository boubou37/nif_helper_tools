# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 200, 481, 141))
        self.groupBox.setObjectName("groupBox")
        self.browseButton = QtWidgets.QPushButton(self.groupBox)
        self.browseButton.setGeometry(QtCore.QRect(220, 40, 75, 21))
        self.browseButton.setObjectName("browseButton")
        self.pathText = QtWidgets.QLineEdit(self.groupBox)
        self.pathText.setGeometry(QtCore.QRect(20, 40, 171, 21))
        self.pathText.setText("")
        self.pathText.setObjectName("pathText")
        self.convertButton = QtWidgets.QPushButton(self.groupBox)
        self.convertButton.setGeometry(QtCore.QRect(100, 90, 75, 23))
        self.convertButton.setObjectName("convertButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 20, 141, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radioDirSearch = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioDirSearch.setObjectName("radioDirSearch")
        self.verticalLayout.addWidget(self.radioDirSearch)
        self.radioFileSearch = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioFileSearch.setObjectName("radioFileSearch")
        self.verticalLayout.addWidget(self.radioFileSearch)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Skyrim to blender conversion"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.label.setText(_translate("MainWindow", "Search by"))
        self.radioDirSearch.setText(_translate("MainWindow", "Directory"))
        self.radioFileSearch.setText(_translate("MainWindow", "File"))

