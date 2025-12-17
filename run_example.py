#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ArithmeticCalculator 실행 예제 스크립트
프로젝트 루트에서 실행: python run_example.py
"""
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from arithmetic.arithmetic_calculator import ArithmeticCalculator

def main():
    """메인 실행 함수"""
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
    print("  divide() 메서드:")
    try:
        result = calc.divide(5, 0)
        print(f"    5 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"    5 / 0 → ZeroDivisionError: {e}")
    
    try:
        result = calc.divide(0, 0)
        print(f"    0 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"    0 / 0 → ZeroDivisionError: {e}")
    
    print("  divide_quotient() 메서드:")
    try:
        result = calc.divide_quotient(5, 0)
        print(f"    5 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"    5 / 0 → ZeroDivisionError: {e}")
    
    try:
        result = calc.divide_quotient(0, 0)
        print(f"    0 / 0 = {result}")
    except ZeroDivisionError as e:
        print(f"    0 / 0 → ZeroDivisionError: {e}")
    print()
    
    print("=" * 60)
    print("실행 완료!")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

