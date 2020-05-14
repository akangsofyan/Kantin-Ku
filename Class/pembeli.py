from TUBES.Class.Driver import *

class pembeli:
    def __init__(self,no_meja):
        assert 0 < no_meja <= 24, 'pilih nomor meja 1-24'
        self.no_meja = no_meja
        self.daf_pesanan = []

    def pesan(self,indx,m,qty):
        pes = []
        pes.append(m)
        pes.append(int(qty))
        pes.append(daf_pen[indx-1].find_menu(m).harga)
        return pes

    def revisiJum(self,m,qty):
        for i in self.daf_pesanan:
            if m == i[0]:
                i[1] += int(qty)

    def pemesanan(self):
        simpan = []
        for i in daf_pen: #buat nampilkan daftar warung
            print(i.nomor, i.nama_warung)
        indx = int(input('pilih wrng : '))
        daf_pen[indx-1].getMenu()
        while True: #perulangan pemesanan
            pil = input('plih menu<koma>jumlah (jika selesai masukkan "sudah") : ')
            if pil == 'sudah':
                break
            else:
                pilmenu,jum = pil.split(',')
                if pilmenu not in simpan:
                    self.daf_pesanan.append(self.pesan(indx,pilmenu,jum))
                    simpan.append(pilmenu)
                else:
                    self.revisiJum(pilmenu,jum)
                daf_pen[indx-1].find_menu(pilmenu).stok -= int(jum) #kurangi stok
                # print(self.daf_pesanan)

        return [self.daf_pesanan,daf_pen[indx-1]]
