"""
DivideOperation 클래스
정수 나눗셈 연산을 수행하는 Strategy 구현
"""

from typing import Union
from .operation import Operation
from arithmetic.arithmetic_calculator import ArithmeticCalculator


class DivideOperation(Operation):
    """정수 나눗셈 연산 클래스"""
    
    def __init__(self):
        """DivideOperation 인스턴스 생성"""
        self._calculator = ArithmeticCalculator()
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """두 수를 나눕니다 (정수 나눗셈).
        
        Args:
            a: 피제수 (나누어지는 수)
            b: 제수 (나누는 수)
            
        Returns:
            두 수의 몫 (정수)
            
        Raises:
            ZeroDivisionError: 제수가 0인 경우
        """
        return self._calculator.divide(int(a), int(b))
    
    def get_symbol(self) -> str:
        """나눗셈 연산자 기호를 반환합니다.
        
        Returns:
            '/'
        """
        return '/'

