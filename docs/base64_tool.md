# Base64 Tool (Popup)

## 목적
MainWindow 외부에서 팝업 위젯으로 동작하는 **Base64 인코딩/디코딩** 가이드입니다.

## 구현 포인트
- `QDialog`로 별도 팝업 창 제공
- 입력/출력은 각각 `QTextEdit` 사용
- Encode/Decode 버튼으로 변환
- Decode 실패 시 메시지 박스로 오류 안내

## 관련 파일
- `views/b64_window.py`
