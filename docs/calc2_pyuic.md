# 계산기2 (pyuic 사용)

## 목적
Designer에서 만든 `.ui` 파일을 **pyuic로 컴파일된 .py UI**로 사용하는 예시입니다.

## 구현 포인트
- `ui/calc2.ui`를 pyuic로 변환한 `ui/calc2_ui.py` 사용
- 위젯 클래스는 `Ui_Form`을 상속하여 `setupUi()`로 UI 구성
- 간단한 2-피연산자 계산 (+, -, *, /) 제공

## 핵심 로직
- 입력: `input_a`, `input_b` (`QLineEdit`)
- 출력: `label_result`
- 버튼별 연산 처리 후 결과 출력

## 관련 파일
- `ui/calc2.ui`
- `ui/calc2_ui.py`
- `views/calc2_window.py`
