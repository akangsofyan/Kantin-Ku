from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtCore import Qt
from TUBES.Model.ORM_akun import Akun
from TUBES.View.reuse.my_customize import myBtn
from TUBES.Model.base import *
from TUBES.View.reuse.my_customize import myLabel, sideMenu, myFrameBtn, myFrameLabel
from TUBES.View.Asset.Font import *


class AdminGUI(QWidget):
    def __init__(self, nama):
        super(AdminGUI, self).__init__()
        self.nama = nama
        vb = QVBoxLayout()

        self.create_table()
        self.test = sideMenu()

        self.lbl_kantin = myFrameLabel('Kantin ITK', font_jdl_u)
        self.lbl_nama = myFrameLabel(f'Halo, {self.nama}!', font_dlg)

        self.btn = myFrameBtn('Log out', self.logout)
        self.btn2 = myFrameBtn('Tambah pegawai', self.tambah)
        self.btn3 = myFrameBtn('Pecat', self.pecat)

        vb.addWidget(self.lbl_kantin, alignment=Qt.AlignLeft)
        vb.addWidget(self.lbl_nama, alignment=Qt.AlignLeft)

        vb.addWidget(self.btn2, alignment=Qt.AlignCenter)
        vb.addWidget(self.btn3, alignment=Qt.AlignCenter)
        vb.addSpacing(200)
        vb.addWidget(self.btn, alignment=Qt.AlignCenter)

        flay = QFormLayout()
        flay.addRow(vb)
        flay.setFormAlignment(Qt.AlignTop)
        self.test.setLayout(flay)

        hb = QHBoxLayout()

        hb.addWidget(self.table, alignment=Qt.AlignLeft)
        hb.setContentsMargins(0, 0, 0, 0)
        # self.btn.clicked.connect()
        hb.addWidget(self.test)
        self.lastClick = None

        self.setLayout(hb)

    def create_table(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.fetchId)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Username", "Alamat", "Tanggal Lahir", "Kontak", "Job"])
        self.table_content()
        self.table.setFixedSize(614, 300)

    def fetchId(self, row):
        self.lastClick = int(self.table.item(row, 0).text())
        print(self.lastClick)

    def table_content(self):
        query = Akun.all()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row, 0, QTableWidgetItem(str(query[row].user_id)))
            self.table.setItem(row, 1, QTableWidgetItem(query[row].username))
            self.table.setItem(row, 2, QTableWidgetItem(query[row].alamat))
            self.table.setItem(row, 3, QTableWidgetItem(query[row].tgl_lahir))
            self.table.setItem(row, 4, QTableWidgetItem(query[row].kontak))
            self.table.setItem(row, 5, QTableWidgetItem(query[row].job))

    def logout(self):
        from TUBES.View.admin_login import Admin_login
        loginform = Admin_login()
        self.parent().setCentralWidget(loginform)

    def tambah(self):
        from TUBES.View.signup import Signup
        signupform = Signup(self.nama)
        self.parent().setCentralWidget(signupform)

    def pecat(self):
        if self.lastClick != None:
            Akun.delete(self.lastClick)
            self.table_content()
        else:
            pass
