# ch 6.3.3 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() 
        self.te1.setReadOnly(True) 

        self.btn1 = QPushButton('Calc', self) # 버튼 이름 변경
        self.btn2 = QPushButton('Clear', self) 

        self.le1 = QLineEdit('0', self) 
        self.le1.setAlignment(QtCore.Qt.AlignRight) 
        self.le1.setFocus(True) # 포커스 설정
        self.le1.selectAll() # 텍스트 전체 선택

        self.le2 = QLineEdit('0', self) 
        self.le2.setAlignment(QtCore.Qt.AlignRight) 

        self.cb = QComboBox(self) 
        self.cb.addItems(['+', '-', '*', '/']) 

        hbox_formula = QHBoxLayout() 
        hbox_formula.addWidget(self.le1)
        hbox_formula.addWidget(self.cb)
        hbox_formula.addWidget(self.le2)

        hbox = QHBoxLayout() 
        hbox.addStretch(1) 
        hbox.addWidget(self.btn1) 
        hbox.addWidget(self.btn2) 

        vbox = QVBoxLayout() 
        vbox.addWidget(self.te1) 
        vbox.addLayout(hbox_formula) 
        vbox.addLayout(hbox) 
        vbox.addStretch(1) 

        self.setLayout(vbox) 

        self.setWindowTitle('Calculator') 
        self.setWindowIcon(QIcon('icon.png')) 
        self.resize(256, 256)
        self.show()
    
    def setDisplay(self, text): # 메서드명 변경
        self.te1.appendPlainText(text)
    
    def clearMessage(self): 
        self.te1.clear()