# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 읽기 전용 설정

        self.btn1 = QPushButton('Message', self) # 버튼 추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭 시 activateMessage 메소드 호출

        self.btn2 = QPushButton('Clear', self) # 버튼2 추가
        self.btn2.clicked.connect(self.clearMessage) # 버튼 클릭 시 clearMessage 메소드 호출

        hbox = QHBoxLayout() # 수평 박스 레이아웃
        hbox.addStretch(1) # 빈 공간
        hbox.addWidget(self.btn1) # 버튼 1 위치
        hbox.addWidget(self.btn2) # 버튼 2 위치

        vbox = QVBoxLayout() # 수직 박스 레이아웃
        vbox.addWidget(self.te1) # 텍스트 에디트 위치
        # vbox.addWidget(self.btn1) # 버튼 위치
        vbox.addLayout(hbox) # 버튼1 위치에 수평 박스 레이아웃 추가
        vbox.addStretch(1) # 빈 공간

        self.setLayout(vbox) # 위대로 레이아웃 설정

        self.setWindowTitle('Calculator') 
        self.setWindowIcon(QIcon('icon.png')) # 아이콘 추가
        self.resize(256, 256)
        self.show()
    
    def activateMessage(self): # 버튼 클릭 시 호출되는 메소드 : 텍스트 에디트에 메시지 출력
        # QMessageBox.information(self, 'Information', 'Button clicked!') # 메시지 박스
        self.te1.appendPlainText('Button clicked!')
    
    def clearMessage(self): # 버튼 클릭 시 호출되는 메소드 : 텍스트 에디트 내용 삭제
        self.te1.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())