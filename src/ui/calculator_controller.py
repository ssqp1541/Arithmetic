"""
CalculatorController 클래스
계산기 비즈니스 로직을 처리하는 컨트롤러
MVC 패턴의 Controller 역할
"""

from typing import Optional, Union
from operations.operation_factory import OperationFactory


class CalculatorController:
    """계산기 컨트롤러 클래스
    
    사용자 입력을 받아 계산을 수행하고 결과를 반환합니다.
    UI와 비즈니스 로직을 분리하여 SRP를 준수합니다.
    """
    
    def __init__(self):
        """CalculatorController 인스턴스 생성"""
        self._current_value: Optional[str] = None
        self._previous_value: Optional[str] = None
        self._operator: Optional[str] = None
        self._should_reset_display: bool = False
    
    def input_number(self, digit: str) -> str:
        """숫자 입력을 처리합니다.
        
        Args:
            digit: 입력된 숫자 (0-9 또는 '.')
            
        Returns:
            현재 표시할 값
        """
        if self._should_reset_display:
            self._current_value = None
            self._should_reset_display = False
        
        if self._current_value is None:
            self._current_value = digit
        else:
            self._current_value += digit
        
        return self._current_value
    
    def input_operator(self, operator: str) -> Optional[str]:
        """연산자 입력을 처리합니다.
        
        이전 연산이 있으면 먼저 계산을 수행합니다.
        
        Args:
            operator: 연산자 기호
            
        Returns:
            계산 결과 (이전 연산이 있는 경우), None (이전 연산이 없는 경우)
            
        Raises:
            ValueError: 지원하지 않는 연산자인 경우
        """
        if not OperationFactory.is_supported(operator):
            raise ValueError(f"지원하지 않는 연산자: {operator}")
        
        result = None
        
        # 이전 연산이 있으면 먼저 계산
        if self._previous_value is not None and self._current_value is not None and self._operator is not None:
            try:
                result = self.calculate()
                self._previous_value = result
                self._current_value = None
            except (ValueError, ZeroDivisionError) as e:
                self.clear()
                raise e
        
        # 현재 값을 이전 값으로 설정 (아직 계산하지 않은 경우)
        if self._previous_value is None and self._current_value is not None:
            self._previous_value = self._current_value
            self._current_value = None
        
        self._operator = operator
        self._should_reset_display = False
        
        return result
    
    def calculate(self) -> str:
        """현재 입력된 값으로 계산을 수행합니다.
        
        Returns:
            계산 결과 문자열
            
        Raises:
            ValueError: 계산할 수 없는 상태인 경우
            ZeroDivisionError: 0으로 나누는 경우
        """
        if self._previous_value is None or self._current_value is None or self._operator is None:
            if self._current_value is not None:
                return self._current_value
            return "0"
        
        try:
            a = float(self._previous_value)
            b = float(self._current_value)
            
            operation = OperationFactory.create(self._operator)
            result = operation.execute(a, b)
            
            # 결과를 문자열로 변환 (소수점이 0이면 정수로 표시)
            if isinstance(result, float) and result.is_integer():
                result_str = str(int(result))
            else:
                result_str = str(result)
            
            # 계산 후 상태 업데이트
            self._previous_value = result_str
            self._current_value = None
            self._operator = None
            self._should_reset_display = True
            
            return result_str
            
        except ZeroDivisionError as e:
            self.clear()
            raise ZeroDivisionError(str(e))
        except ValueError as e:
            self.clear()
            raise ValueError(f"계산 오류: {str(e)}")
    
    def clear(self):
        """모든 입력을 초기화합니다."""
        self._current_value = None
        self._previous_value = None
        self._operator = None
        self._should_reset_display = False
    
    def clear_entry(self):
        """현재 입력만 초기화합니다 (CE 기능)."""
        self._current_value = None
        self._should_reset_display = False
    
    def get_display_value(self) -> str:
        """현재 표시할 값을 반환합니다.
        
        Returns:
            현재 표시할 값 (없으면 "0")
        """
        if self._current_value is not None:
            return self._current_value
        if self._previous_value is not None:
            return self._previous_value
        return "0"
    
    def get_expression(self) -> str:
        """현재 계산식 문자열을 반환합니다.
        
        Returns:
            계산식 문자열 (예: "5+3")
        """
        if self._previous_value is None:
            return ""
        
        if self._operator is None:
            return self._previous_value
        
        if self._current_value is None:
            return f"{self._previous_value}{self._operator}"
        
        return f"{self._previous_value}{self._operator}{self._current_value}"
    
    def backspace(self) -> str:
        """마지막 문자를 삭제합니다 (⌫ 기능).
        
        Returns:
            삭제 후 현재 표시할 값
        """
        if self._should_reset_display:
            return self.get_display_value()
        
        if self._current_value is not None and len(self._current_value) > 1:
            self._current_value = self._current_value[:-1]
            return self._current_value
        elif self._current_value is not None:
            self._current_value = None
            return "0"
        elif self._previous_value is not None and self._operator is None:
            if len(self._previous_value) > 1:
                self._previous_value = self._previous_value[:-1]
                return self._previous_value
            else:
                self._previous_value = None
                return "0"
        
        return "0"
    
    def change_sign(self) -> str:
        """현재 값의 부호를 변경합니다 (+/- 기능).
        
        Returns:
            부호 변경 후 현재 표시할 값
        """
        current = self.get_display_value()
        if current and current != "0":
            try:
                value = float(current)
                new_value = -value
                # 정수로 표시 가능하면 정수로
                if new_value.is_integer():
                    new_value_str = str(int(new_value))
                else:
                    new_value_str = str(new_value)
                
                # 현재 값이 있으면 현재 값 업데이트, 없으면 이전 값 업데이트
                if self._current_value is not None:
                    self._current_value = new_value_str
                elif self._previous_value is not None:
                    self._previous_value = new_value_str
                
                return new_value_str
            except ValueError:
                pass
        
        return current

