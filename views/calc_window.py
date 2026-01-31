# views/calc_window.py
from PyQt5 import QtWidgets, uic, QtCore

class CalcWindow(QtWidgets.QDialog):
    okClicked = QtCore.pyqtSignal()   # 메인으로 보낼 신호

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("./ui/calc.ui", self)

        # calc.ui 안에 QPushButton objectName = btr_ok
        self.btr_ok.clicked.connect(self.on_ok)

    def on_ok(self):
        self.okClicked.emit()
        self.close()
