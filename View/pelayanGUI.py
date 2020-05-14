from TUBES.View.reuse.my_customize import myLabel, sideMenu,myFrameBtn,myFrameLabel
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtCore import Qt
from TUBES.View.Asset.Font import *


class PelayanGUI(QWidget):
    def __init__(self,nama):
        super(PelayanGUI, self).__init__()

        vb = QVBoxLayout()

        self.lbl_kantin = myFrameLabel('Kantin ITK', font_jdl_u)
        self.lbl_nama = myFrameLabel(f'Halo, {nama}!',font_dlg)
        self.lbl = myLabel('Halo, Pelayan', font_jdl)
        self.btn = myFrameBtn('Log out', self.logout)
        # self.btn2 = myFrameBtn('Log out2', self.logout2)

        self.test = sideMenu()

        vb.addWidget(self.lbl_kantin, alignment=Qt.AlignLeft)
        vb.addWidget(self.lbl_nama, alignment=Qt.AlignLeft)
        vb.addWidget(self.btn,alignment=Qt.AlignCenter)
        # vb.addWidget(self.btn2,alignment=Qt.AlignCenter)

        flay = QFormLayout()
        flay.addRow(vb)
        flay.setFormAlignment(Qt.AlignTop)
        self.test.setLayout(flay)

        hb = QHBoxLayout()

        hb.addWidget(self.lbl, alignment=Qt.AlignLeft)
        hb.setContentsMargins(0, 0, 0, 0)

        hb.addWidget(self.test)
        self.setLayout(hb)

    def logout(self):
        from TUBES.View.login import Login
        loginform = Login()
        self.parent().setCentralWidget(loginform)
