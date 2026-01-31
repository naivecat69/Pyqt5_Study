# 계산기 (CalcBasicWidget)

## 목적
Windows 기본 계산기와 비슷한 **사칙연산 전용** 계산기 가이드입니다.

## 구현 포인트
- `QLineEdit`를 디스플레이로 사용 (읽기 전용)
- 버튼 입력 → 숫자 조합 / 소수점 / 부호 전환 처리
- 연산자 입력 시 중간 결과를 계산하고 상태 저장
- `=` 반복 입력 시 마지막 피연산자를 재사용

## 핵심 로직
- `_stored_value`: 이전 피연산자
- `_pending_op`: 대기 중인 연산자
- `_reset_display`: 다음 입력에서 디스플레이 초기화 여부
- `_last_operand`: `=` 반복 계산용

## 관련 파일
- `views/calc_basic_widget.py`
