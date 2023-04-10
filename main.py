#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random, sys

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Password Generator")
        self.setWindowIcon(QIcon(r'images/password.png'))
        self.setGeometry(650, 300, 450, 100)
        self.setMaximumWidth(450)
        self.setMaximumHeight(100)
        self.initUI()
        

    def initUI(self):
        font = QFontDatabase.addApplicationFont(r'fonts/whitrabt.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)


        inner_layout = QVBoxLayout()
        inner_layout.addStretch()
        inner_layout.addSpacing(5)

        # Text Label
        password_layout = QVBoxLayout()

        password_output = QLineEdit(self)
        password_output.setFont(QFont(families[0], 12))
        password_output.setFixedHeight(45)
        password_output.setAlignment(Qt.AlignCenter)
        
        password_layout.addWidget(password_output)

        # Button
        button_layout = QVBoxLayout()

        generate_button = QPushButton(self)
        generate_button.setIcon(QIcon(r'images/reset-password.png'))
        generate_button.setFont(QFont(families[0], 12))
        generate_button.setIconSize(QSize(30, 30))
        generate_button.setText('Generate Random Password')
        
        button_layout.addWidget(generate_button)
        
        inner_layout.setAlignment(Qt.AlignCenter)




        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(password_layout)
        main_layout.addLayout(button_layout) 
        main_layout.addStretch()
        self.setLayout(main_layout)
        self.show()





app = QApplication(sys.argv)
window = MainScreen()
window.show()
app.exec()


