# PyQt5 기본 명령어 모음집

교육용 참고서 형태로 **자주 쓰는 클래스/메서드**와 **사용 예제**를 간단히 정리했습니다.

---

## 1) 앱/윈도우 기본

### QApplication / QMainWindow / QWidget
- `QApplication`: Qt 이벤트 루프 담당
- `QMainWindow`: 메뉴/툴바/상태바가 있는 메인 창
- `QWidget`: 가장 기본적인 UI 요소 (모든 위젯의 부모)

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("My App")
window.resize(800, 600)
window.show()
sys.exit(app.exec_())
```

---

## 2) 위젯 기본

### 자주 쓰는 위젯
- `QLabel`: 텍스트 표시
- `QLineEdit`: 한 줄 입력
- `QTextEdit`: 여러 줄 입력
- `QPushButton`: 버튼
- `QCheckBox`, `QRadioButton`, `QComboBox`

```python
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

root = QWidget()
layout = QVBoxLayout(root)

layout.addWidget(QLabel("이름"))
layout.addWidget(QLineEdit())
layout.addWidget(QPushButton("확인"))
```

---

## 3) 레이아웃(Layout)

### 기본 레이아웃
- `QVBoxLayout`: 세로 방향
- `QHBoxLayout`: 가로 방향
- `QGridLayout`: 격자 배치
- `QFormLayout`: 폼 형태 (라벨 + 입력)

```python
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

root = QWidget()
grid = QGridLayout(root)
grid.addWidget(QPushButton("1"), 0, 0)
grid.addWidget(QPushButton("2"), 0, 1)
grid.addWidget(QPushButton("3"), 1, 0, 1, 2)  # row=1, col=0, rowSpan=1, colSpan=2
```

### 여백/간격 조절
```python
layout.setContentsMargins(12, 12, 12, 12)
layout.setSpacing(8)
```

---

## 4) 시그널/슬롯 (이벤트 처리)

### 기본 개념
- **시그널**: 이벤트 발생 알림
- **슬롯**: 시그널을 받는 함수

```python
def on_click():
    print("버튼 클릭됨")

button.clicked.connect(on_click)
```

### 람다로 값 전달
```python
button.clicked.connect(lambda: print("Hello"))
```

### 사용자 정의 시그널
```python
from PyQt5 import QtCore, QtWidgets

class MyDialog(QtWidgets.QDialog):
    okClicked = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        btn = QtWidgets.QPushButton("OK", self)
        btn.clicked.connect(self.okClicked.emit)
```

---

## 5) 파일 다이얼로그

```python
from PyQt5.QtWidgets import QFileDialog

path, _ = QFileDialog.getOpenFileName(
    self, "Open file", "", "All Files (*.*)"
)
if path:
    print("선택된 파일:", path)
```

---

## 6) 메시지 박스

```python
from PyQt5.QtWidgets import QMessageBox

QMessageBox.information(self, "정보", "작업이 완료되었습니다.")
QMessageBox.warning(self, "경고", "입력 값이 올바르지 않습니다.")
QMessageBox.critical(self, "에러", "파일을 열 수 없습니다.")
```

---

## 7) QStackedWidget (화면 전환)

```python
from PyQt5.QtWidgets import QStackedWidget, QWidget

stack = QStackedWidget()
page1 = QWidget()
page2 = QWidget()
stack.addWidget(page1)
stack.addWidget(page2)

stack.setCurrentWidget(page2)  # 페이지 전환
```

---

## 8) 타이머 / 주기적 이벤트

```python
from PyQt5.QtCore import QTimer

timer = QTimer()
timer.timeout.connect(lambda: print("tick"))
timer.start(1000)  # 1초마다 실행
```

---

## 9) 스타일 적용 (간단)

```python
button.setStyleSheet("font-size: 14px; padding: 6px;")
```

---

## 10) UI 파일 로드 (uic)

```python
from PyQt5 import uic

uic.loadUi("./ui/main.ui", self)
```

---

## 11) pyuic로 변환된 UI 사용

```python
from PyQt5 import QtWidgets
from ui.calc2_ui import Ui_Form

class MyWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
```

---

## 12) 참고 팁

- 큰 데이터 렌더링 시 **다운샘플링**을 고려
- 위젯 로직은 컨트롤러로 분리하면 유지보수 쉬움
- `QTextBrowser`는 출력용, `QTextEdit`는 입력용으로 사용하면 직관적

