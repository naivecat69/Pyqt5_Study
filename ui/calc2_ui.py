# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc2.ui'
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic is run again.
#
# 사용 예제(한국어): Calc2Widget에서 Ui_Form을 상속하고 setupUi(self)를 호출합니다.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_a = QtWidgets.QLabel(Form)
        self.label_a.setObjectName("label_a")
        self.gridLayout.addWidget(self.label_a, 0, 0, 1, 1)
        self.input_a = QtWidgets.QLineEdit(Form)
        self.input_a.setObjectName("input_a")
        self.gridLayout.addWidget(self.input_a, 0, 1, 1, 1)
        self.label_b = QtWidgets.QLabel(Form)
        self.label_b.setObjectName("label_b")
        self.gridLayout.addWidget(self.label_b, 1, 0, 1, 1)
        self.input_b = QtWidgets.QLineEdit(Form)
        self.input_b.setObjectName("input_b")
        self.gridLayout.addWidget(self.input_b, 1, 1, 1, 1)
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setSpacing(8)
        self.buttonLayout.setObjectName("buttonLayout")
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setObjectName("btn_add")
        self.buttonLayout.addWidget(self.btn_add)
        self.btn_sub = QtWidgets.QPushButton(Form)
        self.btn_sub.setObjectName("btn_sub")
        self.buttonLayout.addWidget(self.btn_sub)
        self.btn_mul = QtWidgets.QPushButton(Form)
        self.btn_mul.setObjectName("btn_mul")
        self.buttonLayout.addWidget(self.btn_mul)
        self.btn_div = QtWidgets.QPushButton(Form)
        self.btn_div.setObjectName("btn_div")
        self.buttonLayout.addWidget(self.btn_div)
        self.btn_clear = QtWidgets.QPushButton(Form)
        self.btn_clear.setObjectName("btn_clear")
        self.buttonLayout.addWidget(self.btn_clear)
        self.verticalLayout.addLayout(self.buttonLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator 2 (pyuic)"))
        self.label_title.setText(_translate("Form", "Calculator 2 - pyuic generated UI"))
        self.label_a.setText(_translate("Form", "A"))
        self.label_b.setText(_translate("Form", "B"))
        self.label_result.setText(_translate("Form", "Result: 0"))
        self.btn_add.setText(_translate("Form", "+"))
        self.btn_sub.setText(_translate("Form", "-"))
        self.btn_mul.setText(_translate("Form", "*"))
        self.btn_div.setText(_translate("Form", "/"))
        self.btn_clear.setText(_translate("Form", "Clear"))
