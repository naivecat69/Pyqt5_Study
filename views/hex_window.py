# views/hex_window.py
from PyQt5 import QtWidgets, uic
from src.hex_viewer_logic import HexViewerController


class HexViewerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("./ui/hex_viewer.ui", self)
        self.controller = HexViewerController(self)
