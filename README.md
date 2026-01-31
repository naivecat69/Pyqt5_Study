# PyQt5 Guide Repo

PyQt5로 GUI 기본 패턴을 학습하기 위한 가이드 프로젝트입니다.  
MainWindow에서 각 기능 위젯으로 이동하며, 버튼 클릭으로 항목별 가이드를 확인할 수 있습니다.

## 포함된 가이드
1. 계산기 (사칙연산 기본형)
2. Hex Viewer (Wireshark 스타일 hex view)
3. 계산기2 (pyuic로 변환된 .py UI 사용)
4. 그래프 전시 (바이너리 파일 시각화 + FFT)
5. Base64 Tool (팝업 위젯)

## 실행
```bash
python main.py
```

## 문서
- `docs/main_window.md`
- `docs/calc_basic.md`
- `docs/hex_viewer.md`
- `docs/calc2_pyuic.md`
- `docs/graph_fft.md`
- `docs/base64_tool.md`

## 구조
```
project/
├─ main.py
├─ ui/
│   ├─ main.ui
│   ├─ hex_viewer.ui
│   ├─ calc2.ui
│   └─ calc2_ui.py   # pyuic로 생성된 UI (예시)
├─ views/
│   ├─ main_window.py
│   ├─ calc_basic_widget.py
│   ├─ hex_window.py
│   ├─ calc2_window.py
│   ├─ graph_window.py
│   └─ b64_window.py
├─ src/
│   └─ hex_viewer_logic.py
└─ docs/
    ├─ main_window.md
    ├─ calc_basic.md
    ├─ hex_viewer.md
    ├─ calc2_pyuic.md
    ├─ graph_fft.md
    └─ base64_tool.md
```

## 참고
- 그래프 전시는 `matplotlib`, `numpy`가 필요합니다.
