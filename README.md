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

1. **RED**: 실패하는 테스트를 먼저 작성  - ✅ 완료
2. **GREEN**: 테스트를 통과하는 최소한의 코드 작성 - ⏳ 진행 예정
3. **REFACTOR**: 코드를 개선하고 리팩토링

### GREEN 단계 구현 목록

#### 기능 요구사항 (Functional Requirements)

1. **ArithmeticCalculator 클래스 구현**
   - 위치: `src/arithmetic/arithmetic_calculator.py`
   - 사칙연산을 수행하는 메인 클래스

2. **덧셈 기능 (add 메서드)** - 우선순위: 높음
   - 메서드 시그니처: `add(a: int, b: int) -> int`
   - 처리 케이스:
     - 양수 + 양수: `1 + 10 = 11`
     - 0 + 양수: `0 + 1 = 1`
     - 음수 + 음수: `-1 + (-10) = -11`

3. **뺄셈 기능 (subtract 메서드)** - 우선순위: 높음
   - 메서드 시그니처: `subtract(a: int, b: int) -> int`
   - 처리 케이스:
     - 양수 - 양수: `5 - 2 = 3`

4. **곱셈 기능 (multiply 메서드)** - 우선순위: 중간
   - 메서드 시그니처: `multiply(a: int, b: int) -> int`
   - 처리 케이스:
     - 음수 × 음수: `-5 * -3 = 15`
     - 0 × 양수: `0 * 10 = 0`

5. **정수 나눗셈 기능 (divide 메서드)** - 우선순위: 높음
   - 메서드 시그니처: `divide(a: int, b: int) -> int`
   - 처리 케이스:
     - 정수 나눗셈: `5 / 2 = 2` (정수 몫 반환)
     - 음수 피제수: `-10 / 2 = -5`

6. **소수점 나눗셈 기능 (divide_quotient 메서드)** - 우선순위: 중간
   - 메서드 시그니처: `divide_quotient(a: int, b: int) -> float`
   - 처리 케이스:
     - 소수점 나눗셈: `5 ÷ 2 = 2.5` (부동소수점 결과 반환)

#### 비기능 요구사항 (Non-Functional Requirements)

1. **예외 처리 (Exception Handling)** - 우선순위: 높음
   - 요구사항: 0으로 나누기 시 `ZeroDivisionError` 예외 발생
   - 적용 메서드: `divide()`, `divide_quotient()`
   - 테스트 케이스:
     - `0 / 0` → `ZeroDivisionError`
     - `5 / 0` → `ZeroDivisionError`

2. **정확도 (Accuracy)** - 우선순위: 중간
   - 요구사항: 소수점 나눗셈 결과의 정확도 보장
   - 검증 기준: `abs(result - expected) < 0.0001`
   - 적용 메서드: `divide_quotient()`

3. **테스트 커버리지 (Test Coverage)** - 우선순위: 높음
   - 목표: 100% 커버리지
   - 범위: 모든 메서드와 예외 케이스 포함

4. **코드 품질 (Code Quality)**
   - 요구사항: Given-When-Then 패턴 준수
   - 모듈 구조: `arithmetic.arithmetic_calculator` 모듈로 import 가능해야 함

#### 구현 체크리스트

- [ ] `src/arithmetic/arithmetic_calculator.py` 파일 생성
- [ ] `ArithmeticCalculator` 클래스 정의
- [ ] `add(a, b)` 메서드 구현
- [ ] `subtract(a, b)` 메서드 구현
- [ ] `multiply(a, b)` 메서드 구현
- [ ] `divide(a, b)` 메서드 구현 (정수 나눗셈)
- [ ] `divide_quotient(a, b)` 메서드 구현 (소수점 나눗셈)
- [ ] 0으로 나누기 예외 처리 (`ZeroDivisionError`)
- [ ] 모든 테스트 통과 확인 (11개 테스트)
- [ ] 테스트 커버리지 100% 달성

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

### 모듈 실행

#### 1. 직접 실행 (실행 예제 보기)

**방법 1: 원본 파일 직접 실행**
```bash
# Windows
python src\arithmetic\arithmetic_calculator.py

# Linux/Mac
python src/arithmetic/arithmetic_calculator.py
```

**방법 2: 실행 스크립트 사용 (권장)**
```bash
# 프로젝트 루트에서 실행
python run_example.py
```

실행하면 모든 사칙연산 기능과 예외 처리 예제가 출력됩니다.

**문제 해결:**
- 출력이 보이지 않는 경우:
  1. Python 버전 확인: `python --version` (Python 3.8 이상 필요)
  2. 파일 인코딩 확인: UTF-8로 저장되어 있는지 확인
  3. 터미널 인코딩 확인: Windows에서는 `chcp 65001` 실행 후 재시도
  4. `run_example.py` 사용 (더 안정적)

#### 2. 대화형 콘솔 프로그램 실행

**간단한 사칙연산 콘솔 프로그램 (입력 받기)**

```bash
python console_calculator.py
```

실행 예시:
```
입력화면
첫번째 정수값 >>10
연산자>>+
두번째 정수값>>30

결과 뷰 화면
==============================
10+30을 계산합니다.
==============================
10+30=40입니다.
```

**지원하는 연산자:**
- `+` : 덧셈
- `-` : 뺄셈
- `*` : 곱셈
- `/` : 정수 나눗셈
- `÷` : 소수점 나눗셈

#### 3. Python 코드에서 사용하기

```python
# 모듈 import
from arithmetic.arithmetic_calculator import ArithmeticCalculator

# 계산기 인스턴스 생성
calc = ArithmeticCalculator()

# 덧셈
result = calc.add(1, 10)  # 결과: 11

# 뺄셈
result = calc.subtract(5, 2)  # 결과: 3

# 곱셈
result = calc.multiply(-5, -3)  # 결과: 15

# 정수 나눗셈
result = calc.divide(5, 2)  # 결과: 2

# 소수점 나눗셈
result = calc.divide_quotient(5, 2)  # 결과: 2.5

# 예외 처리
try:
    result = calc.divide(5, 0)
except ZeroDivisionError as e:
    print(f"에러: {e}")  # 출력: 에러: Division by zero is not allowed
```

#### 3. 대화형 Python에서 사용하기

```bash
# Python 대화형 모드 실행
python

# Python 대화형 모드에서
>>> from arithmetic.arithmetic_calculator import ArithmeticCalculator
>>> calc = ArithmeticCalculator()
>>> calc.add(1, 10)
11
>>> calc.divide_quotient(5, 2)
2.5
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
| test_subtract_positive_numbers | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_multiply_negative_numbers | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_multiply_with_zero | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_divide_integer_division | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_divide_decimal_division | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_divide_negative_dividend | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_divide_by_zero_throws_exception | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |
| test_divide_by_zero_throws_exception2 | 2025-12-16 | 실패 | ArithmeticCalculator 클래스 미구현 (의도된 상태) |

**참고**: RED 단계에서는 모든 테스트가 실패하는 것이 정상입니다. ArithmeticCalculator 클래스가 아직 구현되지 않았기 때문입니다.

## 특별 절차

1. 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다.
2. 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요.

## 작성자

- **작성자**: 홍길동
- **승인자**: 박문수
- **테스트 조직**: 개발팀

