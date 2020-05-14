from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from TUBES.View.Asset.Font import *
from TUBES.View.reuse.my_customize import myLabel, myBtn, myLineEdit, twoWidLayout
from TUBES.Model.base import *
from TUBES.Model.ORM_akun import Akun


class Login(QWidget):
    def __init__(self):
        super(Login,self).__init__()

        self.lbl_wel = myLabel('SELAMAT DATANG', font_jdl)
        self.lbl_dlg = myLabel('Silahkan Login dulu!', font_dlg)

        self.lename = myLineEdit('Masukkan Username',auto=False,w=600)
        self.lepass = myLineEdit('Masukkan Password',auto=False,w=600)
        self.lepass.setEchoMode(QLineEdit.Password)

        self.btn_login = myBtn('Log in', self.login)
        self.btn_back = myBtn('Back', self.back)

        self.flay = QFormLayout()

        vb = QVBoxLayout()
        vb.addWidget(self.lbl_wel, alignment=Qt.AlignHCenter)
        vb.addWidget(self.lbl_dlg, alignment=Qt.AlignHCenter)
        vb.addSpacing(20)
        self.flay.addRow(vb)

        vb3 = twoWidLayout(self.lename, self.lepass)
        vb2 = twoWidLayout(self.btn_login, self.btn_back)
        self.flay.addRow(vb3)
        self.flay.addRow(vb2)

        self.flay.setFormAlignment(Qt.AlignVCenter)
        self.flay.setHorizontalSpacing(15)
        self.flay.setSpacing(10)
        self.setLayout(self.flay)

    def login(self):
        msg = QMessageBox()
        query = Akun.all()
        ada = False
        for row in query:
            if self.lename.text() == row.username:
                ada = True
                if self.lepass.text() == row.password:
                    if row.job == 'Kasir':
                        from TUBES.View.kasirGUI import KasirGUI
                        x = KasirGUI(row.username)
                    elif row.job == 'Pelayan':
                        from TUBES.View.pelayanGUI import PelayanGUI
                        x = PelayanGUI(row.username)
                    else:
                        from TUBES.View.penjualGUI import PenjualGUI
                        x = PenjualGUI(row.username)
                    self.parent().setCentralWidget(x)

                else:
                    msg.setWindowTitle("Stop it, get some help")
                    msg.setText('Password salah')
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break

        if not ada:
            msg.setWindowTitle("Stop it, get some help")
            msg.setText('Username Tidak ditemukan')
            # msg.setWindowIcon()
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def back(self):
        from TUBES.View.welcome import Welcome
        welcome = Welcome()
        self.parent().setCentralWidget(welcome)
