# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_sensor_step.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1097, 705)
        self.listIssues = QtWidgets.QListWidget(Form)
        self.listIssues.setGeometry(QtCore.QRect(10, 440, 311, 171))
        self.listIssues.setObjectName("listIssues")
        self.leStatus = QtWidgets.QLineEdit(Form)
        self.leStatus.setGeometry(QtCore.QRect(60, 610, 261, 20))
        self.leStatus.setText("")
        self.leStatus.setReadOnly(True)
        self.leStatus.setObjectName("leStatus")
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setGeometry(QtCore.QRect(10, 610, 51, 20))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 20, 331, 41))
        self.label.setObjectName("label")
        self.ckCheckFeet = QtWidgets.QCheckBox(Form)
        self.ckCheckFeet.setGeometry(QtCore.QRect(10, 400, 351, 31))
        self.ckCheckFeet.setObjectName("ckCheckFeet")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 300, 101, 17))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 201, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.sbID = QtWidgets.QSpinBox(self.frame)
        self.sbID.setGeometry(QtCore.QRect(110, 0, 91, 21))
        self.sbID.setObjectName("sbID")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 111, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_27.setGeometry(QtCore.QRect(0, 20, 111, 20))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pbSave = QtWidgets.QPushButton(self.frame)
        self.pbSave.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.pbSave.setObjectName("pbSave")
        self.pbCancel = QtWidgets.QPushButton(self.frame)
        self.pbCancel.setGeometry(QtCore.QRect(100, 80, 71, 21))
        self.pbCancel.setObjectName("pbCancel")
        self.pbNew = QtWidgets.QPushButton(self.frame)
        self.pbNew.setEnabled(True)
        self.pbNew.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.pbNew.setObjectName("pbNew")
        self.pbEdit = QtWidgets.QPushButton(self.frame)
        self.pbEdit.setGeometry(QtCore.QRect(100, 50, 71, 21))
        self.pbEdit.setObjectName("pbEdit")
        self.cbInstitution = QtWidgets.QComboBox(self.frame)
        self.cbInstitution.setGeometry(QtCore.QRect(110, 20, 91, 21))
        self.cbInstitution.setObjectName("cbInstitution")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.cbInstitution.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 121, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 420, 191, 16))
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 140, 831, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pbClear6 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear6.setGeometry(QtCore.QRect(780, 120, 51, 21))
        self.pbClear6.setObjectName("pbClear6")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(0, 60, 61, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.leBaseplate6 = QtWidgets.QLineEdit(self.frame_2)
        self.leBaseplate6.setGeometry(QtCore.QRect(440, 120, 91, 20))
        self.leBaseplate6.setObjectName("leBaseplate6")
        self.leBaseplate3 = QtWidgets.QLineEdit(self.frame_2)
        self.leBaseplate3.setGeometry(QtCore.QRect(440, 60, 91, 20))
        self.leBaseplate3.setObjectName("leBaseplate3")
        self.sbTool6 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool6.setGeometry(QtCore.QRect(180, 120, 51, 21))
        self.sbTool6.setMinimum(-1)
        self.sbTool6.setMaximum(2147483647)
        self.sbTool6.setObjectName("sbTool6")
        self.leProtomodule2 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule2.setEnabled(True)
        self.leProtomodule2.setGeometry(QtCore.QRect(590, 40, 131, 20))
        self.leProtomodule2.setReadOnly(True)
        self.leProtomodule2.setObjectName("leProtomodule2")
        self.pbGoProtoModule1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtoModule1.setEnabled(True)
        self.pbGoProtoModule1.setGeometry(QtCore.QRect(720, 20, 51, 21))
        self.pbGoProtoModule1.setObjectName("pbGoProtoModule1")
        self.pbGoBaseplate6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoBaseplate6.setGeometry(QtCore.QRect(530, 120, 51, 21))
        self.pbGoBaseplate6.setObjectName("pbGoBaseplate6")
        self.pbClear3 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear3.setGeometry(QtCore.QRect(780, 60, 51, 21))
        self.pbClear3.setObjectName("pbClear3")
        self.leBaseplate5 = QtWidgets.QLineEdit(self.frame_2)
        self.leBaseplate5.setGeometry(QtCore.QRect(440, 100, 91, 20))
        self.leBaseplate5.setObjectName("leBaseplate5")
        self.pbGoSensor2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoSensor2.setGeometry(QtCore.QRect(380, 40, 51, 21))
        self.pbGoSensor2.setObjectName("pbGoSensor2")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(0, 100, 61, 20))
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pbGoTool3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool3.setGeometry(QtCore.QRect(230, 60, 51, 21))
        self.pbGoTool3.setObjectName("pbGoTool3")
        self.pbGoProtoModule4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtoModule4.setEnabled(True)
        self.pbGoProtoModule4.setGeometry(QtCore.QRect(720, 80, 51, 21))
        self.pbGoProtoModule4.setObjectName("pbGoProtoModule4")
        self.leSensor5 = QtWidgets.QLineEdit(self.frame_2)
        self.leSensor5.setGeometry(QtCore.QRect(290, 100, 91, 20))
        self.leSensor5.setObjectName("leSensor5")
        self.leProtomodule1 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule1.setEnabled(True)
        self.leProtomodule1.setGeometry(QtCore.QRect(590, 20, 131, 20))
        self.leProtomodule1.setReadOnly(True)
        self.leProtomodule1.setObjectName("leProtomodule1")
        self.pbClear1 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear1.setGeometry(QtCore.QRect(780, 20, 51, 21))
        self.pbClear1.setObjectName("pbClear1")
        self.pbClear2 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear2.setGeometry(QtCore.QRect(780, 40, 51, 21))
        self.pbClear2.setObjectName("pbClear2")
        self.pbGoTool1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool1.setGeometry(QtCore.QRect(230, 20, 51, 21))
        self.pbGoTool1.setObjectName("pbGoTool1")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(0, 0, 61, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pbGoBaseplate4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoBaseplate4.setGeometry(QtCore.QRect(530, 80, 51, 21))
        self.pbGoBaseplate4.setObjectName("pbGoBaseplate4")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(290, 0, 141, 20))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pbGoProtoModule2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtoModule2.setEnabled(True)
        self.pbGoProtoModule2.setGeometry(QtCore.QRect(720, 40, 51, 21))
        self.pbGoProtoModule2.setObjectName("pbGoProtoModule2")
        self.pbGoSensor4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoSensor4.setGeometry(QtCore.QRect(380, 80, 51, 21))
        self.pbGoSensor4.setObjectName("pbGoSensor4")
        self.pbGoProtoModule5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtoModule5.setEnabled(True)
        self.pbGoProtoModule5.setGeometry(QtCore.QRect(720, 100, 51, 21))
        self.pbGoProtoModule5.setObjectName("pbGoProtoModule5")
        self.pbGoBaseplate5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoBaseplate5.setGeometry(QtCore.QRect(530, 100, 51, 21))
        self.pbGoBaseplate5.setObjectName("pbGoBaseplate5")
        self.leProtomodule6 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule6.setEnabled(True)
        self.leProtomodule6.setGeometry(QtCore.QRect(590, 120, 131, 20))
        self.leProtomodule6.setReadOnly(True)
        self.leProtomodule6.setObjectName("leProtomodule6")
        self.pbClear5 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear5.setGeometry(QtCore.QRect(780, 100, 51, 21))
        self.pbClear5.setObjectName("pbClear5")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_14.setEnabled(True)
        self.lineEdit_14.setGeometry(QtCore.QRect(590, 0, 181, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.leSensor1 = QtWidgets.QLineEdit(self.frame_2)
        self.leSensor1.setGeometry(QtCore.QRect(290, 20, 91, 20))
        self.leSensor1.setObjectName("leSensor1")
        self.pbClear4 = QtWidgets.QPushButton(self.frame_2)
        self.pbClear4.setGeometry(QtCore.QRect(780, 80, 51, 21))
        self.pbClear4.setObjectName("pbClear4")
        self.leSensor6 = QtWidgets.QLineEdit(self.frame_2)
        self.leSensor6.setGeometry(QtCore.QRect(290, 120, 91, 20))
        self.leSensor6.setObjectName("leSensor6")
        self.pbGoBaseplate2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoBaseplate2.setGeometry(QtCore.QRect(530, 40, 51, 21))
        self.pbGoBaseplate2.setObjectName("pbGoBaseplate2")
        self.sbTool4 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool4.setGeometry(QtCore.QRect(180, 80, 51, 22))
        self.sbTool4.setMinimum(-1)
        self.sbTool4.setMaximum(2147483647)
        self.sbTool4.setObjectName("sbTool4")
        self.pbGoBaseplate3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoBaseplate3.setGeometry(QtCore.QRect(530, 60, 51, 21))
        self.pbGoBaseplate3.setObjectName("pbGoBaseplate3")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(0, 40, 61, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.sbTool1 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool1.setGeometry(QtCore.QRect(180, 20, 51, 22))
        self.sbTool1.setMinimum(-1)
        self.sbTool1.setMaximum(2147483647)
        self.sbTool1.setObjectName("sbTool1")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(0, 20, 61, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pbGoTool4 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool4.setGeometry(QtCore.QRect(230, 80, 51, 21))
        self.pbGoTool4.setObjectName("pbGoTool4")
        self.pbGoSensor1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoSensor1.setGeometry(QtCore.QRect(380, 20, 51, 21))
        self.pbGoSensor1.setObjectName("pbGoSensor1")
        self.pbGoTool6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool6.setGeometry(QtCore.QRect(230, 120, 51, 21))
        self.pbGoTool6.setObjectName("pbGoTool6")
        self.sbTool3 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool3.setGeometry(QtCore.QRect(180, 60, 51, 22))
        self.sbTool3.setMinimum(-1)
        self.sbTool3.setMaximum(2147483647)
        self.sbTool3.setObjectName("sbTool3")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(180, 0, 101, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(440, 0, 141, 20))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.sbTool5 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool5.setGeometry(QtCore.QRect(180, 100, 51, 22))
        self.sbTool5.setMinimum(-1)
        self.sbTool5.setMaximum(2147483647)
        self.sbTool5.setObjectName("sbTool5")
        self.leBaseplate4 = QtWidgets.QLineEdit(self.frame_2)
        self.leBaseplate4.setGeometry(QtCore.QRect(440, 80, 91, 20))
        self.leBaseplate4.setObjectName("leBaseplate4")
        self.pbGoSensor3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoSensor3.setGeometry(QtCore.QRect(380, 60, 51, 21))
        self.pbGoSensor3.setObjectName("pbGoSensor3")
        self.leProtomodule4 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule4.setEnabled(True)
        self.leProtomodule4.setGeometry(QtCore.QRect(590, 80, 131, 20))
        self.leProtomodule4.setReadOnly(True)
        self.leProtomodule4.setObjectName("leProtomodule4")
        self.leSensor3 = QtWidgets.QLineEdit(self.frame_2)
        self.leSensor3.setGeometry(QtCore.QRect(290, 60, 91, 20))
        self.leSensor3.setObjectName("leSensor3")
        self.pbGoTool5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool5.setGeometry(QtCore.QRect(230, 100, 51, 21))
        self.pbGoTool5.setObjectName("pbGoTool5")
        self.pbGoBaseplate1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoBaseplate1.setGeometry(QtCore.QRect(530, 20, 51, 21))
        self.pbGoBaseplate1.setObjectName("pbGoBaseplate1")
        self.leSensor2 = QtWidgets.QLineEdit(self.frame_2)
        self.leSensor2.setGeometry(QtCore.QRect(290, 40, 91, 20))
        self.leSensor2.setObjectName("leSensor2")
        self.sbTool2 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTool2.setGeometry(QtCore.QRect(180, 40, 51, 22))
        self.sbTool2.setMinimum(-1)
        self.sbTool2.setMaximum(2147483647)
        self.sbTool2.setObjectName("sbTool2")
        self.pbGoSensor6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoSensor6.setGeometry(QtCore.QRect(380, 120, 51, 21))
        self.pbGoSensor6.setObjectName("pbGoSensor6")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(0, 120, 61, 21))
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.leProtomodule3 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule3.setEnabled(True)
        self.leProtomodule3.setGeometry(QtCore.QRect(590, 60, 131, 20))
        self.leProtomodule3.setReadOnly(True)
        self.leProtomodule3.setObjectName("leProtomodule3")
        self.leSensor4 = QtWidgets.QLineEdit(self.frame_2)
        self.leSensor4.setGeometry(QtCore.QRect(290, 80, 91, 20))
        self.leSensor4.setObjectName("leSensor4")
        self.leProtomodule5 = QtWidgets.QLineEdit(self.frame_2)
        self.leProtomodule5.setEnabled(True)
        self.leProtomodule5.setGeometry(QtCore.QRect(590, 100, 131, 20))
        self.leProtomodule5.setReadOnly(True)
        self.leProtomodule5.setObjectName("leProtomodule5")
        self.pbGoTool2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTool2.setGeometry(QtCore.QRect(230, 40, 51, 21))
        self.pbGoTool2.setObjectName("pbGoTool2")
        self.pbGoSensor5 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoSensor5.setGeometry(QtCore.QRect(380, 100, 51, 21))
        self.pbGoSensor5.setObjectName("pbGoSensor5")
        self.pbGoProtoModule6 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtoModule6.setEnabled(True)
        self.pbGoProtoModule6.setGeometry(QtCore.QRect(720, 120, 51, 21))
        self.pbGoProtoModule6.setObjectName("pbGoProtoModule6")
        self.leBaseplate2 = QtWidgets.QLineEdit(self.frame_2)
        self.leBaseplate2.setGeometry(QtCore.QRect(440, 40, 91, 20))
        self.leBaseplate2.setObjectName("leBaseplate2")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(0, 80, 61, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.leBaseplate1 = QtWidgets.QLineEdit(self.frame_2)
        self.leBaseplate1.setGeometry(QtCore.QRect(440, 20, 91, 20))
        self.leBaseplate1.setObjectName("leBaseplate1")
        self.pbGoProtoModule3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoProtoModule3.setEnabled(True)
        self.pbGoProtoModule3.setGeometry(QtCore.QRect(720, 60, 51, 21))
        self.pbGoProtoModule3.setObjectName("pbGoProtoModule3")
        self.sbTrayAssembly2 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTrayAssembly2.setGeometry(QtCore.QRect(70, 60, 51, 41))
        self.sbTrayAssembly2.setMinimum(-1)
        self.sbTrayAssembly2.setMaximum(2147483647)
        self.sbTrayAssembly2.setObjectName("sbTrayAssembly2")
        self.pbGoTrayAssembly1 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTrayAssembly1.setGeometry(QtCore.QRect(120, 30, 51, 21))
        self.pbGoTrayAssembly1.setObjectName("pbGoTrayAssembly1")
        self.sbTrayAssembly3 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTrayAssembly3.setGeometry(QtCore.QRect(70, 100, 51, 41))
        self.sbTrayAssembly3.setMinimum(-1)
        self.sbTrayAssembly3.setMaximum(2147483647)
        self.sbTrayAssembly3.setObjectName("sbTrayAssembly3")
        self.sbTrayAssembly1 = QtWidgets.QSpinBox(self.frame_2)
        self.sbTrayAssembly1.setGeometry(QtCore.QRect(70, 20, 51, 41))
        self.sbTrayAssembly1.setMinimum(-1)
        self.sbTrayAssembly1.setMaximum(2147483647)
        self.sbTrayAssembly1.setObjectName("sbTrayAssembly1")
        self.pbGoTrayAssembly3 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTrayAssembly3.setGeometry(QtCore.QRect(120, 110, 51, 21))
        self.pbGoTrayAssembly3.setObjectName("pbGoTrayAssembly3")
        self.pbGoTrayAssembly2 = QtWidgets.QPushButton(self.frame_2)
        self.pbGoTrayAssembly2.setGeometry(QtCore.QRect(120, 70, 51, 21))
        self.pbGoTrayAssembly2.setObjectName("pbGoTrayAssembly2")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(70, 0, 101, 20))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 320, 301, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.leBatchAraldite = QtWidgets.QLineEdit(self.frame_3)
        self.leBatchAraldite.setGeometry(QtCore.QRect(180, 20, 71, 20))
        self.leBatchAraldite.setObjectName("leBatchAraldite")
        self.pbGoBatchAraldite = QtWidgets.QPushButton(self.frame_3)
        self.pbGoBatchAraldite.setGeometry(QtCore.QRect(250, 20, 51, 21))
        self.pbGoBatchAraldite.setObjectName("pbGoBatchAraldite")
        self.sbTrayComponent = QtWidgets.QSpinBox(self.frame_3)
        self.sbTrayComponent.setGeometry(QtCore.QRect(180, 0, 71, 21))
        self.sbTrayComponent.setMinimum(-1)
        self.sbTrayComponent.setMaximum(999999)
        self.sbTrayComponent.setObjectName("sbTrayComponent")
        self.pbGoTrayComponent = QtWidgets.QPushButton(self.frame_3)
        self.pbGoTrayComponent.setGeometry(QtCore.QRect(250, 0, 51, 21))
        self.pbGoTrayComponent.setObjectName("pbGoTrayComponent")
        self.leTextAraldite = QtWidgets.QLineEdit(self.frame_3)
        self.leTextAraldite.setGeometry(QtCore.QRect(90, 20, 91, 21))
        self.leTextAraldite.setReadOnly(True)
        self.leTextAraldite.setObjectName("leTextAraldite")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setGeometry(QtCore.QRect(0, 0, 181, 21))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.leTextTape50 = QtWidgets.QLineEdit(self.frame_3)
        self.leTextTape50.setGeometry(QtCore.QRect(90, 40, 91, 21))
        self.leTextTape50.setReadOnly(True)
        self.leTextTape50.setObjectName("leTextTape50")
        self.pbGoTape50 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoTape50.setGeometry(QtCore.QRect(250, 40, 51, 21))
        self.pbGoTape50.setObjectName("pbGoTape50")
        self.leTextTape120 = QtWidgets.QLineEdit(self.frame_3)
        self.leTextTape120.setGeometry(QtCore.QRect(90, 60, 91, 21))
        self.leTextTape120.setReadOnly(True)
        self.leTextTape120.setObjectName("leTextTape120")
        self.pbGoTape120 = QtWidgets.QPushButton(self.frame_3)
        self.pbGoTape120.setGeometry(QtCore.QRect(250, 60, 51, 21))
        self.pbGoTape120.setObjectName("pbGoTape120")
        self.cbAdhesive = QtWidgets.QComboBox(self.frame_3)
        self.cbAdhesive.setGeometry(QtCore.QRect(0, 45, 91, 32))
        self.cbAdhesive.setObjectName("cbAdhesive")
        self.cbAdhesive.addItem("")
        self.cbAdhesive.addItem("")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_33.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.leTape50 = QtWidgets.QLineEdit(self.frame_3)
        self.leTape50.setGeometry(QtCore.QRect(180, 40, 71, 20))
        self.leTape50.setObjectName("leTape50")
        self.leTape120 = QtWidgets.QLineEdit(self.frame_3)
        self.leTape120.setGeometry(QtCore.QRect(180, 60, 71, 20))
        self.leTape120.setObjectName("leTape120")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(380, 320, 311, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 161, 21))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pbRunStopNow = QtWidgets.QPushButton(self.frame_4)
        self.pbRunStopNow.setGeometry(QtCore.QRect(220, 50, 91, 21))
        self.pbRunStopNow.setObjectName("pbRunStopNow")
        self.dtRunStart = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dtRunStart.setGeometry(QtCore.QRect(70, 30, 151, 21))
        self.dtRunStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtRunStart.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtRunStart.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtRunStart.setCalendarPopup(True)
        self.dtRunStart.setObjectName("dtRunStart")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_28.setGeometry(QtCore.QRect(0, 50, 71, 21))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.pbRunStartNow = QtWidgets.QPushButton(self.frame_4)
        self.pbRunStartNow.setGeometry(QtCore.QRect(220, 30, 91, 21))
        self.pbRunStartNow.setObjectName("pbRunStartNow")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(0, 30, 71, 21))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.cbUserPerformed = QtWidgets.QComboBox(self.frame_4)
        self.cbUserPerformed.setGeometry(QtCore.QRect(160, 0, 151, 21))
        self.cbUserPerformed.setObjectName("cbUserPerformed")
        self.dtRunStop = QtWidgets.QDateTimeEdit(self.frame_4)
        self.dtRunStop.setGeometry(QtCore.QRect(70, 50, 151, 21))
        self.dtRunStop.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dtRunStop.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.dtRunStop.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dtRunStop.setCalendarPopup(True)
        self.dtRunStop.setObjectName("dtRunStop")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(380, 440, 311, 251))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_29.setGeometry(QtCore.QRect(0, 200, 61, 20))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.pbCancelSearch = QtWidgets.QPushButton(self.frame_5)
        self.pbCancelSearch.setGeometry(QtCore.QRect(120, 230, 101, 21))
        self.pbCancelSearch.setObjectName("pbCancelSearch")
        self.leSearchStatus = QtWidgets.QLineEdit(self.frame_5)
        self.leSearchStatus.setGeometry(QtCore.QRect(60, 200, 251, 20))
        self.leSearchStatus.setText("")
        self.leSearchStatus.setReadOnly(True)
        self.leSearchStatus.setObjectName("leSearchStatus")
        self.pbAddPart = QtWidgets.QPushButton(self.frame_5)
        self.pbAddPart.setGeometry(QtCore.QRect(0, 230, 101, 21))
        self.pbAddPart.setObjectName("pbAddPart")
        self.lwPartList = QtWidgets.QListWidget(self.frame_5)
        self.lwPartList.setGeometry(QtCore.QRect(0, 0, 311, 201))
        self.lwPartList.setObjectName("lwPartList")

        self.retranslateUi(Form)
        self.cbInstitution.setCurrentIndex(-1)
        self.cbAdhesive.setCurrentIndex(-1)
        self.cbUserPerformed.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.listIssues.setToolTip(_translate("Form", "list of issues"))
        self.lineEdit_26.setText(_translate("Form", "Status:"))
        self.label.setText(_translate("Form", "Warning:  all parts must be downloaded locally\n"
"before assembly"))
        self.ckCheckFeet.setText(_translate("Form", "Check:  correct feet are installed on pickup tools"))
        self.label_2.setText(_translate("Form", "Assembly run"))
        self.lineEdit.setText(_translate("Form", "Sensor step ID"))
        self.lineEdit_27.setText(_translate("Form", "Institution"))
        self.pbSave.setText(_translate("Form", "Save"))
        self.pbCancel.setText(_translate("Form", "Cancel"))
        self.pbNew.setText(_translate("Form", "New"))
        self.pbEdit.setText(_translate("Form", "Edit"))
        self.cbInstitution.setItemText(0, _translate("Form", "CERN"))
        self.cbInstitution.setItemText(1, _translate("Form", "FNAL"))
        self.cbInstitution.setItemText(2, _translate("Form", "UCSB"))
        self.cbInstitution.setItemText(3, _translate("Form", "UMN"))
        self.cbInstitution.setItemText(4, _translate("Form", "HEPHY"))
        self.cbInstitution.setItemText(5, _translate("Form", "HPK"))
        self.cbInstitution.setItemText(6, _translate("Form", "CMU"))
        self.cbInstitution.setItemText(7, _translate("Form", "TTU"))
        self.cbInstitution.setItemText(8, _translate("Form", "IHEP"))
        self.cbInstitution.setItemText(9, _translate("Form", "TIFR"))
        self.cbInstitution.setItemText(10, _translate("Form", "NTU"))
        self.cbInstitution.setItemText(11, _translate("Form", "FSU"))
        self.label_3.setText(_translate("Form", "Assembly info"))
        self.label_4.setText(_translate("Form", "Items to add:"))
        self.pbClear6.setText(_translate("Form", "clear"))
        self.lineEdit_17.setText(_translate("Form", "3 (2, 1)"))
        self.pbGoProtoModule1.setText(_translate("Form", "go to"))
        self.pbGoBaseplate6.setText(_translate("Form", "select"))
        self.pbClear3.setText(_translate("Form", "clear"))
        self.pbGoSensor2.setText(_translate("Form", "select"))
        self.lineEdit_19.setText(_translate("Form", "5 (3, 1)"))
        self.pbGoTool3.setText(_translate("Form", "go to"))
        self.pbGoProtoModule4.setText(_translate("Form", "go to"))
        self.pbClear1.setText(_translate("Form", "clear"))
        self.pbClear2.setText(_translate("Form", "clear"))
        self.pbGoTool1.setText(_translate("Form", "go to"))
        self.lineEdit_12.setText(_translate("Form", "position"))
        self.pbGoBaseplate4.setText(_translate("Form", "select"))
        self.lineEdit_23.setText(_translate("Form", "sensor serial"))
        self.pbGoProtoModule2.setText(_translate("Form", "go to"))
        self.pbGoSensor4.setText(_translate("Form", "select"))
        self.pbGoProtoModule5.setText(_translate("Form", "go to"))
        self.pbGoBaseplate5.setText(_translate("Form", "select"))
        self.pbClear5.setText(_translate("Form", "clear"))
        self.lineEdit_14.setText(_translate("Form", "protomodule serial (auto)"))
        self.pbClear4.setText(_translate("Form", "clear"))
        self.pbGoBaseplate2.setText(_translate("Form", "select"))
        self.pbGoBaseplate3.setText(_translate("Form", "select"))
        self.lineEdit_16.setText(_translate("Form", "2 (1, 2)"))
        self.lineEdit_15.setText(_translate("Form", "1 (1, 1)"))
        self.pbGoTool4.setText(_translate("Form", "go to"))
        self.pbGoSensor1.setText(_translate("Form", "select"))
        self.pbGoTool6.setText(_translate("Form", "go to"))
        self.lineEdit_13.setText(_translate("Form", "sensor tool ID"))
        self.lineEdit_22.setText(_translate("Form", "baseplate serial"))
        self.pbGoSensor3.setText(_translate("Form", "select"))
        self.pbGoTool5.setText(_translate("Form", "go to"))
        self.pbGoBaseplate1.setText(_translate("Form", "select"))
        self.pbGoSensor6.setText(_translate("Form", "select"))
        self.lineEdit_20.setText(_translate("Form", "6 (3, 2)"))
        self.pbGoTool2.setText(_translate("Form", "go to"))
        self.pbGoSensor5.setText(_translate("Form", "select"))
        self.pbGoProtoModule6.setText(_translate("Form", "go to"))
        self.lineEdit_18.setText(_translate("Form", "4 (2, 2)"))
        self.pbGoProtoModule3.setText(_translate("Form", "go to"))
        self.pbGoTrayAssembly1.setText(_translate("Form", "go to"))
        self.pbGoTrayAssembly3.setText(_translate("Form", "go to"))
        self.pbGoTrayAssembly2.setText(_translate("Form", "go to"))
        self.lineEdit_25.setText(_translate("Form", "assembly tray"))
        self.pbGoBatchAraldite.setText(_translate("Form", "go to"))
        self.pbGoTrayComponent.setText(_translate("Form", "go to"))
        self.leTextAraldite.setText(_translate("Form", "araldite batch"))
        self.lineEdit_24.setText(_translate("Form", "sensor component tray"))
        self.leTextTape50.setText(_translate("Form", "50um tape"))
        self.pbGoTape50.setText(_translate("Form", "go to"))
        self.leTextTape120.setText(_translate("Form", "120um tape"))
        self.pbGoTape120.setText(_translate("Form", "go to"))
        self.cbAdhesive.setItemText(0, _translate("Form", "Araldite"))
        self.cbAdhesive.setItemText(1, _translate("Form", "Tape"))
        self.lineEdit_33.setText(_translate("Form", "Adhesive?"))
        self.lineEdit_2.setText(_translate("Form", "who performed step"))
        self.pbRunStopNow.setText(_translate("Form", "set to now"))
        self.lineEdit_28.setText(_translate("Form", "run stop"))
        self.pbRunStartNow.setText(_translate("Form", "set to now"))
        self.lineEdit_10.setText(_translate("Form", "run start"))
        self.lineEdit_29.setText(_translate("Form", "Status:"))
        self.pbCancelSearch.setText(_translate("Form", "Cancel"))
        self.pbAddPart.setText(_translate("Form", "Add item"))
