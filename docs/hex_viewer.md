# Hex Viewer (Wireshark 스타일)

## 목적
바이너리 파일을 열고 **헥스 + ASCII** 형태로 출력하는 가이드 위젯입니다.

## 구현 포인트
- `ui/hex_viewer.ui` 기반 위젯 로드
- 로직 분리를 위해 `HexViewerController` 사용
- 파일 열기 후 **오프셋 + 헥스 + ASCII** 출력
- 줄당 바이트 수 변경 가능 (`text_row`)
- 대용량 파일은 미리보기 제한 (기본 1MB)

## 핵심 로직
- `format_hexdump()`에서 Wireshark 스타일 포맷 생성
- `HexViewerController.open_file()`로 파일 로드
- `render_hex()`에서 헤더 + 덤프 출력

## 관련 파일
- `ui/hex_viewer.ui`
- `views/hex_window.py`
- `src/hex_viewer_logic.py`
