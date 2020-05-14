from TUBES.Class.transaksi import *
from TUBES.Model.ORM_akun import *

class Pegawai:
    def __init__(self,nama,password,alamat,tgl_lahir,kontak):
        self.nama = nama
        self.password = password
        self.alamat = alamat
        self.tgl_lahir = tgl_lahir
        self.kontak = kontak


    def getNama(self):
        return self.nama
    def __getPassword(self):
        return self.password
    def getAlamat(self):
        return self.alamat
    def getTgl_lahir(self):
        return self.tgl_lahir
    def getKontak(self):
        return self.kontak

    def setNama(self, baru):
        self.nama = baru
    def __setPassword(self, baru):
        self.password = baru
    def setAlamat(self, baru):
        self.alamat = baru
    def setTgl_lahir(self, baru):
        self.tgl_lahir = baru
    def setKontak(self, baru):
        self.kontak = baru

    def insertDB(self,job):
        dumm = Akun(self.nama, self.password ,
                    self.alamat, self.tgl_lahir,
                    self.kontak, job)


class Kasir(Pegawai):
    def __init__(self,nama,password,alamat,tgl_lahir,kontak):
        super().__init__(nama,password,alamat,tgl_lahir,kontak)
        self.insertDB('Kasir')

    def konfirmasi(self,costumer,lp):
        x,penjual = costumer.pemesanan()
        ans = input('konfir? y/n : ')
        if ans == 'y':
            penjual.dpesanan.append(costumer.no_meja);penjual.dpesanan.append(x)
            dummy = transaksi(date,lp.order)
            dummy.cetak_struk(x)
            lp.order += 1

        else:
            print('pesanan dibatalkan')

    def setMejaTerisi(self):
        pass
    def setBarang(self):
        pass
    def getBarang(self):
        pass
    def getDaftarMeja(self):
        return meja


class Pelayan(Pegawai):
    def __init__(self,nama,password,alamat,tgl_lahir,kontak):
        super().__init__(nama,password,alamat,tgl_lahir,kontak)
        self.insertDB('Pelayan')

    def setMejaKosong(self):
        pass

# tac = kasir('erja','hahaha','jl dulu','07/08/2000','0893485639')
# for i in session.query(Akun):
#     print(i.username)
