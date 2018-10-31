import Menu
import Peminjaman
import FungsiUmum
import google_book


nama_file_penyimpanan={}
kolom_yg_digunakan={}
menu_yang_disediakan=["anggota", "buku", "peminjaman", "googlebook","keluar"]
while True:
    print "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x"
    print "        Selmat Datang di Perpustakaan UTM"
    print ""
    pilihan_menu=raw_input("Masukkan Pilihan Menu " + str(menu_yang_disediakan).capitalize() + " : ").lower()
    if pilihan_menu in menu_yang_disediakan:
       if pilihan_menu == "googlebook":
        google_book.tampilan_utama()
       else:
            setting_aplikasi = FungsiUmum.baca_setting("setting.txt")
            kolom_yg_digunakan = setting_aplikasi['key'][pilihan_menu]
            nama_file_penyimpanan = setting_aplikasi['penyimpanan'][pilihan_menu]

            if pilihan_menu== "anggota" or pilihan_menu== "buku":
                Menu.menu_utama(pilihan_menu, kolom_yg_digunakan, nama_file_penyimpanan)
            elif pilihan_menu== "peminjaman":
                Peminjaman.tampilan_menu(kolom_yg_digunakan, nama_file_penyimpanan)
            elif pilihan_menu=="googlebook":
                google_book.tampilan_utama()
            elif pilihan_menu == "keluar":
                break;
    else:
        Menu.cetak_pesan_error()




