# Arithmetic Operations - 사칙연산 모듈

## 프로젝트 개요

사칙연산 정확도를 검증하는 공통 모듈 프로젝트입니다. TDD(Test-Driven Development)의 RED-GREEN-REFACTOR 방식을 적용하여 개발합니다.

## 프로젝트 정보

- **프로젝트명**: Arithmetic
- **테스트 범위**: 공통 모듈 (Common Module / Arithmetic Operations)
- **테스트 ID**: TC-CMM-001 / TC-AO-001
- **작성일**: 2020-09-01
- **버전**: v1.0

## 테스트 환경

- **Python**: Python 3.8 이상
- **IDE**: IntelliJ IDEA 2023.2 / PyCharm / VS Code
- **운영 체제**: Windows 10
- **테스트 프레임워크**: pytest

## 전제 조건

1. Python 3.8 이상이 설치되어 있어야 합니다.
2. 모든 종속성을 올바르게 설치하고 구성해야 합니다.
3. 가상 환경(virtual environment) 사용을 권장합니다.

## 테스트 케이스

### 기본 사칙연산 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 덧셈 | 1 + 10 | 11 | 중요 | 성공 |
| 덧셈 | 0 + 1 | 1 | 중요 | 성공 |
| 덧셈 | -1 + (-10) | -11 | 보통 | 성공 |
| 뺄셈 | 5 - 2 | 3 | 중요 | 성공 |
| 곱셈 | -5 * -3 | 15 | 보통 | 성공 |
| 곱셈 | 0 * 10 | 0 | 낮음 | 성공 |
| 정수 나눗셈 | 5 / 2 | 2 | 중요 | 성공 |
| 소수점 나눗셈 | 5 ÷ 2 (quotient) | 2.5 | 보통 | 성공 |
| 나눗셈 | -10 / 2 | -5 | 중요 | 성공 |

### 예외 처리 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 0으로 나누기 | 0 / 0 | ZeroDivisionError | 중요 | 성공 |

## 개발 방법론

### RED-GREEN-REFACTOR 사이클

1. **RED**: 실패하는 테스트를 먼저 작성  - 진행 중
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성
3. **REFACTOR**: 코드를 개선하고 리팩토링

## 프로젝트 구조

```
Arithmetic/
├── src/
│   └── arithmetic/
│       ├── __init__.py
│       └── arithmetic_calculator.py
├── tests/
│   └── test_arithmetic_calculator.py
├── README.md
└── requirements.txt
```

## 설치 및 실행

### 가상 환경 설정 (권장)

```bash
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화 (Windows)
venv\Scripts\activate

# 가상 환경 활성화 (Linux/Mac)
source venv/bin/activate
```

### 의존성 설치

```bash
# 패키지 설치
pip install -r requirements.txt
```

### 테스트 실행

```bash
# 모든 테스트 실행
pytest

# 상세 출력과 함께 테스트 실행
pytest -v

# 커버리지 포함 테스트 실행
pytest --cov=src/arithmetic

# 특정 테스트 파일만 실행
pytest tests/test_arithmetic_calculator.py
```

## 성공/실패 기준

- **성공**: 모든 테스트 사례가 예상한 결과를 생성합니다.
- **실패**: 테스트 케이스가 예상한 결과를 생성하지 않습니다.

## 테스트 실행 기록

### RED 단계 테스트 실행 결과

| 테스트 함수 | 실행일 | 결과 | 비고 |
|------------|--------|------|------|
| test_add_positive_numbers | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_add_zero_and_positive | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_add_negative_numbers | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |

**참고**: RED 단계에서는 모든 테스트가 실패하는 것이 정상입니다. ArithmeticCalculator 클래스가 아직 구현되지 않았기 때문입니다.

## 특별 절차

1. 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다.
2. 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요.

## 작성자

- **작성자**: 홍길동
- **승인자**: 박문수
- **테스트 조직**: 개발팀

