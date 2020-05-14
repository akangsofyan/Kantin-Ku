from PyQt5.QtWidgets import QLabel

class myLabel(QLabel):
    def __init__(self,txt,font,parent=None):
        super(myLabel,self).__init__()
        self.setText(txt)
        self.setFont(font)
        self.setStyleSheet('color: #6100C2')
