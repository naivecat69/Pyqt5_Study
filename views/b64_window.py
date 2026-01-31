# views/b64_window.py
import base64
from PyQt5 import QtCore, QtWidgets


class Base64Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Base64 Encode / Decode")
        self.setMinimumSize(640, 420)
        self._build_ui()

    def _build_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        title = QtWidgets.QLabel("Base64 Encode / Decode")
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        self.input_text = QtWidgets.QTextEdit()
        self.input_text.setPlaceholderText("Input text here...")
        layout.addWidget(self.input_text, 1)

        button_row = QtWidgets.QHBoxLayout()
        layout.addLayout(button_row)

        self.btn_encode = QtWidgets.QPushButton("Encode →")
        self.btn_decode = QtWidgets.QPushButton("Decode →")
        self.btn_clear = QtWidgets.QPushButton("Clear")
        button_row.addWidget(self.btn_encode)
        button_row.addWidget(self.btn_decode)
        button_row.addStretch(1)
        button_row.addWidget(self.btn_clear)

        self.output_text = QtWidgets.QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Output here...")
        layout.addWidget(self.output_text, 1)

        self.btn_encode.clicked.connect(self.encode_text)
        self.btn_decode.clicked.connect(self.decode_text)
        self.btn_clear.clicked.connect(self.clear_text)

    def encode_text(self):
        raw = self.input_text.toPlainText()
        data = raw.encode("utf-8")
        encoded = base64.b64encode(data).decode("utf-8")
        self.output_text.setPlainText(encoded)

    def decode_text(self):
        raw = self.input_text.toPlainText().strip()
        try:
            decoded = base64.b64decode(raw.encode("utf-8"), validate=True).decode("utf-8")
        except Exception as exc:
            QtWidgets.QMessageBox.warning(self, "Decode error", f"Base64 디코드 실패:\n{exc}")
            return
        self.output_text.setPlainText(decoded)

    def clear_text(self):
        self.input_text.clear()
        self.output_text.clear()
