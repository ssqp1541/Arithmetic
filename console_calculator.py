#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
간단한 사칙연산 콘솔 프로그램
사용자로부터 두 정수와 연산자를 입력받아 계산 결과를 출력합니다.
"""
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from arithmetic.arithmetic_calculator import ArithmeticCalculator


def get_integer_input(prompt):
    """정수 입력을 받는 함수"""
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("올바른 정수를 입력해주세요.")


def get_operator_input():
    """연산자 입력을 받는 함수"""
    valid_operators = ['+', '-', '*', '/', '÷']
    while True:
        operator = input("연산자>>")
        if operator in valid_operators:
            return operator
        else:
            print(f"올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")


def calculate(calc, a, operator, b):
    """연산을 수행하는 함수"""
    if operator == '+':
        return calc.add(a, b), f"{a}+{b}"
    elif operator == '-':
        return calc.subtract(a, b), f"{a}-{b}"
    elif operator == '*':
        return calc.multiply(a, b), f"{a}*{b}"
    elif operator == '/':
        return calc.divide(a, b), f"{a}/{b}"
    elif operator == '÷':
        return calc.divide_quotient(a, b), f"{a}÷{b}"


def main():
    """메인 함수"""
    # 출력 인코딩 설정
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 60)
    print("간단한 사칙연산 콘솔 프로그램")
    print("=" * 60)
    print()
    
    # 계산기 인스턴스 생성
    calc = ArithmeticCalculator()
    
    try:
        # 입력 화면
        print("입력화면")
        a = get_integer_input("첫번째 정수값 >>")
        operator = get_operator_input()
        b = get_integer_input("두번째 정수값 >>")
        
        print()
        
        # 결과 뷰 화면
        print("결과 뷰 화면")
        print("=" * 30)
        
        try:
            result, expression = calculate(calc, a, operator, b)
            print(f"{expression}을 계산합니다.")
            print("=" * 30)
            print(f"{expression}={result}입니다.")
        except ZeroDivisionError as e:
            print(f"{a}{operator}{b}을 계산합니다.")
            print("=" * 30)
            print(f"오류: {e}")
        
    except KeyboardInterrupt:
        print("\n\n프로그램이 종료되었습니다.")
        return 1
    except Exception as e:
        print(f"\n오류가 발생했습니다: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

