# main.py
# 이 파일은 앱의 진입점입니다.
# 사용 예제: `python main.py` 실행 후 좌측 메뉴에서 가이드를 선택하세요.
import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow

def main():
    # QApplication은 모든 Qt 위젯의 이벤트 루프를 담당합니다.
    app = QApplication(sys.argv)
    # 메인 윈도우 생성
    w = MainWindow()
    w.show()
    # 이벤트 루프 시작 (종료 코드 반환)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
