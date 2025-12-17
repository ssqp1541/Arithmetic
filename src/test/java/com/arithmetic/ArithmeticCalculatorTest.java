package com.arithmetic;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

/**
 * ArithmeticCalculator 테스트 클래스
 * TC-CMM-001 / TC-AO-001
 * 
 * RED 단계: 실패하는 테스트 작성
 */
@DisplayName("사칙연산 정확도 테스트")
class ArithmeticCalculatorTest {

    private ArithmeticCalculator calculator = new ArithmeticCalculator();

    @Test
    @DisplayName("덧셈 테스트: 1 + 10 = 11")
    void testAdd_PositiveNumbers() {
        // Given
        int a = 1;
        int b = 10;
        int expected = 11;

        // When
        int result = calculator.add(a, b);

        // Then
        assertEquals(expected, result, "1 + 10은 11이어야 합니다.");
    }

    @Test
    @DisplayName("덧셈 테스트: 0 + 1 = 1")
    void testAdd_ZeroAndPositive() {
        // Given
        int a = 0;
        int b = 1;
        int expected = 1;

        // When
        int result = calculator.add(a, b);

        // Then
        assertEquals(expected, result, "0 + 1은 1이어야 합니다.");
    }

    @Test
    @DisplayName("덧셈 테스트: -1 + (-10) = -11")
    void testAdd_NegativeNumbers() {
        // Given
        int a = -1;
        int b = -10;
        int expected = -11;

        // When
        int result = calculator.add(a, b);

        // Then
        assertEquals(expected, result, "-1 + (-10)은 -11이어야 합니다.");
    }

    @Test
    @DisplayName("뺄셈 테스트: 5 - 2 = 3")
    void testSubtract_PositiveNumbers() {
        // Given
        int a = 5;
        int b = 2;
        int expected = 3;

        // When
        int result = calculator.subtract(a, b);

        // Then
        assertEquals(expected, result, "5 - 2는 3이어야 합니다.");
    }

    @Test
    @DisplayName("곱셈 테스트: -5 * -3 = 15")
    void testMultiply_NegativeNumbers() {
        // Given
        int a = -5;
        int b = -3;
        int expected = 15;

        // When
        int result = calculator.multiply(a, b);

        // Then
        assertEquals(expected, result, "-5 * -3은 15이어야 합니다.");
    }

    @Test
    @DisplayName("곱셈 테스트: 0 * 10 = 0")
    void testMultiply_WithZero() {
        // Given
        int a = 0;
        int b = 10;
        int expected = 0;

        // When
        int result = calculator.multiply(a, b);

        // Then
        assertEquals(expected, result, "0 * 10은 0이어야 합니다.");
    }

    @Test
    @DisplayName("정수 나눗셈 테스트: 5 / 2 = 2")
    void testDivide_IntegerDivision() {
        // Given
        int a = 5;
        int b = 2;
        int expected = 2;

        // When
        int result = calculator.divide(a, b);

        // Then
        assertEquals(expected, result, "5 / 2는 2이어야 합니다.");
    }

    @Test
    @DisplayName("소수점 나눗셈 테스트: 5 ÷ 2 = 2.5")
    void testDivide_DecimalDivision() {
        // Given
        int a = 5;
        int b = 2;
        double expected = 2.5;

        // When
        double result = calculator.divideQuotient(a, b);

        // Then
        assertEquals(expected, result, 0.0001, "5 ÷ 2는 2.5이어야 합니다.");
    }

    @Test
    @DisplayName("나눗셈 테스트: -10 / 2 = -5")
    void testDivide_NegativeDividend() {
        // Given
        int a = -10;
        int b = 2;
        int expected = -5;

        // When
        int result = calculator.divide(a, b);

        // Then
        assertEquals(expected, result, "-10 / 2는 -5이어야 합니다.");
    }

    @Test
    @DisplayName("예외 처리 테스트: 0 / 0 → ArithmeticException")
    void testDivide_ByZero_ThrowsException() {
        // Given
        int a = 0;
        int b = 0;

        // When & Then
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(a, b);
        }, "0 / 0은 ArithmeticException을 발생시켜야 합니다.");
    }

    @Test
    @DisplayName("예외 처리 테스트: 5 / 0 → ArithmeticException")
    void testDivide_ByZero_ThrowsException2() {
        // Given
        int a = 5;
        int b = 0;

        // When & Then
        assertThrows(ArithmeticException.class, () -> {
            calculator.divide(a, b);
        }, "5 / 0은 ArithmeticException을 발생시켜야 합니다.");
    }
}

