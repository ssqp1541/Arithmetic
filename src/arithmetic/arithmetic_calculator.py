"""
ArithmeticCalculator 모듈
TC-CMM-001 / TC-AO-001

사칙연산을 수행하는 공통 모듈
"""


class ArithmeticCalculator:
    """사칙연산을 수행하는 계산기 클래스"""
    
    def add(self, a: int, b: int) -> int:
        """두 정수를 더하는 메서드
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            두 정수의 합
        """
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        """두 정수를 빼는 메서드
        
        Args:
            a: 피감수 (빼어지는 수)
            b: 감수 (빼는 수)
            
        Returns:
            두 정수의 차
        """
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        """두 정수를 곱하는 메서드
        
        Args:
            a: 첫 번째 정수
            b: 두 번째 정수
            
        Returns:
            두 정수의 곱
        """
        return a * b
    
    def divide(self, a: int, b: int) -> int:
        """두 정수를 나누는 메서드 (정수 나눗셈)
        
        Args:
            a: 피제수 (나누어지는 수)
            b: 제수 (나누는 수)
            
        Returns:
            두 정수의 몫 (정수)
            
        Raises:
            ZeroDivisionError: 제수가 0인 경우
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a // b
    
    def divide_quotient(self, a: int, b: int) -> float:
        """두 정수를 나누는 메서드 (소수점 나눗셈)
        
        Args:
            a: 피제수 (나누어지는 수)
            b: 제수 (나누는 수)
            
        Returns:
            두 정수의 몫 (부동소수점)
            
        Raises:
            ZeroDivisionError: 제수가 0인 경우
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b


if __name__ == "__main__":
    """실행 예제: ArithmeticCalculator 사용 예시"""
    print("=" * 60)
    print("ArithmeticCalculator - 사칙연산 계산기 실행 예제")
    print("=" * 60)
    print()
    
    # 계산기 인스턴스 생성
    calc = ArithmeticCalculator()
    
    # 덧셈 예제
    print("【 덧셈 (Addition) 】")
    print(f"  1 + 10 = {calc.add(1, 10)}")
    print(f"  0 + 1 = {calc.add(0, 1)}")
    print(f"  -1 + (-10) = {calc.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("【 뺄셈 (Subtraction) 】")
    print(f"  5 - 2 = {calc.subtract(5, 2)}")
    print()
    
    # 곱셈 예제
    print("【 곱셈 (Multiplication) 】")
    print(f"  -5 * -3 = {calc.multiply(-5, -3)}")
    print(f"  0 * 10 = {calc.multiply(0, 10)}")
    print()
    
    # 정수 나눗셈 예제
    print("【 정수 나눗셈 (Integer Division) 】")
    print(f"  5 / 2 = {calc.divide(5, 2)}")
    print(f"  -10 / 2 = {calc.divide(-10, 2)}")
    print()
    
    # 소수점 나눗셈 예제
    print("【 소수점 나눗셈 (Decimal Division) 】")
    print(f"  5 ÷ 2 = {calc.divide_quotient(5, 2)}")
    print()
    
    # 예외 처리 예제
    print("【 예외 처리 (Exception Handling) 】")
    try:
        result = calc.divide(5, 0)
        print(f"  5 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"  5 / 0 → ZeroDivisionError: {e}")
    
    try:
        result = calc.divide(0, 0)
        print(f"  0 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"  0 / 0 → ZeroDivisionError: {e}")
    print()
    
    print("=" * 60)
    print("실행 완료!")
    print("=" * 60)

