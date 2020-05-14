from TUBES.Class.pegawai import Pegawai
from TUBES.Model.ORM_akun import *

class menu:
    def __init__(self,id_pen,nama_menu,harga,stok):
        self.id_pen = id_pen
        self.nama_menu = nama_menu
        self.harga = harga
        self.stok = stok
        self.stokAwal = stok
        self.insertMenu()

    def insertMenu(self):
        dumm = Menu(id_penjual=self.id_pen,
                    nama_menu=self.nama_menu,
                    harga_menu=self.harga,
                    stok=self.stok)
        session.add(dumm)
        session.commit()


    def __str__(self): #tampilan print
        return self.nama_menu + '\t\t\t' + str(self.harga) + '\t\t' + str(self.stok)


class Penjual(Pegawai):
    def __init__(self,nama,password,alamat,tgl_lahir,kontak):
        super().__init__(nama,password,alamat,tgl_lahir,kontak)
        self.insertDB('Penjual')
        # self.dmenu = dmenu
        # self.dpesanan = dpesanan
        # try:
        #     self.insertDB('Penjual')
        # except:
        #     pass

    def getMenu(self):
        print('nama menu\t\tharga\t\tstok')
        # for i in self.dmenu:
        #     print(i)

    def tambahMenu(self,id):
        id_pen = id
        nama = input()
        harga = int(input())
        stok = int(input())
        menu(id_pen,nama,harga,stok)

# p1=None
# le='nama'
#
# #login berhsil
# id=4
# for user in session.query(Akun):
#     if user.user_id==id:
#         p1 = Penjual(user.username, user.password, user.alamat, user.tgl_lahir, user.kontak)
#
# p1.tambahMenu(id)
# p1.tambahMenu()
    # def find_menu(self,target):
        # for i in self.dmenu :
        #     if target == i.nama_menu:
        #         return i


class notifikasi:
    def setDering(self):
        pass

# penjual1 = penjual('Geprek Mania', '9876', 'jl kucing', '02/12/1993','082223384576')
