# views/graph_window.py
from PyQt5 import QtCore, QtWidgets


class GraphViewerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = None
        self._path = None
        self._build_ui()

    def _build_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        title = QtWidgets.QLabel("Binary Graph Viewer + FFT")
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title)

        controls = QtWidgets.QHBoxLayout()
        layout.addLayout(controls)

        self.btn_open = QtWidgets.QPushButton("Open binary")
        self.btn_open.clicked.connect(self.open_file)
        controls.addWidget(self.btn_open)

        self.label_path = QtWidgets.QLabel("No file loaded")
        self.label_path.setMinimumWidth(240)
        controls.addWidget(self.label_path, 1)

        range_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(range_layout)

        range_layout.addWidget(QtWidgets.QLabel("Start"))
        self.spin_start = QtWidgets.QSpinBox()
        self.spin_start.setMaximum(10**9)
        range_layout.addWidget(self.spin_start)

        range_layout.addWidget(QtWidgets.QLabel("End"))
        self.spin_end = QtWidgets.QSpinBox()
        self.spin_end.setMaximum(10**9)
        range_layout.addWidget(self.spin_end)

        self.btn_apply = QtWidgets.QPushButton("Apply Range")
        self.btn_apply.clicked.connect(self.apply_range)
        range_layout.addWidget(self.btn_apply)

        self.btn_auto = QtWidgets.QPushButton("Auto Range")
        self.btn_auto.clicked.connect(self.auto_range)
        range_layout.addWidget(self.btn_auto)

        fft_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(fft_layout)

        self.chk_fft = QtWidgets.QCheckBox("Show FFT")
        self.chk_fft.setChecked(True)
        fft_layout.addWidget(self.chk_fft)

        fft_layout.addWidget(QtWidgets.QLabel("Sample rate"))
        self.spin_rate = QtWidgets.QDoubleSpinBox()
        self.spin_rate.setDecimals(4)
        self.spin_rate.setRange(0.0001, 1e9)
        self.spin_rate.setValue(1.0)
        fft_layout.addWidget(self.spin_rate)

        self.btn_fft = QtWidgets.QPushButton("Compute FFT")
        self.btn_fft.clicked.connect(self.apply_range)
        fft_layout.addWidget(self.btn_fft)
        fft_layout.addStretch(1)

        self._plot_container = QtWidgets.QWidget()
        self._plot_layout = QtWidgets.QVBoxLayout(self._plot_container)
        self._plot_layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._plot_container, 1)

        self._init_plot()

    def _init_plot(self):
        try:
            from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
            from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
            from matplotlib.figure import Figure
        except Exception:
            label = QtWidgets.QLabel("matplotlib이 필요합니다. (pip install matplotlib)")
            label.setAlignment(QtCore.Qt.AlignCenter)
            self._plot_layout.addWidget(label)
            self._canvas = None
            return

        self._figure = Figure(figsize=(5, 4))
        self._canvas = FigureCanvas(self._figure)
        self._toolbar = NavigationToolbar(self._canvas, self)
        self._plot_layout.addWidget(self._toolbar)
        self._plot_layout.addWidget(self._canvas, 1)

    def open_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open binary file",
            "",
            "All Files (*.*)"
        )
        if not path:
            return
        self._path = path
        self.label_path.setText(path)
        self._load_data(path)
        self.auto_range()

    def _load_data(self, path: str):
        import numpy as np
        try:
            with open(path, "rb") as f:
                data = f.read()
        except Exception as exc:
            QtWidgets.QMessageBox.critical(self, "Error", f"파일을 열 수 없습니다:\n{exc}")
            return
        self._data = np.frombuffer(data, dtype=np.uint8).astype(float)

    def auto_range(self):
        if self._data is None:
            return
        self.spin_start.setValue(0)
        self.spin_end.setValue(max(0, len(self._data) - 1))
        self.apply_range()

    def apply_range(self):
        if self._data is None or self._canvas is None:
            return
        start = self.spin_start.value()
        end = self.spin_end.value()
        if end <= start:
            QtWidgets.QMessageBox.warning(self, "Range error", "End는 Start보다 커야 합니다.")
            return
        end = min(end, len(self._data) - 1)
        segment = self._data[start:end + 1]
        if segment.size == 0:
            return
        self._draw_segment(segment)

    def _draw_segment(self, segment):
        import numpy as np

        self._figure.clear()
        show_fft = self.chk_fft.isChecked()
        if show_fft:
            ax1 = self._figure.add_subplot(2, 1, 1)
            ax2 = self._figure.add_subplot(2, 1, 2)
        else:
            ax1 = self._figure.add_subplot(1, 1, 1)
            ax2 = None

        max_points = 200000
        if segment.size > max_points:
            step = max(1, int(segment.size / max_points))
            segment = segment[::step]
            ax1.set_title(f"Time Domain (downsample x{step})")
        else:
            ax1.set_title("Time Domain")

        ax1.plot(segment, linewidth=0.8)
        ax1.set_xlabel("Sample")
        ax1.set_ylabel("Value")
        ax1.grid(True, alpha=0.3)

        if show_fft and ax2 is not None:
            rate = float(self.spin_rate.value())
            window = np.hanning(len(segment))
            y = (segment - np.mean(segment)) * window
            fft_vals = np.fft.rfft(y)
            mag = np.abs(fft_vals)
            freqs = np.fft.rfftfreq(len(segment), d=1.0 / rate)
            ax2.plot(freqs, mag, linewidth=0.8)
            ax2.set_title("FFT Magnitude")
            ax2.set_xlabel("Frequency")
            ax2.set_ylabel("Magnitude")
            ax2.grid(True, alpha=0.3)

        self._canvas.draw_idle()
