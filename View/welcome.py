from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from TUBES.View.Asset.Font import *
from TUBES.View.reuse.my_customize import myBtn,myLabel

class Welcome(QWidget):
    def __init__(self):
        super(Welcome,self).__init__()

        self.lbl_wel = myLabel('SELAMAT DATANG',font_jdl)
        self.lbl_dlg = myLabel('Silahkan Login/Sign up dulu!',font_dlg)

        self.btn_login = myBtn('Log in',self.login)
        self.btn_signup = myBtn('Admin Log in',self.signup)


        hb = QHBoxLayout()
        hb.addWidget(self.btn_login)
        hb.addWidget(self.btn_signup)
        hb.setSpacing(15)

        vb = QVBoxLayout()
        vb.addWidget(self.lbl_wel,alignment=Qt.AlignHCenter)
        vb.addWidget(self.lbl_dlg,alignment=Qt.AlignHCenter)
        vb.addSpacing(20)
        vb.addLayout(hb)

        self.flay = QFormLayout()
        self.flay.addRow(vb)
        self.flay.setFormAlignment(Qt.AlignCenter)
        self.flay.setSpacing(10)
        self.setLayout(self.flay)

    def login(self):
        from TUBES.View.login import Login
        loginform = Login()
        self.parent().setCentralWidget(loginform)

    def signup(self):
        from TUBES.View.admin_login import Admin_login
        admin_lgn = Admin_login()
        self.parent().setCentralWidget(admin_lgn)
