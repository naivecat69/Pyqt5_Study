# views/main_window.py
from PyQt5 import QtWidgets, uic
from views.calc_window import CalcWindow
from src.call_calc import calc

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/main.ui", self)

        # main.ui 안에 QPushButton objectName = btr_1
        self.btr_1.clicked.connect(self.open_calc_window)

        self.calc_window = None

    def open_calc_window(self):
        if self.calc_window is None:
            self.calc_window = CalcWindow(self)
            self.calc_window.okClicked.connect(self.run_calc)

        self.calc_window.show()
        self.calc_window.raise_()
        self.calc_window.activateWindow()

    def run_calc(self):
        result = calc()
        print(f"calc() 결과: {result}")
