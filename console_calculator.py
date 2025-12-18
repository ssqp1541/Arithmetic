#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
간단한 사칙연산 콘솔 프로그램
사용자로부터 두 정수와 연산자를 입력받아 계산 결과를 출력합니다.

리팩토링: Controller 패턴 적용, SOLID 원칙 준수
"""
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ui.calculator_controller import CalculatorController
from operations.operation_factory import OperationFactory


def get_number_input(prompt: str) -> str:
    """숫자 입력을 받는 함수
    
    Args:
        prompt: 입력 프롬프트
        
    Returns:
        입력된 숫자 문자열
    """
    while True:
        try:
            value = input(prompt)
            # 숫자 검증 (정수 또는 소수)
            float(value)
            return value
        except ValueError:
            print("올바른 숫자를 입력해주세요.")


def get_operator_input() -> str:
    """연산자 입력을 받는 함수
    
    Returns:
        입력된 연산자 기호
    """
    valid_operators = OperationFactory.get_supported_symbols()
    while True:
        operator = input("연산자>>")
        if OperationFactory.is_supported(operator):
            return operator
        else:
            print(f"올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")


def main():
    """메인 함수"""
    # 출력 인코딩 설정
    sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 60)
    print("간단한 사칙연산 콘솔 프로그램")
    print("=" * 60)
    print()
    
    # 컨트롤러 인스턴스 생성
    controller = CalculatorController()
    
    try:
        # 입력 화면
        print("입력화면")
        a_str = get_number_input("첫번째 숫자값 >>")
        operator = get_operator_input()
        b_str = get_number_input("두번째 숫자값 >>")
        
        # 컨트롤러에 입력 설정
        controller._previous_value = a_str
        controller._current_value = b_str
        controller._operator = operator
        
        print()
        
        # 결과 뷰 화면
        print("결과 뷰 화면")
        print("=" * 30)
        
        try:
            expression = controller.get_expression()
            result = controller.calculate()
            print(f"{expression}을 계산합니다.")
            print("=" * 30)
            print(f"{expression}={result}입니다.")
        except ZeroDivisionError as e:
            expression = controller.get_expression()
            print(f"{expression}을 계산합니다.")
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

