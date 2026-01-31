# views/calc2_window.py
# pyuic로 생성된 UI를 사용하는 계산기 예제
# 사용 예제: A/B 입력 후 +, -, *, / 버튼 클릭
from PyQt5 import QtWidgets
from ui.calc2_ui import Ui_Form


class Calc2Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._wire()

    def _wire(self):
        # 버튼 이벤트 연결
        self.btn_add.clicked.connect(lambda: self._calc("+"))
        self.btn_sub.clicked.connect(lambda: self._calc("-"))
        self.btn_mul.clicked.connect(lambda: self._calc("*"))
        self.btn_div.clicked.connect(lambda: self._calc("/"))
        self.btn_clear.clicked.connect(self._clear)

    def _get_inputs(self):
        # 입력값을 float로 변환 (실패 시 0.0)
        try:
            a = float(self.input_a.text().strip())
        except ValueError:
            a = 0.0
        try:
            b = float(self.input_b.text().strip())
        except ValueError:
            b = 0.0
        return a, b

    def _calc(self, op: str):
        # 사칙연산 처리
        a, b = self._get_inputs()
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = 0.0 if b == 0 else a / b
        else:
            result = 0.0
        if float(result).is_integer():
            result_text = str(int(result))
        else:
            result_text = str(result)
        self.label_result.setText(f"Result: {result_text}")

    def _clear(self):
        # 입력/출력 초기화
        self.input_a.clear()
        self.input_b.clear()
        self.label_result.setText("Result: 0")
