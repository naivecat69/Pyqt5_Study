# views/hex_window.py
# Hex Viewer 위젯: UI 로드 후 컨트롤러 연결
# 사용 예제: "Open file" 버튼 -> 바이너리 선택 -> 덤프 표시
from PyQt5 import QtWidgets, uic
from src.hex_viewer_logic import HexViewerController


class HexViewerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Designer UI 로드
        uic.loadUi("./ui/hex_viewer.ui", self)
        # 로직 분리: 컨트롤러가 기능 담당
        self.controller = HexViewerController(self)
