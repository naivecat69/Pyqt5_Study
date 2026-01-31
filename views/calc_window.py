# views/calc_window.py
# 간단한 다이얼로그 예제 (기존 샘플)
# 사용 예제: OK 버튼 클릭 시 시그널을 메인으로 전달
from PyQt5 import QtWidgets, uic, QtCore

class CalcWindow(QtWidgets.QDialog):
    okClicked = QtCore.pyqtSignal()   # 메인으로 보낼 신호

    def __init__(self, parent=None):
        super().__init__(parent)
        # Designer UI 로드
        uic.loadUi("./ui/calc.ui", self)

        # calc.ui 안에 QPushButton objectName = btr_ok
        self.btr_ok.clicked.connect(self.on_ok)

    def on_ok(self):
        # OK 클릭 시 메인에 신호 전달 후 닫기
        self.okClicked.emit()
        self.close()
