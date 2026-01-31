# views/calc_basic_widget.py
# 기본 사칙연산 계산기 위젯
# 사용 예제: 숫자 입력 -> 연산자 -> 숫자 -> '=' 클릭
from PyQt5 import QtCore, QtWidgets


class CalcBasicWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()
        self._reset_state()

    def _build_ui(self):
        # UI 구성 (레이아웃 + 버튼 그리드)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        title = QtWidgets.QLabel("Basic Calculator (사칙연산)")
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        # 디스플레이: 입력/출력 표시창
        self.display = QtWidgets.QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.display.setMinimumHeight(48)
        font = self.display.font()
        font.setPointSize(font.pointSize() + 6)
        self.display.setFont(font)
        layout.addWidget(self.display)

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(6)
        layout.addLayout(grid)

        # 버튼 배치 (텍스트, row, col, rowspan?, colspan?)
        buttons = [
            ("C", 0, 0), ("⌫", 0, 1), ("±", 0, 2), ("/", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2, 1, 2),
        ]

        self._button_map = {}
        for item in buttons:
            text, row, col, *span = item
            rowspan, colspan = (span + [1, 1])[:2]
            btn = QtWidgets.QPushButton(text)
            btn.setMinimumHeight(44)
            grid.addWidget(btn, row, col, rowspan, colspan)
            self._button_map[text] = btn

        self._button_map["0"].setMinimumHeight(44)

        # 버튼 이벤트 연결
        self._button_map["C"].clicked.connect(self.clear_all)
        self._button_map["⌫"].clicked.connect(self.backspace)
        self._button_map["±"].clicked.connect(self.toggle_sign)
        self._button_map["+"].clicked.connect(lambda: self.set_operation("+"))
        self._button_map["-"].clicked.connect(lambda: self.set_operation("-"))
        self._button_map["*"].clicked.connect(lambda: self.set_operation("*"))
        self._button_map["/"].clicked.connect(lambda: self.set_operation("/"))
        self._button_map["="].clicked.connect(self.calculate)
        self._button_map["."].clicked.connect(self.input_decimal)

        for d in "0123456789":
            self._button_map[d].clicked.connect(lambda _, x=d: self.input_digit(x))

    def _reset_state(self):
        # 내부 상태 초기화
        self._stored_value = None
        self._pending_op = None
        self._reset_display = False
        self._last_operand = None

    def _display_value(self) -> float:
        try:
            return float(self.display.text())
        except ValueError:
            return 0.0

    def _set_display(self, text: str):
        self.display.setText(text)

    def input_digit(self, digit: str):
        # 숫자 입력 처리
        if self._reset_display:
            self._set_display(digit)
            self._reset_display = False
            return
        current = self.display.text()
        if current == "0":
            self._set_display(digit)
        else:
            self._set_display(current + digit)

    def input_decimal(self):
        # 소수점 입력 처리
        if self._reset_display:
            self._set_display("0.")
            self._reset_display = False
            return
        if "." not in self.display.text():
            self._set_display(self.display.text() + ".")

    def clear_all(self):
        # 전체 초기화
        self._reset_state()
        self._set_display("0")

    def backspace(self):
        # 한 글자 삭제
        if self._reset_display:
            self._set_display("0")
            self._reset_display = False
            return
        text = self.display.text()
        if len(text) <= 1:
            self._set_display("0")
        else:
            self._set_display(text[:-1])

    def toggle_sign(self):
        # 부호 토글
        text = self.display.text()
        if text.startswith("-"):
            self._set_display(text[1:])
        elif text != "0":
            self._set_display("-" + text)

    def set_operation(self, op: str):
        # 연산자 입력 시 중간 계산
        current = self._display_value()
        if self._pending_op is not None and not self._reset_display:
            self._stored_value = self._apply_op(self._stored_value, current, self._pending_op)
            self._set_display(self._format_number(self._stored_value))
        else:
            self._stored_value = current
        self._pending_op = op
        self._reset_display = True

    def calculate(self):
        # '=' 계산
        if self._pending_op is None:
            return
        current = self._display_value()
        if self._reset_display and self._last_operand is not None:
            current = self._last_operand
        result = self._apply_op(self._stored_value, current, self._pending_op)
        self._set_display(self._format_number(result))
        self._stored_value = result
        self._last_operand = current
        self._reset_display = True

    def _apply_op(self, a: float, b: float, op: str) -> float:
        # 실제 사칙연산 수행
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                return 0.0
            return a / b
        return b

    def _format_number(self, value: float) -> str:
        # 정수는 소수점 없이 표시
        if value.is_integer():
            return str(int(value))
        return str(value)
