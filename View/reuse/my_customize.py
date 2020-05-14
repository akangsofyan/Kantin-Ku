from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QFrame
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFormLayout
from PyQt5.QtCore import Qt

class myLabel(QLabel):
    def __init__(self,txt,font,parent=None):
        super(myLabel,self).__init__()
        self.setText(txt)
        self.setFont(font)
        self.setStyleSheet('color: #6100C2')

class myFrameLabel(QLabel):
    def __init__(self,txt,font,parent=None):
        super(myFrameLabel,self).__init__()
        self.setText(txt)
        self.setFont(font)
        self.setStyleSheet('color: white')


class myBtn(QPushButton):
    def __init__(self,txt,act,parent=None):
        super(myBtn,self).__init__(parent)
        self.setText(txt)
        self.setFixedHeight(30)
        self.setFixedWidth(138)
        self.setStyleSheet('background-color: #6100C2;\
                            color: white;\
                            border-radius: 7px')
        self.clicked.connect(act)

class myFrameBtn(QPushButton):
    def __init__(self,txt,act,parent=None):
        super(myFrameBtn,self).__init__(txt,parent)
        self.setText(txt)
        self.setFixedHeight(30)
        self.setFixedWidth(110)
        self.setStyleSheet('padding: 15')
        self.setStyleSheet('background-color: white;\
                            color: #6100C2; border-radius:\
                            15px; font-weight: bold')
        self.clicked.connect(act)

class myLineEdit(QLineEdit):
    def __init__(self,txt,parent=None,auto=True,w=0):
        super(myLineEdit,self).__init__()
        self.setStyleSheet('font-size: 15pt;\
                           border-radius: 10px;\
                           border: 0.5px solid black')
        if not auto:
            self.setFixedWidth(w)
        self.setFixedHeight(40)
        self.setPlaceholderText(txt)

class twoWidLayout(QVBoxLayout):
    def __init__(self,wid,wid2,parent=None):
        super(twoWidLayout, self).__init__()
        self.addWidget(wid,alignment=Qt.AlignCenter)
        self.addWidget(wid2,alignment=Qt.AlignCenter)
        self.setSpacing(12)

class sideMenu(QFrame):
    def __init__(self,parent=None):
        super(sideMenu,self).__init__()
        self.setStyleSheet('background-color: #6100C2')
        self.setFixedHeight(506)
        self.setFixedWidth(225)
