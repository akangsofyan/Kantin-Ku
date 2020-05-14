from TUBES.Class.Driver import *

class transaksi:
    def __init__(self,waktu, no_trans):
        self.waktu = waktu
        self.no_trans = no_trans

    def cetak_struk(self,pesn):
        print(f'\nNomor transaksi : {self.no_trans}\ntanggal : {self.waktu}'
              f'\n{ln}\npesanan\t\t jumlah\t\tsatuan\t\tharga\n{ln}')
        total = 0
        for i in pesn:
            print(f'{i[0]}\t\t\t{i[1]}\t\t{i[2]}\t\t{i[1]*i[2]}')
            total += i[1]*i[2]
        print(f'{ln}\ntotal : \t\t\t\t\t\t\t{total}\n{ln}\n')
