from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFormLayout, QFrame
from PyQt5.QtCore import Qt

class twoBtnLayout(QVBoxLayout):
    def __init__(self,btn1,btn2,parent=None):
        super(twoBtnLayout,self).__init__()

        self.addWidget(btn1,alignment=Qt.AlignCenter)
        self.addWidget(btn2,alignment=Qt.AlignCenter)
        self.setSpacing(8)

class sideMenu(QFrame):
    def __init__(self,parent=None):
        super(sideMenu,self).__init__()
        self.setStyleSheet('background-color: purple')
        self.setFixedWidth(200)
        self.flay = QFormLayout()
        self.setLayout(self.flay)
