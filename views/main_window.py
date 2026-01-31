# views/main_window.py
# MainWindow: 좌측 네비게이션 + 우측 페이지 전환용 컨테이너
# 사용 예제: 앱 실행 후 버튼을 누르면 해당 위젯이 화면에 표시됩니다.
from PyQt5 import QtWidgets, uic
from views.calc_basic_widget import CalcBasicWidget
from views.calc2_window import Calc2Widget
from views.hex_window import HexViewerWidget
from views.graph_window import GraphViewerWidget
from views.b64_window import Base64Dialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Designer로 만든 main.ui 로드
        uic.loadUi("./ui/main.ui", self)

        # 스택 페이지 구성 및 버튼 연결
        self._build_pages()
        self._wire_nav()

        # 앱 시작 시 기본 페이지
        self._set_page("calc1")
        self._b64_dialog = None

    def _build_pages(self):
        # 스택에 들어갈 위젯들을 미리 생성
        self._pages = {
            "calc1": CalcBasicWidget(self),
            "hex": HexViewerWidget(self),
            "calc2": Calc2Widget(self),
            "graph": GraphViewerWidget(self),
        }
        for page in self._pages.values():
            self.stackedWidget.addWidget(page)

    def _wire_nav(self):
        # 좌측 버튼 -> 스택 페이지 전환
        self.btn_calc1.clicked.connect(lambda: self._set_page("calc1"))
        self.btn_hex.clicked.connect(lambda: self._set_page("hex"))
        self.btn_calc2.clicked.connect(lambda: self._set_page("calc2"))
        self.btn_graph.clicked.connect(lambda: self._set_page("graph"))
        self.btn_b64.clicked.connect(self._open_b64_dialog)

    def _set_page(self, key: str):
        # key에 해당하는 위젯을 스택에서 보여줌
        page = self._pages.get(key)
        if page is None:
            return
        self.stackedWidget.setCurrentWidget(page)

    def _open_b64_dialog(self):
        # Base64는 메인 스택이 아닌 별도 팝업으로 띄움
        if self._b64_dialog is None:
            self._b64_dialog = Base64Dialog(self)
        self._b64_dialog.show()
        self._b64_dialog.raise_()
        self._b64_dialog.activateWindow()
