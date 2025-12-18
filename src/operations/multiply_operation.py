"""
MultiplyOperation 클래스
곱셈 연산을 수행하는 Strategy 구현
"""

from typing import Union
from .operation import Operation
from arithmetic.arithmetic_calculator import ArithmeticCalculator


class MultiplyOperation(Operation):
    """곱셈 연산 클래스"""
    
    def __init__(self):
        """MultiplyOperation 인스턴스 생성"""
        self._calculator = ArithmeticCalculator()
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """두 수를 곱합니다.
        
        Args:
            a: 첫 번째 피연산자
            b: 두 번째 피연산자
            
        Returns:
            두 수의 곱
        """
        return self._calculator.multiply(int(a), int(b))
    
    def get_symbol(self) -> str:
        """곱셈 연산자 기호를 반환합니다.
        
        Returns:
            '*'
        """
        return '*'

