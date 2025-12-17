"""
ArithmeticCalculator 테스트 모듈
TC-CMM-001 / TC-AO-001

RED 단계: 실패하는 테스트 작성
"""
import pytest
from arithmetic.arithmetic_calculator import ArithmeticCalculator


@pytest.fixture
def calculator():
    """ArithmeticCalculator 인스턴스를 생성하는 fixture"""
    return ArithmeticCalculator()


class TestArithmeticCalculator:
    """사칙연산 정확도 테스트 클래스"""

    def test_add_positive_numbers(self, calculator):
        """덧셈 테스트: 1 + 10 = 11"""
        # Given
        a = 1
        b = 10
        expected = 11

        # When
        result = calculator.add(a, b)

        # Then
        assert result == expected, "1 + 10은 11이어야 합니다."

    def test_add_zero_and_positive(self, calculator):
        """덧셈 테스트: 0 + 1 = 1"""
        # Given
        a = 0
        b = 1
        expected = 1

        # When
        result = calculator.add(a, b)

        # Then
        assert result == expected, "0 + 1은 1이어야 합니다."

    def test_add_negative_numbers(self, calculator):
        """덧셈 테스트: -1 + (-10) = -11"""
        # Given
        a = -1
        b = -10
        expected = -11

        # When
        result = calculator.add(a, b)

        # Then
        assert result == expected, "-1 + (-10)은 -11이어야 합니다."

    def test_subtract_positive_numbers(self, calculator):
        """뺄셈 테스트: 5 - 2 = 3"""
        # Given
        a = 5
        b = 2
        expected = 3

        # When
        result = calculator.subtract(a, b)

        # Then
        assert result == expected, "5 - 2는 3이어야 합니다."

    def test_multiply_negative_numbers(self, calculator):
        """곱셈 테스트: -5 * -3 = 15"""
        # Given
        a = -5
        b = -3
        expected = 15

        # When
        result = calculator.multiply(a, b)

        # Then
        assert result == expected, "-5 * -3은 15이어야 합니다."

    def test_multiply_with_zero(self, calculator):
        """곱셈 테스트: 0 * 10 = 0"""
        # Given
        a = 0
        b = 10
        expected = 0

        # When
        result = calculator.multiply(a, b)

        # Then
        assert result == expected, "0 * 10은 0이어야 합니다."

    def test_divide_integer_division(self, calculator):
        """정수 나눗셈 테스트: 5 / 2 = 2"""
        # Given
        a = 5
        b = 2
        expected = 2

        # When
        result = calculator.divide(a, b)

        # Then
        assert result == expected, "5 / 2는 2이어야 합니다."

    def test_divide_decimal_division(self, calculator):
        """소수점 나눗셈 테스트: 5 ÷ 2 = 2.5"""
        # Given
        a = 5
        b = 2
        expected = 2.5

        # When
        result = calculator.divide_quotient(a, b)

        # Then
        assert abs(result - expected) < 0.0001, "5 ÷ 2는 2.5이어야 합니다."

    def test_divide_negative_dividend(self, calculator):
        """나눗셈 테스트: -10 / 2 = -5"""
        # Given
        a = -10
        b = 2
        expected = -5

        # When
        result = calculator.divide(a, b)

        # Then
        assert result == expected, "-10 / 2는 -5이어야 합니다."

    def test_divide_by_zero_throws_exception(self, calculator):
        """예외 처리 테스트: 0 / 0 → ZeroDivisionError"""
        # Given
        a = 0
        b = 0

        # When & Then
        with pytest.raises(ZeroDivisionError, match=".*"):
            calculator.divide(a, b)

    def test_divide_by_zero_throws_exception2(self, calculator):
        """예외 처리 테스트: 5 / 0 → ZeroDivisionError"""
        # Given
        a = 5
        b = 0

        # When & Then
        with pytest.raises(ZeroDivisionError, match=".*"):
            calculator.divide(a, b)

    def test_divide_quotient_by_zero_throws_exception(self, calculator):
        """예외 처리 테스트: 5 / 0 (divide_quotient) → ZeroDivisionError"""
        # Given
        a = 5
        b = 0

        # When & Then
        with pytest.raises(ZeroDivisionError, match=".*"):
            calculator.divide_quotient(a, b)

    def test_divide_quotient_zero_by_zero_throws_exception(self, calculator):
        """예외 처리 테스트: 0 / 0 (divide_quotient) → ZeroDivisionError"""
        # Given
        a = 0
        b = 0

        # When & Then
        with pytest.raises(ZeroDivisionError, match=".*"):
            calculator.divide_quotient(a, b)

