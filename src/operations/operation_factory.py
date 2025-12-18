"""
OperationFactory 클래스
Factory 패턴을 사용하여 연산자에 맞는 Operation 인스턴스를 생성
"""

from typing import Dict, Type, Optional
from .operation import Operation
from .add_operation import AddOperation
from .subtract_operation import SubtractOperation
from .multiply_operation import MultiplyOperation
from .divide_operation import DivideOperation
from .divide_quotient_operation import DivideQuotientOperation


class OperationFactory:
    """연산자 팩토리 클래스
    
    Factory 패턴을 사용하여 연산자 기호로 적절한 Operation 인스턴스를 생성합니다.
    OCP 원칙을 준수하여 새로운 연산자를 추가할 때 기존 코드를 수정하지 않아도 됩니다.
    """
    
    # 연산자 기호와 Operation 클래스의 매핑
    _operations: Dict[str, Type[Operation]] = {}
    
    # 기본 연산자 등록
    _initialized = False
    
    @classmethod
    def _initialize(cls):
        """기본 연산자를 등록합니다."""
        if cls._initialized:
            return
        
        cls.register('+', AddOperation)
        cls.register('-', SubtractOperation)
        cls.register('*', MultiplyOperation)
        cls.register('×', MultiplyOperation)  # 곱셈 기호 대체
        cls.register('/', DivideOperation)
        cls.register('÷', DivideQuotientOperation)
        
        cls._initialized = True
    
    @classmethod
    def register(cls, symbol: str, operation_class: Type[Operation]):
        """연산자를 등록합니다.
        
        Args:
            symbol: 연산자 기호
            operation_class: Operation 클래스
            
        Raises:
            ValueError: operation_class가 Operation을 상속하지 않는 경우
        """
        if not issubclass(operation_class, Operation):
            raise ValueError(f"{operation_class}는 Operation을 상속해야 합니다.")
        
        cls._operations[symbol] = operation_class
    
    @classmethod
    def create(cls, symbol: str) -> Operation:
        """연산자 기호로 Operation 인스턴스를 생성합니다.
        
        Args:
            symbol: 연산자 기호
            
        Returns:
            Operation 인스턴스
            
        Raises:
            ValueError: 지원하지 않는 연산자인 경우
        """
        cls._initialize()
        
        if symbol not in cls._operations:
            valid_symbols = ', '.join(cls._operations.keys())
            raise ValueError(
                f"지원하지 않는 연산자: '{symbol}'. "
                f"지원하는 연산자: {valid_symbols}"
            )
        
        return cls._operations[symbol]()
    
    @classmethod
    def get_supported_symbols(cls) -> list[str]:
        """지원하는 연산자 기호 목록을 반환합니다.
        
        Returns:
            지원하는 연산자 기호 목록
        """
        cls._initialize()
        return list(cls._operations.keys())
    
    @classmethod
    def is_supported(cls, symbol: str) -> bool:
        """연산자가 지원되는지 확인합니다.
        
        Args:
            symbol: 연산자 기호
            
        Returns:
            지원되면 True, 아니면 False
        """
        cls._initialize()
        return symbol in cls._operations

