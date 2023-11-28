# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1417, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.hlMainSections = QtWidgets.QHBoxLayout()
        self.hlMainSections.setSpacing(0)
        self.hlMainSections.setObjectName("hlMainSections")
        self.vlUISelect = QtWidgets.QVBoxLayout()
        self.vlUISelect.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlUISelect.setSpacing(0)
        self.vlUISelect.setObjectName("vlUISelect")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.vlUISelect.addWidget(self.lineEdit_4)
        self.listUsers = QtWidgets.QListWidget(self.centralwidget)
        self.listUsers.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listUsers.sizePolicy().hasHeightForWidth())
        self.listUsers.setSizePolicy(sizePolicy)
        self.listUsers.setMaximumSize(QtCore.QSize(16777215, 30))
        self.listUsers.setObjectName("listUsers")
        item = QtWidgets.QListWidgetItem()
        self.listUsers.addItem(item)
        self.vlUISelect.addWidget(self.listUsers)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vlUISelect.addItem(spacerItem)
        self.leInformation = QtWidgets.QLineEdit(self.centralwidget)
        self.leInformation.setReadOnly(True)
        self.leInformation.setObjectName("leInformation")
        self.vlUISelect.addWidget(self.leInformation)
        self.listInformation = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listInformation.sizePolicy().hasHeightForWidth())
        self.listInformation.setSizePolicy(sizePolicy)
        self.listInformation.setMinimumSize(QtCore.QSize(0, 150))
        self.listInformation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listInformation.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listInformation.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listInformation.setObjectName("listInformation")
        item = QtWidgets.QListWidgetItem()
        self.listInformation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listInformation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listInformation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listInformation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listInformation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listInformation.addItem(item)
        self.vlUISelect.addWidget(self.listInformation)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vlUISelect.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.vlUISelect.addWidget(self.lineEdit)
        self.listAssembly = QtWidgets.QListWidget(self.centralwidget)
        self.listAssembly.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listAssembly.sizePolicy().hasHeightForWidth())
        self.listAssembly.setSizePolicy(sizePolicy)
        self.listAssembly.setMinimumSize(QtCore.QSize(0, 110))
        self.listAssembly.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listAssembly.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listAssembly.setAutoScroll(True)
        self.listAssembly.setObjectName("listAssembly")
        item = QtWidgets.QListWidgetItem()
        self.listAssembly.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listAssembly.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listAssembly.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listAssembly.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listAssembly.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listAssembly.addItem(item)
        self.vlUISelect.addWidget(self.listAssembly)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vlUISelect.addItem(spacerItem2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.vlUISelect.addWidget(self.lineEdit_2)
        self.listModules = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listModules.sizePolicy().hasHeightForWidth())
        self.listModules.setSizePolicy(sizePolicy)
        self.listModules.setObjectName("listModules")
        item = QtWidgets.QListWidgetItem()
        self.listModules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listModules.addItem(item)
        self.vlUISelect.addWidget(self.listModules)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vlUISelect.addItem(spacerItem3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 226, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pbUploadObject = QtWidgets.QPushButton(self.groupBox)
        self.pbUploadObject.setEnabled(False)
        self.pbUploadObject.setGeometry(QtCore.QRect(29, 30, 171, 25))
        self.pbUploadObject.setMinimumSize(QtCore.QSize(150, 0))
        self.pbUploadObject.setMaximumSize(QtCore.QSize(220, 16777215))
        self.pbUploadObject.setObjectName("pbUploadObject")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(5, 70, 221, 17))
        self.label.setObjectName("label")
        self.pbUploadDate = QtWidgets.QPushButton(self.groupBox)
        self.pbUploadDate.setEnabled(False)
        self.pbUploadDate.setGeometry(QtCore.QRect(30, 115, 161, 25))
        self.pbUploadDate.setMinimumSize(QtCore.QSize(150, 0))
        self.pbUploadDate.setObjectName("pbUploadDate")
        self.dUpload = QtWidgets.QDateEdit(self.groupBox)
        self.dUpload.setEnabled(False)
        self.dUpload.setGeometry(QtCore.QRect(35, 90, 151, 26))
        self.dUpload.setMinimumSize(QtCore.QSize(150, 0))
        self.dUpload.setCalendarPopup(True)
        self.dUpload.setDate(QtCore.QDate(2021, 1, 1))
        self.dUpload.setObjectName("dUpload")
        self.leStatus = QtWidgets.QLineEdit(self.groupBox)
        self.leStatus.setEnabled(False)
        self.leStatus.setGeometry(QtCore.QRect(10, 170, 211, 25))
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(5, 150, 211, 17))
        self.label_2.setObjectName("label_2")
        self.vlUISelect.addWidget(self.groupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vlUISelect.addItem(spacerItem4)
        self.vlUISelect.setStretch(3, 1)
        self.vlUISelect.setStretch(4, 6)
        self.vlUISelect.setStretch(6, 1)
        self.vlUISelect.setStretch(7, 5)
        self.hlMainSections.addLayout(self.vlUISelect)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlMainSections.addItem(spacerItem5)
        self.hlUIpane = QtWidgets.QHBoxLayout()
        self.hlUIpane.setSpacing(0)
        self.hlUIpane.setObjectName("hlUIpane")
        self.swPages = QtWidgets.QStackedWidget(self.centralwidget)
        self.swPages.setFrameShape(QtWidgets.QFrame.Box)
        self.swPages.setObjectName("swPages")
        self.hlUIpane.addWidget(self.swPages)
        self.hlMainSections.addLayout(self.hlUIpane)
        self.hlMainSections.setStretch(0, 8)
        self.hlMainSections.setStretch(1, 1)
        self.hlMainSections.setStretch(2, 40)
        self.gridLayout.addLayout(self.hlMainSections, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1417, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.listInformation.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_4.setText(_translate("MainWindow", "User management"))
        __sortingEnabled = self.listUsers.isSortingEnabled()
        self.listUsers.setSortingEnabled(False)
        item = self.listUsers.item(0)
        item.setText(_translate("MainWindow", "Users"))
        self.listUsers.setSortingEnabled(__sortingEnabled)
        self.leInformation.setText(_translate("MainWindow", "Parts, tooling, and supplies"))
        __sortingEnabled = self.listInformation.isSortingEnabled()
        self.listInformation.setSortingEnabled(False)
        item = self.listInformation.item(0)
        item.setText(_translate("MainWindow", "Search"))
        item = self.listInformation.item(1)
        item.setText(_translate("MainWindow", "Baseplates"))
        item = self.listInformation.item(2)
        item.setText(_translate("MainWindow", "Sensors"))
        item = self.listInformation.item(3)
        item.setText(_translate("MainWindow", "PCBs"))
        item = self.listInformation.item(4)
        item.setText(_translate("MainWindow", "Tooling"))
        item = self.listInformation.item(5)
        item.setText(_translate("MainWindow", "Supplies"))
        self.listInformation.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("MainWindow", "Production steps and testing"))
        __sortingEnabled = self.listAssembly.isSortingEnabled()
        self.listAssembly.setSortingEnabled(False)
        item = self.listAssembly.item(0)
        item.setText(_translate("MainWindow", "1. Sensor - pre-assembly"))
        item = self.listAssembly.item(1)
        item.setText(_translate("MainWindow", "2. Sensor - post-assembly"))
        item = self.listAssembly.item(2)
        item.setText(_translate("MainWindow", "3. PCB - pre-assembly"))
        item = self.listAssembly.item(3)
        item.setText(_translate("MainWindow", "4. PCB - post-assembly"))
        item = self.listAssembly.item(4)
        item.setText(_translate("MainWindow", "5. Wirebonding & encapsulating"))
        item = self.listAssembly.item(5)
        item.setText(_translate("MainWindow", "6. Module testing"))
        self.listAssembly.setSortingEnabled(__sortingEnabled)
        self.lineEdit_2.setText(_translate("MainWindow", "Protomodules and modules"))
        __sortingEnabled = self.listModules.isSortingEnabled()
        self.listModules.setSortingEnabled(False)
        item = self.listModules.item(0)
        item.setText(_translate("MainWindow", "Protomodules"))
        item = self.listModules.item(1)
        item.setText(_translate("MainWindow", "Modules"))
        self.listModules.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.lineEdit_3.setText(_translate("MainWindow", "Uploading to the HGCAL DB (WIP)"))
        self.pbUploadObject.setText(_translate("MainWindow", "Upload current object"))
        self.label.setText(_translate("MainWindow", "Upload objects created on date:"))
        self.pbUploadDate.setText(_translate("MainWindow", "Upload objects"))
        self.label_2.setText(_translate("MainWindow", "Upload status"))
