#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyQt GUI 계산기 프로그램
진입점 (Entry Point)
"""

import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from PyQt6.QtWidgets import QApplication
from ui.calculator_window import CalculatorWindow


def main():
    """메인 함수"""
    app = QApplication(sys.argv)
    
    # 계산기 윈도우 생성 및 표시
    window = CalculatorWindow()
    window.show()
    
    # 이벤트 루프 실행
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())

