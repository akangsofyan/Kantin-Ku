from TUBES.Class.Driver import *

class penghasilan:
    def __init__(self, tanggal, order):
        self.tanggal = tanggal
        self.order = order

    def getLaporanKeuangan(self,id):
        for i in daf_pen:
            # print(type(i.nomor))
            if id == i.nomor:
                print(f'\n---------------Laporan keuangan {i.nama_warung}---------------')
                total = 0
                for i in i.dmenu:
                    terjual = i.stokAwal-i.stok
                    print(f'{i.nama_menu}\t\tstok terjual = stok awal - stok sisa\n\
                         = {i.stokAwal} - {i.stok} = {terjual} x {i.harga} = {terjual*i.harga}\n')
                    total += terjual*i.harga
                print(f'\t\t\ttotal penghasilan tanggal {self.tanggal} = Rp.{total}')
