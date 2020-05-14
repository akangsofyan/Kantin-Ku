# pmbeli datang > kasir memberikan daftar meja kosong > pembeli pilih nomor meja (meja-=1)
# daftar warung tampil dan pilih warung > daftar menu dan pilih menu > bisa kembali atau konfir pemesanan
# setelah konfir pop up muncul di penjual > pesanan dibuat dan diantar >  meja dibersihkan pelayan (meja +=1)
import datetime
import time
import sys



daf_pen = []
meja = 24
order = 0;ln='------------------------------------------'
date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y'))
# print(date)




# demo#
#### guistart demo ####


#### pegawai demo ####
# pegawai1 = kasir('budi', 'kp.timur','30 jan 1999','082233445566')
#
# print(pegawai1.getNama())
# print(pegawai1.getAlamat())
# print(pegawai1.getTgl_lahir())
# print(pegawai1.getKontak())
#
# print('\ndiupdate dulu..\n')
# pegawai1.setAlamat('jl kenangan')
# pegawai1.setKontak('081234567891')
#
# print(pegawai1.getNama())
# print(pegawai1.getAlamat())
# print(pegawai1.getTgl_lahir())
# print(pegawai1.getKontak())
#
# print(pegawai1.getDaftarMeja())


### demo pemesanan ####
# n1 = penjual('1','mas gus',[menu(1,'geprek',15000,20),menu(1,'nasgor',12000,20),menu(1,'tahuu',5000,20)],[])
# n2 = penjual('2','mba boy',[menu(2,'mie gas',14000,20),menu(2,'salome',5000,20),menu(2,'tempe',3000,20)],[])
# n3 = penjual('3','dek dor',[menu(3,'wedank',7000,20),menu(3,'es the',4000,20),menu(3,'jeruk',5000,20)],[])



# masmsa = kasir('andi','jljl','12 apr 1995','08234242442')
# pm = pembeli(12)
# pme = pembeli(1)
#
# lp1 = penghasilan(date,0)
# masmsa.konfirmasi(pm,lp1)
# masmsa.konfirmasi(pme,lp1)
#
# ### demo laporan #### (require demo pemesanan)
# lp1.getLaporanKeuangan('2')
#
# @Testdecorator
# def antrianPesanan(warung):
#     for i in range(0,len(warung.dpesanan),2):
#         print(warung.dpesanan[i],end='')
#         for j in warung.dpesanan[i+1]:
#             print(f' \t\t\t {j[0]}  \t\t\t {j[1]}')
#         print()
#
#
#
# antrianPesanan(n2)
#
# db.remove(userid)
# for row in db.fetch():
#     print(' '.join(list(map(str,(row)))))
