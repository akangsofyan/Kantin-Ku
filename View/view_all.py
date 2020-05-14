import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from TUBES.View.Asset.Font import *
from TUBES.View.reuse.my_customize import myBtn,myLineEdit,myLabel,twoWidLayout, sideMenu
from PyQt5.QtGui import QBrush,QImage,QPalette
from TUBES.Model.ORM_akun import *
from TUBES.Class.pegawai import Pelayan,Kasir
from TUBES.Class.penjual import Penjual

class Welcome(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)

        self.lbl_wel = myLabel('SELAMAT DATANG',font_jdl)
        self.lbl_dlg = myLabel('Silahkan Login/Sign up dulu!',font_dlg)

        self.btn_login = myBtn('Log in',self.login)
        self.btn_signup = myBtn('Sign up',self.signup)

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
        loginform = Login()
        MW.central_widget.removeWidget(MW.central_widget.currentWidget())
        MW.central_widget.addWidget(loginform)

    def signup(self):
        admin_lgn = Admin_login()
        MW.central_widget.removeWidget(MW.central_widget.currentWidget())
        MW.central_widget.addWidget(admin_lgn)

class Admin_login(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.lename = myLineEdit('Masukkan Username')
        self.lepass = myLineEdit('Masukkan Password')
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

        self.flay.addRow(self.lename)
        self.flay.addRow(self.lepass)

        vb2 = twoWidLayout(self.btn_login, self.btn_back)
        self.flay.addRow(vb2)

        self.flay.setFormAlignment(Qt.AlignVCenter)
        self.flay.setHorizontalSpacing(15)
        self.setLayout(self.flay)

    def login(self):
        signupform = Signup()
        MW.central_widget.removeWidget(MW.central_widget.currentWidget())
        MW.central_widget.addWidget(signupform)

    def back(self):
        welcome = Welcome()
        MW.central_widget.removeWidget(MW.central_widget.currentWidget())
        MW.central_widget.addWidget(welcome)

class Signup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.lbl_dlg = myLabel('Silahkan isi data diri calon pegawai!',font_dlg)
        self.lename = myLineEdit('Masukkan Username')
        self.lepass = myLineEdit('Masukkan Password')
        self.lepass.setEchoMode(QLineEdit.Password)
        self.lealmt = myLineEdit('Masukkan Alamat')
        self.borndt = QDateEdit()
        self.lekntk = myLineEdit('Masukkan Kontak')
        self.lekntk.setFixedWidth(200)
        self.borndt.setCalendarPopup(True)
        self.cbx_job = QComboBox()
        self.cbx_job.addItems(['Kasir', 'Pelayan', 'Penjual'])

        self.btn_signup = myBtn('Sign up',self.signup)
        self.btn_back = myBtn('Back',self.back)

        self.flay = QFormLayout()
        hb = QHBoxLayout()
        hb.addWidget(self.lbl_dlg, alignment=Qt.AlignCenter)

        self.flay.addRow(hb)
        self.flay.addRow(self.lename)
        self.flay.addRow(self.lepass)
        self.flay.addRow(self.lekntk,self.lealmt)
        self.flay.addRow(self.borndt)
        self.flay.addRow(self.cbx_job)

        vb2 = twoWidLayout(self.btn_signup, self.btn_back)
        self.flay.addRow(vb2)

        self.flay.setFormAlignment(Qt.AlignVCenter)
        self.flay.setHorizontalSpacing(15)
        self.flay.setSpacing(10)
        self.setLayout(self.flay)

    def back(self):
        admin_lgn = Admin_login()
        MW.central_widget.removeWidget(MW.central_widget.currentWidget())
        MW.central_widget.addWidget(admin_lgn)

    def signup(self):
        msg = QMessageBox()
        try:
            nama = self.lename.text()
            pw = self.lepass.text()
            alm = self.lealmt.text()
            tgl = self.borndt.text()
            kon = self.lekntk.text()

            if (nama=='') or (pw=='') or (alm=='') or (kon==''):
                msg.setWindowTitle("Stop it, get some help")
                msg.setText('Field tidak boleh kosong')
                # msg.setWindowIcon()
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

            else:
                if self.cbx_job.currentText() == 'Kasir':
                    Kasir(nama, pw, alm, tgl, kon)
                elif self.cbx_job.currentText() == 'Pelayan':
                    Pelayan(nama, pw, alm, tgl, kon)
                else:
                    Penjual(nama, pw, alm, tgl, kon)

                table = TablePegawai()
                MW.central_widget.removeWidget(MW.central_widget.currentWidget())
                MW.central_widget.addWidget(table)

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("kenapa hayo?")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()

class KasirGUI(QWidget):
    def __init__(self):
        super(KasirGUI,self).__init__()

        self.lbl = myLabel('Halo, Kasir', font_jdl)

        hb = QHBoxLayout()
        t = sideMenu
        # self.flay = QFormLayout()
        hb.addWidget(self.lbl, alignment=Qt.AlignLeft)
        hb.addLayout(t)
        self.setLayout(hb)

class PelayanGUI(QWidget):
    def __init__(self):
        super(PelayanGUI,self).__init__()

        self.lbl = myLabel('Halo, Waiter', font_jdl)

        hb = QHBoxLayout()
        # self.flay = QFormLayout()
        hb.addWidget(self.lbl, alignment=Qt.AlignLeft)
        self.setLayout(hb)

class PenjualGUI(QWidget):
    def __init__(self):
        super(PenjualGUI,self).__init__()

        self.lbl = myLabel('Halo, Penjual', font_jdl)

        hb = QHBoxLayout()
        # self.flay = QFormLayout()
        hb.addWidget(self.lbl, alignment=Qt.AlignLeft)
        self.setLayout(hb)

class Login(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.lbl_wel = myLabel('SELAMAT DATANG',font_jdl)
        self.lbl_dlg = myLabel('Silahkan Login dulu!',font_dlg)

        self.lename = myLineEdit('Masukkan Username')
        self.lepass = myLineEdit('Masukkan Password')
        self.lepass.setEchoMode(QLineEdit.Password)

        self.btn_login = myBtn('Log in',self.login)
        self.btn_back = myBtn('Back',self.back)

        self.flay = QFormLayout()

        vb = QVBoxLayout()
        vb.addWidget(self.lbl_wel,alignment=Qt.AlignHCenter)
        vb.addWidget(self.lbl_dlg,alignment=Qt.AlignHCenter)
        vb.addSpacing(20)
        self.flay.addRow(vb)

        self.flay.addRow(self.lename)
        self.flay.addRow(self.lepass)

        vb2 = twoWidLayout(self.btn_login, self.btn_back)
        self.flay.addRow(vb2)

        self.flay.setFormAlignment(Qt.AlignVCenter)
        self.flay.setHorizontalSpacing(15)
        self.flay.setSpacing(10)
        self.setLayout(self.flay)

    def login(self):
        query = Akun.list_user()
        for row in query:
            # print(row.username)
            if self.lename.text() == row.username:
                if self.lepass.text() == row.password:
                    if row.job == 'Kasir':
                        ksr = KasirGUI()
                    elif row.job == 'Pelayan':
                        ksr = PelayanGUI()
                    else:
                        ksr = PenjualGUI()
                    MW.central_widget.removeWidget(MW.central_widget.currentWidget())
                    MW.central_widget.addWidget(ksr)

    def back(self):
        welcome = Welcome()
        MW.central_widget.removeWidget(MW.central_widget.currentWidget())
        MW.central_widget.addWidget(welcome)

class TablePegawai(QWidget):
    def  __init__(self):
        super(TablePegawai, self).__init__()

        self.btn_back = myBtn('Back',self.back)
        self.create_table()

        self.flay = QFormLayout()
        self.flay.addRow(self.table)
        self.flay.addRow(self.btn_back)

        self.flay.setFormAlignment(Qt.AlignLeft)
        self.flay.setHorizontalSpacing(15)
        self.flay.setSpacing(10)
        self.setLayout(self.flay)

    def create_table(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID","Username","Alamat","Tanggal Lahir","Kontak","Job"])
        self.table_content()
        self.table.setFixedSize(614,300)

    def table_content(self):
        query = Akun.list_user()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row,0,QTableWidgetItem(str(query[row].user_id)))
            self.table.setItem(row,1,QTableWidgetItem(query[row].username))
            self.table.setItem(row,2,QTableWidgetItem(query[row].alamat))
            self.table.setItem(row,3,QTableWidgetItem(query[row].tgl_lahir))
            self.table.setItem(row,4,QTableWidgetItem(query[row].kontak))
            self.table.setItem(row,5,QTableWidgetItem(query[row].job))

    def back(self):
        signupform = Signup()
        MW.central_widget.removeWidget(MW.central_widget.currentWidget())
        MW.central_widget.addWidget(signupform)


class MW(QMainWindow):
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    central_widget = QStackedWidget()

    def __init__(self):
        super(MW,self).__init__()
        self.setWindowTitle('KantinKu')
        self.resize(700,400)
        self.setContentsMargins(50,50,50,50)
        im = QImage('HOME.jpg')
        sim = im.scaled(QSize(700,400))
        pal = QPalette()
        pal.setBrush(10, QBrush(sim))
        self.setPalette(pal)

        # self.setStyleSheet('background-image: url(HOME.jpg); background-position: right}')
        self.setCentralWidget(MW.central_widget)
        welcome = Welcome()
        MW.central_widget.addWidget(welcome)

mw = MW()
mw.show()
sys.exit(MW.app.exec_())

