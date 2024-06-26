# ch 6.2.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 읽기 전용 설정

        self.btn1 = QPushButton('Message', self) # 버튼 추가
        self.btn2 = QPushButton('Clear', self) # 버튼2 추가

        self.le1 = QLineEdit('0', self) # 라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) # f라인 에디트1 문자열 배치 설정

        self.le2 = QLineEdit('0', self) # 라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight) # 라인 에디트2 문자열 배치 설정

        self.cb = QComboBox(self) # 콤보 박스 추가
        self.cb.addItems(['+', '-', '*', '/']) # 콤보 박스 항목 추가(연산자)

        hbox_formula = QHBoxLayout() # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formula.addWidget(self.le1)
        hbox_formula.addWidget(self.cb)
        hbox_formula.addWidget(self.le2)

        hbox = QHBoxLayout() # 수평 박스 레이아웃
        hbox.addStretch(1) # 빈 공간
        hbox.addWidget(self.btn1) # 버튼 1 위치
        hbox.addWidget(self.btn2) # 버튼 2 위치

        vbox = QVBoxLayout() # 수직 박스 레이아웃
        vbox.addWidget(self.te1) # 텍스트 에디트 위치
        vbox.addLayout(hbox_formula) # hbox_formula 배치
        vbox.addLayout(hbox) # 버튼1 위치에 수평 박스 레이아웃 추가
        vbox.addStretch(1) # 빈 공간

        self.setLayout(vbox) # 위대로 레이아웃 설정

        self.setWindowTitle('Calculator') 
        self.setWindowIcon(QIcon('icon.png')) # 아이콘 추가
        self.resize(256, 256)
        self.show()
    
    def activateMessage(self): # 버튼 클릭 시 호출되는 메소드 : 텍스트 에디트에 메시지 출력
        self.te1.appendPlainText('Button clicked!')
    
    def clearMessage(self): # 버튼 클릭 시 호출되는 메소드 : 텍스트 에디트 내용 삭제
        self.te1.clear()