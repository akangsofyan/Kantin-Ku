from PyQt5.QtWidgets import QPushButton

class myBtn(QPushButton):
    def __init__(self,txt,act,parent=None):
        super(myBtn,self).__init__()
        self.setText(txt)
        self.setFixedWidth(88)
        self.setStyleSheet('background-color: #6100C2; color: white')
        self.clicked.connect(act)
