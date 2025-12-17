# GREEN 단계 최소 단위 구현 시나리오

## 개요

TDD의 GREEN 단계에서 테스트를 통과시키기 위한 최소한의 코드만 구현합니다. 각 단계마다 테스트를 실행하여 점진적으로 기능을 완성합니다.

## 구현 원칙

1. **최소 단위 구현**: 테스트를 통과시키기 위한 최소한의 코드만 작성
2. **점진적 개발**: 하나의 테스트를 통과시킨 후 다음 테스트로 진행
3. **우선순위 기반**: 중요도가 높은 기능부터 구현
4. **테스트 검증**: 각 단계마다 테스트 실행하여 검증

---

## 구현 단계별 시나리오

### Phase 1: 기본 클래스 구조 생성

**목표**: 모듈 import 오류 해결

**구현 내용**:
- `src/arithmetic/arithmetic_calculator.py` 파일 생성
- `ArithmeticCalculator` 빈 클래스 정의

**예상 결과**:
- ✅ `ModuleNotFoundError` 해결
- ❌ 모든 테스트는 여전히 실패 (메서드 미구현)

**검증 명령어**:
```bash
python -m pytest tests/test_arithmetic_calculator.py -v
```

---

### Phase 2: 덧셈 기능 구현 (우선순위: 높음)

**목표**: 덧셈 관련 3개 테스트 통과

**구현 순서**:

#### 2-1. 첫 번째 덧셈 테스트 통과
- **테스트**: `test_add_positive_numbers` (1 + 10 = 11)
- **구현**: `add(a, b)` 메서드 - 최소 구현 `return a + b`
- **검증**: 해당 테스트만 통과 확인

#### 2-2. 두 번째 덧셈 테스트 통과
- **테스트**: `test_add_zero_and_positive` (0 + 1 = 1)
- **구현**: 기존 `add` 메서드로 자동 통과 (추가 구현 불필요)
- **검증**: 덧셈 관련 2개 테스트 통과 확인

#### 2-3. 세 번째 덧셈 테스트 통과
- **테스트**: `test_add_negative_numbers` (-1 + (-10) = -11)
- **구현**: 기존 `add` 메서드로 자동 통과 (추가 구현 불필요)
- **검증**: 덧셈 관련 3개 테스트 모두 통과 확인

**최종 구현**:
```python
def add(self, a: int, b: int) -> int:
    return a + b
```

**검증 명령어**:
```bash
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_add_positive_numbers -v
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_add_zero_and_positive -v
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_add_negative_numbers -v
```

---

### Phase 3: 뺄셈 기능 구현 (우선순위: 높음)

**목표**: 뺄셈 관련 1개 테스트 통과

**구현 내용**:
- **테스트**: `test_subtract_positive_numbers` (5 - 2 = 3)
- **구현**: `subtract(a, b)` 메서드 - 최소 구현 `return a - b`

**최종 구현**:
```python
def subtract(self, a: int, b: int) -> int:
    return a - b
```

**검증 명령어**:
```bash
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_subtract_positive_numbers -v
```

---

### Phase 4: 곱셈 기능 구현 (우선순위: 중간)

**목표**: 곱셈 관련 2개 테스트 통과

**구현 순서**:

#### 4-1. 첫 번째 곱셈 테스트 통과
- **테스트**: `test_multiply_negative_numbers` (-5 * -3 = 15)
- **구현**: `multiply(a, b)` 메서드 - 최소 구현 `return a * b`
- **검증**: 해당 테스트만 통과 확인

#### 4-2. 두 번째 곱셈 테스트 통과
- **테스트**: `test_multiply_with_zero` (0 * 10 = 0)
- **구현**: 기존 `multiply` 메서드로 자동 통과 (추가 구현 불필요)
- **검증**: 곱셈 관련 2개 테스트 모두 통과 확인

**최종 구현**:
```python
def multiply(self, a: int, b: int) -> int:
    return a * b
```

**검증 명령어**:
```bash
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_multiply_negative_numbers -v
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_multiply_with_zero -v
```

---

### Phase 5: 정수 나눗셈 기능 구현 (우선순위: 높음)

**목표**: 정수 나눗셈 관련 2개 테스트 통과 (예외 처리 제외)

**구현 순서**:

#### 5-1. 첫 번째 나눗셈 테스트 통과
- **테스트**: `test_divide_integer_division` (5 / 2 = 2)
- **구현**: `divide(a, b)` 메서드 - 정수 나눗셈 `return a // b`
- **검증**: 해당 테스트만 통과 확인

#### 5-2. 두 번째 나눗셈 테스트 통과
- **테스트**: `test_divide_negative_dividend` (-10 / 2 = -5)
- **구현**: 기존 `divide` 메서드로 자동 통과 (추가 구현 불필요)
- **검증**: 정수 나눗셈 관련 2개 테스트 통과 확인

**최종 구현** (예외 처리 제외):
```python
def divide(self, a: int, b: int) -> int:
    return a // b
```

**검증 명령어**:
```bash
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_divide_integer_division -v
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_divide_negative_dividend -v
```

---

### Phase 6: 예외 처리 구현 (우선순위: 높음)

**목표**: 0으로 나누기 예외 처리 테스트 2개 통과

**구현 순서**:

#### 6-1. 첫 번째 예외 처리 테스트 통과
- **테스트**: `test_divide_by_zero_throws_exception` (0 / 0 → ZeroDivisionError)
- **구현**: `divide` 메서드에 0으로 나누기 체크 추가
- **검증**: 해당 테스트만 통과 확인

#### 6-2. 두 번째 예외 처리 테스트 통과
- **테스트**: `test_divide_by_zero_throws_exception2` (5 / 0 → ZeroDivisionError)
- **구현**: 기존 예외 처리로 자동 통과 (추가 구현 불필요)
- **검증**: 예외 처리 관련 2개 테스트 모두 통과 확인

**최종 구현**:
```python
def divide(self, a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a // b
```

**검증 명령어**:
```bash
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_divide_by_zero_throws_exception -v
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_divide_by_zero_throws_exception2 -v
```

---

### Phase 7: 소수점 나눗셈 기능 구현 (우선순위: 중간)

**목표**: 소수점 나눗셈 관련 1개 테스트 통과

**구현 내용**:
- **테스트**: `test_divide_decimal_division` (5 ÷ 2 = 2.5)
- **구현**: `divide_quotient(a, b)` 메서드 - 부동소수점 나눗셈
- **예외 처리**: 0으로 나누기 체크 포함

**최종 구현**:
```python
def divide_quotient(self, a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
```

**검증 명령어**:
```bash
python -m pytest tests/test_arithmetic_calculator.py::TestArithmeticCalculator::test_divide_decimal_division -v
```

---

## 최종 검증

### 전체 테스트 실행
```bash
# 모든 테스트 실행
python -m pytest tests/test_arithmetic_calculator.py -v

# 커버리지 포함 테스트 실행
python -m pytest tests/test_arithmetic_calculator.py --cov=src/arithmetic --cov-report=term-missing
```

### 예상 결과
- ✅ 총 11개 테스트 모두 통과
- ✅ 테스트 커버리지 100%
- ✅ 모든 기능 요구사항 충족
- ✅ 모든 비기능 요구사항 충족

---

## 구현 체크리스트

### Phase 1: 기본 구조
- [ ] `src/arithmetic/arithmetic_calculator.py` 파일 생성
- [ ] `ArithmeticCalculator` 클래스 정의

### Phase 2: 덧셈 기능
- [ ] `add(a, b)` 메서드 구현
- [ ] 덧셈 관련 3개 테스트 통과 확인

### Phase 3: 뺄셈 기능
- [ ] `subtract(a, b)` 메서드 구현
- [ ] 뺄셈 관련 1개 테스트 통과 확인

### Phase 4: 곱셈 기능
- [ ] `multiply(a, b)` 메서드 구현
- [ ] 곱셈 관련 2개 테스트 통과 확인

### Phase 5: 정수 나눗셈 기능
- [ ] `divide(a, b)` 메서드 구현 (정수 나눗셈)
- [ ] 정수 나눗셈 관련 2개 테스트 통과 확인

### Phase 6: 예외 처리
- [ ] `divide` 메서드에 0으로 나누기 예외 처리 추가
- [ ] 예외 처리 관련 2개 테스트 통과 확인

### Phase 7: 소수점 나눗셈 기능
- [ ] `divide_quotient(a, b)` 메서드 구현
- [ ] 소수점 나눗셈 관련 1개 테스트 통과 확인

### 최종 검증
- [ ] 모든 11개 테스트 통과 확인
- [ ] 테스트 커버리지 100% 달성 확인

---

## 구현 시간 예상

| Phase | 작업 내용 | 예상 시간 |
|-------|----------|----------|
| Phase 1 | 기본 클래스 구조 | 2분 |
| Phase 2 | 덧셈 기능 | 3분 |
| Phase 3 | 뺄셈 기능 | 2분 |
| Phase 4 | 곱셈 기능 | 2분 |
| Phase 5 | 정수 나눗셈 | 2분 |
| Phase 6 | 예외 처리 | 3분 |
| Phase 7 | 소수점 나눗셈 | 2분 |
| **총계** | | **약 16분** |

---

## 주의사항

1. **최소 단위 원칙**: 각 단계에서 테스트를 통과시키기 위한 최소한의 코드만 작성
2. **점진적 개발**: 한 번에 모든 기능을 구현하지 않고 단계별로 진행
3. **테스트 검증**: 각 Phase 완료 후 반드시 테스트 실행하여 검증
4. **예외 처리**: 나눗셈 메서드는 반드시 0으로 나누기 체크 포함
5. **타입 일관성**: 정수 나눗셈(`//`)과 부동소수점 나눗셈(`/`) 구분

---

## 승인 요청

이 시나리오에 대한 승인을 받은 후 구현을 진행하겠습니다.

**승인 여부**: ☐ 승인 ☐ 수정 요청

**수정 사항** (있는 경우):

