"""
Operation 추상 클래스
모든 연산의 기본 인터페이스
"""

from abc import ABC, abstractmethod
from typing import Union


class Operation(ABC):
    """연산 추상 클래스
    
    Strategy 패턴의 Strategy 인터페이스 역할
    각 연산은 이 클래스를 상속받아 구현합니다.
    """
    
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
        """연산자 기호를 반환합니다.
        
        Returns:
            연산자 기호 (예: '+', '-', '*', '/', '÷')
        """
        pass
    
    def get_display_symbol(self) -> str:
        """표시용 연산자 기호를 반환합니다.
        
        기본적으로 get_symbol()과 동일하지만,
        필요시 오버라이드하여 다른 기호를 반환할 수 있습니다.
        
        Returns:
            표시용 연산자 기호
        """
        return self.get_symbol()

