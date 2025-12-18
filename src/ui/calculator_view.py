"""
CalculatorView 클래스
PyQt를 사용한 계산기 UI 클래스
MVC 패턴의 View 역할
"""

from PyQt6.QtWidgets import (
    QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class CalculatorView(QWidget):
    """계산기 UI 클래스
    
    이미지에 표시된 레이아웃을 구현합니다.
    """
    
    # 시그널 정의
    button_clicked = pyqtSignal(str)  # 버튼 클릭 시그널
    
    def __init__(self, parent=None):
        """CalculatorView 인스턴스 생성
        
        Args:
            parent: 부모 위젯
        """
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        """UI 초기화"""
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # 디스플레이 (읽기 전용)
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", 20))
        self.display.setText("0")
        self.display.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 10px;
            }
        """)
        main_layout.addWidget(self.display)
        
        # 버튼 그리드 레이아웃
        button_layout = QGridLayout()
        button_layout.setSpacing(5)
        
        # 버튼 정의 (이미지 레이아웃에 맞춤)
        buttons = [
            # Row 1: %, CE, C, ⌫
            ['%', 'CE', 'C', '⌫'],
            # Row 2: 1/x, x², ²√x, ÷
            ['1/x', 'x²', '²√x', '÷'],
            # Row 3: 7, 8, 9, ×
            ['7', '8', '9', '×'],
            # Row 4: 4, 5, 6, −
            ['4', '5', '6', '−'],
            # Row 5: 1, 2, 3, +
            ['1', '2', '3', '+'],
            # Row 6: +/-, 0, ., =
            ['+/-', '0', '.', '='],
        ]
        
        # 버튼 생성 및 배치
        for row, button_row in enumerate(buttons):
            for col, button_text in enumerate(button_row):
                button = self.create_button(button_text)
                button_layout.addWidget(button, row, col)
        
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        
        # 윈도우 설정
        self.setWindowTitle("계산기")
        self.setFixedSize(300, 400)
    
    def create_button(self, text: str) -> QPushButton:
        """버튼을 생성하고 이벤트를 연결합니다.
        
        Args:
            text: 버튼 텍스트
            
        Returns:
            생성된 QPushButton
        """
        button = QPushButton(text)
        button.setFont(QFont("Arial", 14))
        button.setMinimumHeight(50)
        
        # = 버튼은 파란색으로 스타일링
        if text == '=':
            button.setStyleSheet("""
                QPushButton {
                    background-color: #0078d4;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #005a9e;
                }
                QPushButton:pressed {
                    background-color: #004578;
                }
            """)
        else:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #e0e0e0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #d0d0d0;
                }
                QPushButton:pressed {
                    background-color: #c0c0c0;
                }
            """)
        
        # 클릭 이벤트 연결
        button.clicked.connect(lambda checked, t=text: self.on_button_clicked(t))
        
        return button
    
    def on_button_clicked(self, text: str):
        """버튼 클릭 핸들러
        
        Args:
            text: 클릭된 버튼의 텍스트
        """
        self.button_clicked.emit(text)
    
    def set_display(self, value: str):
        """디스플레이 값을 설정합니다.
        
        Args:
            value: 표시할 값
        """
        self.display.setText(value)
    
    def get_display(self) -> str:
        """디스플레이 값을 가져옵니다.
        
        Returns:
            현재 디스플레이 값
        """
        return self.display.text()

