# PyQt GUI 리팩토링 계획서

## 1단계: 코드스멜 분석 및 정적 분석

### 1.1 현재 코드의 문제점 분석

#### 코드스멜 (Code Smell) 발견 사항

1. **Long Method (긴 메서드)**
   - `console_calculator.py`의 `main()` 함수: 입력, 계산, 출력 로직이 모두 혼재
   - **위치**: `console_calculator.py:51-94`

2. **Magic Numbers/Strings (매직 넘버/문자열)**
   - 연산자 문자열이 하드코딩됨: `['+', '-', '*', '/', '÷']`
   - **위치**: `console_calculator.py:28`
   - **문제**: 연산자 추가 시 여러 곳 수정 필요

3. **Feature Envy (기능 질투)**
   - `calculate()` 함수가 `ArithmeticCalculator`의 메서드를 직접 호출
   - **위치**: `console_calculator.py:37-48`
   - **문제**: 연산자와 메서드 매핑이 명확하지 않음

4. **Switch Statements (스위치 문)**
   - `calculate()` 함수의 if-elif 체인
   - **위치**: `console_calculator.py:37-48`
   - **문제**: OCP 위반 (새 연산자 추가 시 수정 필요)

5. **Duplicated Code (중복 코드)**
   - `run_example.py`와 `arithmetic_calculator.py`의 `__main__` 블록에 유사한 코드
   - **위치**: 두 파일 모두

6. **Tight Coupling (강한 결합)**
   - UI 로직과 비즈니스 로직이 직접 결합
   - **위치**: `console_calculator.py` 전체

### 1.2 정적 분석 결과

#### 복잡도 분석
- **Cyclomatic Complexity**: `calculate()` 함수 = 5 (높음)
- **함수 길이**: `main()` 함수 = 44줄 (권장: 20줄 이하)

#### 의존성 분석
```
console_calculator.py
  └─> ArithmeticCalculator (직접 의존)
      └─> Python built-in (int, float)
```

#### 타입 안정성
- 타입 힌트 부족: `calculate()` 함수의 매개변수에 타입 힌트 없음
- 반환 타입 불명확: `calculate()` 함수가 튜플 반환

---

## 2단계: SOLID 원칙 적용 방안

### 2.1 Single Responsibility Principle (SRP) - 단일 책임 원칙

**현재 문제점:**
- `console_calculator.py`가 입력, 계산, 출력을 모두 담당

**개선 방안:**
```
[현재 구조]
console_calculator.py
  ├─ 입력 처리
  ├─ 계산 로직
  └─ 출력 처리

[개선 구조]
src/
  ├─ arithmetic/
  │   └─ arithmetic_calculator.py (계산 로직만)
  ├─ ui/
  │   ├─ calculator_view.py (UI 표시)
  │   └─ calculator_controller.py (입력 처리)
  └─ operations/
      └─ operation_factory.py (연산자 매핑)
```

### 2.2 Open/Closed Principle (OCP) - 개방/폐쇄 원칙

**현재 문제점:**
- 새 연산자 추가 시 `calculate()` 함수 수정 필요

**개선 방안:**
- **Strategy 패턴** 적용
- 연산 인터페이스 정의 후 각 연산을 독립적인 클래스로 구현

```python
# 개선 예시
class Operation(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> Union[int, float]:
        pass

class AddOperation(Operation):
    def execute(self, a: int, b: int) -> int:
        return a + b
```

### 2.3 Liskov Substitution Principle (LSP) - 리스코프 치환 원칙

**적용 방안:**
- 모든 연산 클래스가 `Operation` 인터페이스를 동일하게 구현
- 연산자 팩토리에서 동일한 방식으로 처리 가능

### 2.4 Interface Segregation Principle (ISP) - 인터페이스 분리 원칙

**적용 방안:**
- UI 인터페이스와 계산 인터페이스 분리
- View와 Controller 분리

### 2.5 Dependency Inversion Principle (DIP) - 의존성 역전 원칙

**현재 문제점:**
- UI가 `ArithmeticCalculator`에 직접 의존

**개선 방안:**
- 연산 인터페이스에 의존하도록 변경
- 의존성 주입(DI) 패턴 적용

---

## 3단계: 아키텍처 설계

### 3.1 계층 구조

```
┌─────────────────────────────────────┐
│         GUI Layer (PyQt)           │
│  ┌─────────────┐  ┌──────────────┐ │
│  │   View      │  │  Controller  │ │
│  │ (QWidget)   │◄─┤  (Logic)     │ │
│  └─────────────┘  └──────────────┘ │
└───────────────────┬─────────────────┘
                    │
┌───────────────────▼─────────────────┐
│      Business Logic Layer           │
│  ┌──────────────────────────────┐  │
│  │   Operation Factory          │  │
│  │   (Strategy Pattern)         │  │
│  └──────────────────────────────┘  │
│  ┌──────────────────────────────┐  │
│  │   ArithmeticCalculator       │  │
│  └──────────────────────────────┘  │
└─────────────────────────────────────┘
```

### 3.2 디자인 패턴 적용

1. **Strategy Pattern**: 연산자별 전략 클래스
2. **Factory Pattern**: 연산자에 따른 전략 생성
3. **MVC Pattern**: Model-View-Controller 분리
4. **Observer Pattern**: 계산 결과 업데이트 (PyQt 시그널/슬롯)

---

## 4단계: 단계별 구현 계획

### 4.1 Phase 1: 비즈니스 로직 리팩토링 (SOLID 적용)

**목표**: 연산 로직을 Strategy 패턴으로 리팩토링

**작업 내용:**
1. `src/operations/` 디렉토리 생성
2. `Operation` 추상 클래스 정의
3. 각 연산별 전략 클래스 구현:
   - `AddOperation`
   - `SubtractOperation`
   - `MultiplyOperation`
   - `DivideOperation` (정수)
   - `DivideQuotientOperation` (소수)
4. `OperationFactory` 클래스 구현
5. 기존 테스트가 통과하는지 확인

**예상 파일 구조:**
```
src/
  └─ operations/
      ├─ __init__.py
      ├─ operation.py (추상 클래스)
      ├─ add_operation.py
      ├─ subtract_operation.py
      ├─ multiply_operation.py
      ├─ divide_operation.py
      ├─ divide_quotient_operation.py
      └─ operation_factory.py
```

### 4.2 Phase 2: UI 계층 분리

**목표**: UI와 비즈니스 로직 분리

**작업 내용:**
1. `src/ui/` 디렉토리 생성
2. `CalculatorController` 클래스 구현
   - 입력 검증
   - 연산 실행
   - 예외 처리
3. 기존 콘솔 프로그램을 Controller 사용하도록 리팩토링

**예상 파일 구조:**
```
src/
  └─ ui/
      ├─ __init__.py
      └─ calculator_controller.py
```

### 4.3 Phase 3: PyQt GUI 구현

**목표**: PyQt를 사용한 GUI 구현

**작업 내용:**
1. `requirements.txt`에 PyQt6 추가
2. `CalculatorView` 클래스 구현 (QWidget 상속)
   - 디스플레이 (QLabel 또는 QLineEdit)
   - 버튼 그리드 (QGridLayout)
   - 이미지에 표시된 버튼 레이아웃 구현
3. `CalculatorWindow` 클래스 구현 (메인 윈도우)
4. 이벤트 핸들러 연결
5. Controller와 View 연결

**예상 파일 구조:**
```
src/
  └─ ui/
      ├─ calculator_view.py (PyQt 위젯)
      └─ calculator_window.py (메인 윈도우)
gui_calculator.py (진입점)
```

### 4.4 Phase 4: 고급 기능 구현

**목표**: 이미지에 표시된 고급 기능 구현

**작업 내용:**
1. **% (Percentage)**: 백분율 계산
2. **CE (Clear Entry)**: 현재 입력 초기화
3. **C (Clear)**: 전체 초기화
4. **⌫ (Backspace)**: 마지막 문자 삭제
5. **1/x (Reciprocal)**: 역수 계산
6. **x² (Square)**: 제곱 계산
7. **²√x (Square Root)**: 제곱근 계산
8. **+/- (Sign Change)**: 부호 변경

**확장성 고려:**
- 각 기능을 독립적인 Operation 클래스로 구현
- Factory에 등록하여 확장 가능하도록 설계

### 4.5 Phase 5: 테스트 및 검증

**목표**: 리팩토링 후 기능 검증

**작업 내용:**
1. 기존 단위 테스트 실행 및 통과 확인
2. 새로운 Operation 클래스에 대한 테스트 작성
3. GUI 테스트 (선택사항)
4. 코드 커버리지 확인
5. 정적 분석 도구 실행 (pylint, mypy 등)

---

## 5단계: 구현 세부사항

### 5.1 Operation 인터페이스 설계

```python
from abc import ABC, abstractmethod
from typing import Union

class Operation(ABC):
    """연산 추상 클래스"""
    
    @abstractmethod
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """연산을 수행합니다.
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            연산 결과
            
        Raises:
            ZeroDivisionError: 나눗셈에서 제수가 0인 경우
        """
        pass
    
    @abstractmethod
    def get_symbol(self) -> str:
        """연산자 기호를 반환합니다."""
        pass
```

### 5.2 Factory 패턴 구현

```python
from typing import Dict, Type
from operations.operation import Operation

class OperationFactory:
    """연산자 팩토리 클래스"""
    
    _operations: Dict[str, Type[Operation]] = {}
    
    @classmethod
    def register(cls, symbol: str, operation_class: Type[Operation]):
        """연산자를 등록합니다."""
        cls._operations[symbol] = operation_class
    
    @classmethod
    def create(cls, symbol: str) -> Operation:
        """연산자 기호로 Operation 인스턴스를 생성합니다."""
        if symbol not in cls._operations:
            raise ValueError(f"지원하지 않는 연산자: {symbol}")
        return cls._operations[symbol]()
```

### 5.3 PyQt View 설계

```python
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

class CalculatorView(QWidget):
    """계산기 UI 클래스"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """UI 초기화"""
        # 디스플레이
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        
        # 버튼 그리드
        layout = QGridLayout()
        
        # 버튼 배치 (이미지 레이아웃에 맞춤)
        # Row 1: %, CE, C, ⌫
        # Row 2: 1/x, x², ²√x, ÷
        # Row 3-5: 숫자 및 연산자
        # Row 6: +/-, 0, ., =
        
        self.setLayout(layout)
```

### 5.4 Controller 설계

```python
from typing import Optional
from operations.operation_factory import OperationFactory

class CalculatorController:
    """계산기 컨트롤러 클래스"""
    
    def __init__(self):
        self.current_value: Optional[str] = None
        self.previous_value: Optional[str] = None
        self.operator: Optional[str] = None
    
    def input_number(self, digit: str) -> str:
        """숫자 입력 처리"""
        # 구현
        pass
    
    def input_operator(self, operator: str) -> str:
        """연산자 입력 처리"""
        # 구현
        pass
    
    def calculate(self) -> str:
        """계산 수행"""
        if not all([self.previous_value, self.current_value, self.operator]):
            return self.current_value or "0"
        
        try:
            a = float(self.previous_value)
            b = float(self.current_value)
            operation = OperationFactory.create(self.operator)
            result = operation.execute(a, b)
            return str(result)
        except ZeroDivisionError as e:
            raise ValueError(str(e))
```

---

## 6단계: 마이그레이션 전략

### 6.1 점진적 리팩토링

1. **Step 1**: Operation 패턴 구현 (기존 코드 유지)
2. **Step 2**: 콘솔 프로그램을 Operation 패턴 사용하도록 변경
3. **Step 3**: PyQt GUI 구현 (Operation 패턴 재사용)
4. **Step 4**: 기존 콘솔 프로그램 제거 또는 유지 (선택)

### 6.2 하위 호환성 유지

- `ArithmeticCalculator` 클래스는 유지
- 기존 테스트는 모두 통과해야 함
- Operation 패턴은 내부적으로 `ArithmeticCalculator` 사용 가능

---

## 7단계: 체크리스트

### Phase 1: 비즈니스 로직 리팩토링
- [ ] `Operation` 추상 클래스 정의
- [ ] 각 연산 전략 클래스 구현
- [ ] `OperationFactory` 구현
- [ ] 기존 테스트 통과 확인
- [ ] 코드 커버리지 100% 유지

### Phase 2: UI 계층 분리
- [ ] `CalculatorController` 구현
- [ ] 콘솔 프로그램 리팩토링
- [ ] 테스트 통과 확인

### Phase 3: PyQt GUI 구현
- [ ] PyQt6 의존성 추가
- [ ] `CalculatorView` 구현
- [ ] 버튼 레이아웃 구현 (이미지 참조)
- [ ] 기본 사칙연산 동작 확인

### Phase 4: 고급 기능
- [ ] %, CE, C, ⌫ 구현
- [ ] 1/x, x², ²√x 구현
- [ ] +/- 구현
- [ ] 각 기능 테스트

### Phase 5: 최종 검증
- [ ] 모든 테스트 통과
- [ ] 정적 분석 통과 (pylint, mypy)
- [ ] 코드 리뷰
- [ ] 문서 업데이트

---

## 8단계: 예상 파일 구조 (최종)

```
Arithmetic/
├── src/
│   ├── arithmetic/
│   │   ├── __init__.py
│   │   └── arithmetic_calculator.py (기존 유지)
│   ├── operations/
│   │   ├── __init__.py
│   │   ├── operation.py
│   │   ├── add_operation.py
│   │   ├── subtract_operation.py
│   │   ├── multiply_operation.py
│   │   ├── divide_operation.py
│   │   ├── divide_quotient_operation.py
│   │   └── operation_factory.py
│   └── ui/
│       ├── __init__.py
│       ├── calculator_controller.py
│       ├── calculator_view.py
│       └── calculator_window.py
├── tests/
│   ├── test_arithmetic_calculator.py (기존)
│   ├── test_operations.py (신규)
│   └── test_controller.py (신규)
├── console_calculator.py (리팩토링됨)
├── gui_calculator.py (신규 - PyQt 진입점)
├── run_example.py (기존 유지)
├── requirements.txt (PyQt6 추가)
└── README.md (업데이트)
```

---

## 9단계: 품질 지표

### 코드 품질 목표
- **Cyclomatic Complexity**: 함수당 10 이하
- **함수 길이**: 20줄 이하
- **클래스 응집도**: 높음
- **결합도**: 낮음

### 테스트 목표
- **코드 커버리지**: 100%
- **단위 테스트**: 모든 Operation 클래스
- **통합 테스트**: Controller + View

### 정적 분석 목표
- **pylint**: 9.0 이상
- **mypy**: 타입 체크 통과
- **flake8**: 스타일 규칙 준수

---

## 10단계: 리스크 및 대응 방안

### 리스크
1. **PyQt 학습 곡선**: 팀원의 PyQt 경험 부족
   - **대응**: 단계별 구현, 문서화

2. **기존 테스트 실패**: 리팩토링 중 회귀 발생
   - **대응**: TDD 방식 유지, 점진적 리팩토링

3. **성능 저하**: Strategy 패턴으로 인한 오버헤드
   - **대응**: 프로파일링, 필요시 최적화

---

## 결론

이 계획서는 코드스멜 제거, SOLID 원칙 적용, 확장 가능한 아키텍처 구축을 통해 PyQt GUI로의 성공적인 리팩토링을 보장합니다. 단계별 접근을 통해 리스크를 최소화하고 품질을 유지할 수 있습니다.

