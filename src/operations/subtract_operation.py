"""
SubtractOperation 클래스
뺄셈 연산을 수행하는 Strategy 구현
"""

from typing import Union
from .operation import Operation
from arithmetic.arithmetic_calculator import ArithmeticCalculator


class SubtractOperation(Operation):
    """뺄셈 연산 클래스"""
    
    def __init__(self):
        """SubtractOperation 인스턴스 생성"""
        self._calculator = ArithmeticCalculator()
    
    def execute(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """두 수를 뺍니다.
        
        Args:
            a: 피감수 (빼어지는 수)
            b: 감수 (빼는 수)
            
        Returns:
            두 수의 차
        """
        return self._calculator.subtract(int(a), int(b))
    
    def get_symbol(self) -> str:
        """뺄셈 연산자 기호를 반환합니다.
        
        Returns:
            '-'
        """
        return '-'

