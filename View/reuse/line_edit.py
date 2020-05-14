from PyQt5.QtWidgets import QLineEdit

class myLineEdit(QLineEdit):
    def __init__(self,txt,parent=None):
        super(myLineEdit,self).__init__()
        self.setFixedHeight(30)
        self.setPlaceholderText(txt)
