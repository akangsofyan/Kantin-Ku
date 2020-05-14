from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from TUBES.View.Asset.Font import *
from TUBES.View.reuse.my_customize import myLabel,myBtn,myLineEdit,twoWidLayout
from TUBES.Model.ORM_admin import Admin
from TUBES.Model.base import *

# Admin1 = Admin('Taukhid','masuk123')

class Admin_login(QWidget):
    def __init__(self):
        super(Admin_login,self).__init__()

        self.lename = myLineEdit('Masukkan Username',auto=False,w=600)
        self.lepass = myLineEdit('Masukkan Password',auto=False,w=600)
        self.lepass.setEchoMode(QLineEdit.Password)

        self.btn_login = myBtn('Log in',self.login)
        self.btn_back = myBtn('Back',self.back)

        self.lbl_wel = myLabel('WELCOME ADMIN',font_jdl)
        self.lbl_dlg = myLabel('Log in sebagai Admin',font_dlg)

        self.flay = QFormLayout()

        vb = QVBoxLayout()
        vb.addWidget(self.lbl_wel,alignment=Qt.AlignCenter)
        vb.addWidget(self.lbl_dlg,alignment=Qt.AlignCenter)
        vb.addSpacing(20)
        self.flay.addRow(vb)

        vb3 = twoWidLayout(self.lename, self.lepass)
        self.flay.addRow(vb3)

        vb2 = twoWidLayout(self.btn_login, self.btn_back)
        self.flay.addRow(vb2)

        self.flay.setFormAlignment(Qt.AlignVCenter)
        self.flay.setHorizontalSpacing(15)
        self.flay.setSpacing(10)
        self.setLayout(self.flay)

    def login(self):
        msg = QMessageBox()
        query = Admin.all()
        ada = False
        for row in query:
            if self.lename.text() == row.nama:
                ada = True
                if self.lepass.text() == row.pw:
                        from TUBES.View.adminGUI import AdminGUI
                        admin = AdminGUI(row.nama)
                        self.parent().setCentralWidget(admin)
                else:
                    msg.setWindowTitle("Stop it, get some help")
                    msg.setText('Password salah')
                    # msg.setWindowIcon()
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    break

        if not ada:
            msg.setWindowTitle("Stop it, get some help")
            msg.setText('Username Tidak ditemukan')
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def back(self):
        from TUBES.View.welcome import Welcome
        welcome = Welcome()
        self.parent().setCentralWidget(welcome)

