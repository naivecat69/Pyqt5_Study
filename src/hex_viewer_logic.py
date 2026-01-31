# hex_viewer_logic.py
import os
from PyQt5 import QtWidgets, QtGui


def format_hexdump(data: bytes, bytes_per_row: int = 16, base_offset: int = 0) -> str:
    bytes_per_row = max(1, int(bytes_per_row))
    lines = []

    for i in range(0, len(data), bytes_per_row):
        chunk = data[i:i + bytes_per_row]
        offset = base_offset + i

        if bytes_per_row >= 8:
            mid = bytes_per_row // 2
            left = " ".join(f"{b:02X}" for b in chunk[:mid])
            right = " ".join(f"{b:02X}" for b in chunk[mid:])
            hex_bytes = (left + "  " + right).strip()
            pad_width = bytes_per_row * 3 + 2
        else:
            hex_bytes = " ".join(f"{b:02X}" for b in chunk)
            pad_width = bytes_per_row * 3

        hex_bytes_padded = hex_bytes.ljust(pad_width)
        ascii_part = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)

        lines.append(f"{offset:08X}  {hex_bytes_padded} |{ascii_part}|")

    return "\n".join(lines)


class HexViewerController:
    """
    'Widget' 인스턴스에 붙여서 동작시키는 컨트롤러.
    widget은 다음 위젯들을 가지고 있어야 함:
      - btn_ofile
      - text_row (QLineEdit or QSpinBox)
      - btn_close
      - QTextBrowser 1개 (이름 자유 / 자동 탐색)
    """
    MAX_BYTES_DEFAULT = 1024 * 1024  # 1MB preview

    def __init__(self, widget):
        self.w = widget
        self._hex_browser = self._find_text_browser()
        if self._hex_browser is None:
            raise RuntimeError("HexViewerWidget UI에 QTextBrowser를 하나 추가해 주세요. (objectName='text_browser' 추천)")

        mono = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
        self._hex_browser.setFont(mono)
        self._hex_browser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

        self._current_path = None
        self._current_data = b""

        # connect
        self.w.btn_ofile.clicked.connect(self.open_file)
        self.w.btn_close.clicked.connect(self.close_widget)

        self._connect_row_change()

        self._hex_browser.setPlainText("파일 열기(btn_ofile)를 눌러 바이너리를 선택하세요.\n")

    def _find_text_browser(self):
        for name in ("text_browser", "textBrowser", "tb_hex", "hexBrowser"):
            w = getattr(self.w, name, None)
            if isinstance(w, QtWidgets.QTextBrowser):
                return w
        browsers = self.w.findChildren(QtWidgets.QTextBrowser)
        return browsers[0] if browsers else None

    def _connect_row_change(self):
        w = self.w.text_row
        if hasattr(w, "valueChanged"):
            w.valueChanged.connect(self._rerender_if_loaded)
            return
        if hasattr(w, "textChanged"):
            w.textChanged.connect(self._rerender_if_loaded)
            return

    def _get_bytes_per_row(self) -> int:
        w = self.w.text_row
        if hasattr(w, "value"):
            try:
                return max(1, int(w.value()))
            except Exception:
                return 16
        if hasattr(w, "text"):
            txt = (w.text() or "").strip()
            if not txt:
                return 16
            try:
                return max(1, int(txt))
            except ValueError:
                return 16
        return 16

    def _rerender_if_loaded(self, *_):
        if self._current_data:
            self.render_hex(self._current_data, self._current_path)

    def close_widget(self):
        # 메인윈도우까지 닫지 않도록 hide 권장
        self.w.hide()

    def open_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.w,
            "Open binary file",
            "",
            "All Files (*.*)"
        )
        if not path:
            return
        self._current_path = path
        self._load_and_render(path)

    def _load_and_render(self, path: str):
        try:
            total_size = os.path.getsize(path)
        except OSError:
            total_size = None

        max_bytes = self.MAX_BYTES_DEFAULT
        try:
            with open(path, "rb") as f:
                data = f.read(max_bytes + 1)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.w, "Error", f"파일을 열 수 없습니다:\n{e}")
            return

        truncated = len(data) > max_bytes
        if truncated:
            data = data[:max_bytes]

        self._current_data = data
        self.render_hex(data, path, truncated=truncated, total_size=total_size)

    def render_hex(self, data: bytes, path: str = None, truncated: bool = False, total_size: int = None):
        bpr = self._get_bytes_per_row()
        dump = format_hexdump(data, bytes_per_row=bpr, base_offset=0)

        header = []
        if path:
            header.append(f"File: {path}")
        header.append(f"Bytes shown: {len(data)} (row: {bpr})")
        if total_size is not None:
            header.append(f"Total size: {total_size}")
        if truncated:
            header.append(f"NOTE: 미리보기 제한으로 {self.MAX_BYTES_DEFAULT} bytes까지만 표시 중입니다.")
        header_text = "\n".join(header) + "\n" + ("-" * 80) + "\n"

        self._hex_browser.setPlainText(header_text + dump)
