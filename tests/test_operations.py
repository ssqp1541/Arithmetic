"""
Operation 클래스들에 대한 테스트
"""

import pytest
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from operations import (
    Operation,
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    DivideQuotientOperation,
    OperationFactory,
)


class TestAddOperation:
    """AddOperation 테스트"""
    
    def test_add_positive_numbers(self):
        """양수 덧셈 테스트"""
        operation = AddOperation()
        result = operation.execute(1, 10)
        assert result == 11
        assert operation.get_symbol() == '+'
    
    def test_add_zero_and_positive(self):
        """0과 양수 덧셈 테스트"""
        operation = AddOperation()
        result = operation.execute(0, 1)
        assert result == 1
    
    def test_add_negative_numbers(self):
        """음수 덧셈 테스트"""
        operation = AddOperation()
        result = operation.execute(-1, -10)
        assert result == -11


class TestSubtractOperation:
    """SubtractOperation 테스트"""
    
    def test_subtract_positive_numbers(self):
        """양수 뺄셈 테스트"""
        operation = SubtractOperation()
        result = operation.execute(5, 2)
        assert result == 3
        assert operation.get_symbol() == '-'


class TestMultiplyOperation:
    """MultiplyOperation 테스트"""
    
    def test_multiply_negative_numbers(self):
        """음수 곱셈 테스트"""
        operation = MultiplyOperation()
        result = operation.execute(-5, -3)
        assert result == 15
        assert operation.get_symbol() == '*'
    
    def test_multiply_with_zero(self):
        """0 곱셈 테스트"""
        operation = MultiplyOperation()
        result = operation.execute(0, 10)
        assert result == 0


class TestDivideOperation:
    """DivideOperation 테스트"""
    
    def test_divide_integer_division(self):
        """정수 나눗셈 테스트"""
        operation = DivideOperation()
        result = operation.execute(5, 2)
        assert result == 2
        assert operation.get_symbol() == '/'
    
    def test_divide_negative_dividend(self):
        """음수 피제수 나눗셈 테스트"""
        operation = DivideOperation()
        result = operation.execute(-10, 2)
        assert result == -5
    
    def test_divide_by_zero_throws_exception(self):
        """0으로 나누기 예외 테스트"""
        operation = DivideOperation()
        with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
            operation.execute(5, 0)
    
    def test_divide_zero_by_zero_throws_exception(self):
        """0을 0으로 나누기 예외 테스트"""
        operation = DivideOperation()
        with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
            operation.execute(0, 0)


class TestDivideQuotientOperation:
    """DivideQuotientOperation 테스트"""
    
    def test_divide_quotient_decimal_division(self):
        """소수점 나눗셈 테스트"""
        operation = DivideQuotientOperation()
        result = operation.execute(5, 2)
        assert result == 2.5
        assert operation.get_symbol() == '÷'
    
    def test_divide_quotient_by_zero_throws_exception(self):
        """0으로 나누기 예외 테스트"""
        operation = DivideQuotientOperation()
        with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
            operation.execute(5, 0)


class TestOperationFactory:
    """OperationFactory 테스트"""
    
    def test_create_add_operation(self):
        """덧셈 연산 생성 테스트"""
        operation = OperationFactory.create('+')
        assert isinstance(operation, AddOperation)
        assert operation.execute(1, 2) == 3
    
    def test_create_subtract_operation(self):
        """뺄셈 연산 생성 테스트"""
        operation = OperationFactory.create('-')
        assert isinstance(operation, SubtractOperation)
        assert operation.execute(5, 2) == 3
    
    def test_create_multiply_operation(self):
        """곱셈 연산 생성 테스트"""
        operation = OperationFactory.create('*')
        assert isinstance(operation, MultiplyOperation)
        assert operation.execute(3, 4) == 12
    
    def test_create_divide_operation(self):
        """정수 나눗셈 연산 생성 테스트"""
        operation = OperationFactory.create('/')
        assert isinstance(operation, DivideOperation)
        assert operation.execute(10, 2) == 5
    
    def test_create_divide_quotient_operation(self):
        """소수점 나눗셈 연산 생성 테스트"""
        operation = OperationFactory.create('÷')
        assert isinstance(operation, DivideQuotientOperation)
        assert operation.execute(5, 2) == 2.5
    
    def test_create_invalid_operation_raises_error(self):
        """잘못된 연산자로 생성 시 예외 테스트"""
        with pytest.raises(ValueError, match="지원하지 않는 연산자"):
            OperationFactory.create('@')
    
    def test_get_supported_symbols(self):
        """지원하는 연산자 목록 테스트"""
        symbols = OperationFactory.get_supported_symbols()
        assert '+' in symbols
        assert '-' in symbols
        assert '*' in symbols
        assert '/' in symbols
        assert '÷' in symbols
    
    def test_is_supported(self):
        """연산자 지원 여부 확인 테스트"""
        assert OperationFactory.is_supported('+') is True
        assert OperationFactory.is_supported('-') is True
        assert OperationFactory.is_supported('@') is False

