"""
CalculatorWindow 클래스
계산기 메인 윈도우 클래스
View와 Controller를 연결합니다.
"""

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from .calculator_view import CalculatorView
from .calculator_controller import CalculatorController


class CalculatorWindow(QMainWindow):
    """계산기 메인 윈도우 클래스"""
    
    def __init__(self):
        """CalculatorWindow 인스턴스 생성"""
        super().__init__()
        
        # Controller와 View 생성
        self.controller = CalculatorController()
        self.view = CalculatorView()
        
        # View를 중앙 위젯으로 설정
        self.setCentralWidget(self.view)
        
        # 시그널/슬롯 연결
        self.view.button_clicked.connect(self.on_button_clicked)
        
        # 초기 디스플레이 업데이트
        self.update_display()
    
    def on_button_clicked(self, button_text: str):
        """버튼 클릭 이벤트 핸들러
        
        Args:
            button_text: 클릭된 버튼의 텍스트
        """
        try:
            # 숫자 버튼 (0-9, .)
            if button_text.isdigit() or button_text == '.':
                self.controller.input_number(button_text)
                self.update_display()
            
            # 연산자 버튼 (+, −, ×, ÷)
            elif button_text in ['+', '−', '×', '÷']:
                # PyQt 버튼 텍스트를 내부 연산자로 변환
                operator = self.convert_operator(button_text)
                result = self.controller.input_operator(operator)
                if result is not None:
                    self.update_display()
                else:
                    self.update_display()
            
            # = 버튼
            elif button_text == '=':
                result = self.controller.calculate()
                self.update_display()
            
            # C (Clear) 버튼
            elif button_text == 'C':
                self.controller.clear()
                self.update_display()
            
            # CE (Clear Entry) 버튼
            elif button_text == 'CE':
                self.controller.clear_entry()
                self.update_display()
            
            # ⌫ (Backspace) 버튼
            elif button_text == '⌫':
                self.controller.backspace()
                self.update_display()
            
            # +/- (Sign Change) 버튼
            elif button_text == '+/-':
                self.controller.change_sign()
                self.update_display()
            
            # 고급 기능 (%, 1/x, x², ²√x) - Phase 4에서 구현 예정
            elif button_text in ['%', '1/x', 'x²', '²√x']:
                self.show_not_implemented_message(button_text)
        
        except ZeroDivisionError as e:
            QMessageBox.warning(self, "오류", f"0으로 나눌 수 없습니다.\n{str(e)}")
            self.controller.clear()
            self.update_display()
        except ValueError as e:
            QMessageBox.warning(self, "오류", str(e))
            self.update_display()
        except Exception as e:
            QMessageBox.critical(self, "오류", f"예상치 못한 오류가 발생했습니다.\n{str(e)}")
    
    def convert_operator(self, button_text: str) -> str:
        """PyQt 버튼 텍스트를 내부 연산자로 변환
        
        Args:
            button_text: 버튼 텍스트
            
        Returns:
            내부 연산자 기호
        """
        conversion_map = {
            '−': '-',  # 빼기 기호
            '×': '*',  # 곱하기 기호
            '÷': '÷',  # 나누기 기호 (동일)
        }
        return conversion_map.get(button_text, button_text)
    
    def update_display(self):
        """디스플레이를 업데이트합니다."""
        value = self.controller.get_display_value()
        self.view.set_display(value)
    
    def show_not_implemented_message(self, feature: str):
        """아직 구현되지 않은 기능에 대한 메시지를 표시합니다.
        
        Args:
            feature: 기능 이름
        """
        QMessageBox.information(
            self,
            "알림",
            f"'{feature}' 기능은 Phase 4에서 구현 예정입니다."
        )

