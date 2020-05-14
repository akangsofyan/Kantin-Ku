import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QImage, QBrush, QPalette
from TUBES.View.welcome import Welcome


class MW(QMainWindow):
    app = QApplication(sys.argv)
    app.setStyle('fusion')

    def __init__(self):
        super(MW,self).__init__()
        self.setWindowTitle('KantinKu')
        self.resize(900,506)
        self.setContentsMargins(0,0,0,0)

        im = QImage('asset\Home900.jpg')
        pal = QPalette()
        pal.setBrush(10, QBrush(im))
        self.setPalette(pal)

        welcome = Welcome()
        self.setCentralWidget(welcome)
