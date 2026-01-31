# Main Window (Navigation + Stacked Pages)

## 목적
MainWindow는 가이드 항목을 한 화면에서 전환하기 위한 컨테이너입니다.  
좌측 내비게이션 버튼을 누르면 우측 `QStackedWidget`에 해당 위젯이 표시됩니다.

## 구현 포인트
- `ui/main.ui`에 **좌측 버튼 영역 + 우측 QStackedWidget** 레이아웃 구성
- `views/main_window.py`에서 페이지 인스턴스를 미리 생성하고 스택에 추가
- 버튼 클릭 시 `_set_page()`로 현재 위젯 전환

## 핵심 코드 흐름
- `MainWindow.__init__()`  
  - `uic.loadUi(...)`로 UI 로드  
  - `_build_pages()`로 위젯 구성  
  - `_wire_nav()`로 버튼 연결  
  - 기본 페이지 선택

## 관련 파일
- `ui/main.ui`
- `views/main_window.py`
