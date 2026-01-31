# views/main_window.py
from PyQt5 import QtWidgets, uic
from views.calc_basic_widget import CalcBasicWidget
from views.calc2_window import Calc2Widget
from views.hex_window import HexViewerWidget
from views.graph_window import GraphViewerWidget
from views.b64_window import Base64Dialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/main.ui", self)

        self._build_pages()
        self._wire_nav()

        self._set_page("calc1")
        self._b64_dialog = None

    def _build_pages(self):
        self._pages = {
            "calc1": CalcBasicWidget(self),
            "hex": HexViewerWidget(self),
            "calc2": Calc2Widget(self),
            "graph": GraphViewerWidget(self),
        }
        for page in self._pages.values():
            self.stackedWidget.addWidget(page)

    def _wire_nav(self):
        self.btn_calc1.clicked.connect(lambda: self._set_page("calc1"))
        self.btn_hex.clicked.connect(lambda: self._set_page("hex"))
        self.btn_calc2.clicked.connect(lambda: self._set_page("calc2"))
        self.btn_graph.clicked.connect(lambda: self._set_page("graph"))
        self.btn_b64.clicked.connect(self._open_b64_dialog)

    def _set_page(self, key: str):
        page = self._pages.get(key)
        if page is None:
            return
        self.stackedWidget.setCurrentWidget(page)

    def _open_b64_dialog(self):
        if self._b64_dialog is None:
            self._b64_dialog = Base64Dialog(self)
        self._b64_dialog.show()
        self._b64_dialog.raise_()
        self._b64_dialog.activateWindow()
