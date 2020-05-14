from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from TUBES.View.Asset.Font import *
from TUBES.View.reuse.my_customize import myBtn,myLineEdit,myLabel,twoWidLayout
from TUBES.Class.pegawai import Kasir,Pelayan
from TUBES.Class.penjual import Penjual


class Signup(QWidget):
    def __init__(self,nama):
        super(Signup,self).__init__()
        self.nama = nama

        self.lbl_dlg = myLabel('Silahkan isi data diri calon pegawai!',font_dlg)
        self.lename = myLineEdit('Masukkan Username')
        self.lepass = myLineEdit('Masukkan Password')
        self.lepass.setEchoMode(QLineEdit.Password)
        self.lealmt = myLineEdit('Masukkan Alamat')
        self.borndt = QDateEdit()
        self.lekntk = myLineEdit('Masukkan Kontak')
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
        self.setLayout(self.flay)

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
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()

            else:
                if self.cbx_job.currentText() == 'Kasir':
                    Kasir(nama, pw, alm, tgl, kon)
                elif self.cbx_job.currentText() == 'Pelayan':
                    Pelayan(nama, pw, alm, tgl, kon)
                else:
                    Penjual(nama, pw, alm, tgl, kon)

                from TUBES.View.adminGUI import AdminGUI
                table = AdminGUI(self.nama)
                self.parent().setCentralWidget(table)

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("kenapa hayo?")
            msg.setWindowTitle("Gagal")
            msg.exec_()

    def back(self):
        from TUBES.View.admin_login import Admin_login
        admin_lgn = Admin_login()
        self.parent().setCentralWidget(admin_lgn)
