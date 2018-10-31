import FungsiUmum

#Menampilkan menu utama
def menu_utama(pilihan, kolom_yg_digunakan,opsi_penyimpanan):

    print "-------------------------------------------------------------------------------"
    print ""
    print "Menu : 1. Tampilkan Data "+pilihan+" 2. Tambah "+pilihan+" 3. Edit "+pilihan+" 4. Hapus "+pilihan+" 5.Cari "+pilihan
    menu= raw_input("Pilih Menu : ")
    nama_file_penyimpanan=opsi_penyimpanan['file']
    data= FungsiUmum.ambil_data(nama_file_penyimpanan)
    if menu=="1":
        data= FungsiUmum.ambil_data(opsi_penyimpanan['file'])
        FungsiUmum.cetak_data(data, kolom_yg_digunakan['keyTampil'])
    elif menu=="2":
        input_data(data,kolom_yg_digunakan, opsi_penyimpanan)
    elif menu == "3":
        menu_ubah(data,kolom_yg_digunakan['keyEdit'], opsi_penyimpanan)
    elif menu == "4":
        pilihan_operasi={'operasi': "hapus","opsi":""}
        menu_cari_hapus(pilihan_operasi, data, kolom_yg_digunakan['keyHapus'], opsi_penyimpanan)
    elif menu=="5":
        pilihan_operasi = {'operasi': "cari", "opsi": ""}
        pilihan_operasi['opsi']= raw_input("Pilihan pencarian [ Persis/ Mirip/ > / <  ] : ").lower()
        menu_cari_hapus(pilihan_operasi, data, kolom_yg_digunakan['keyCari'], "")
    else:
        cetak_pesan_error()


#Digunakan untuk mencari data, semua data yang bersifat sederhana dapat menggunakan fungsi ini
def menu_cari_hapus(pilihan_operasi, data, kolom_yg_digunakan, opsi_penyimpanan):
    jenis_operasi=str(pilihan_operasi['operasi'])
    kolom_menu=str(kolom_yg_digunakan).replace("[u", "[")
    kolom_menu=kolom_menu.replace(", u'"," ,'")
    kolom=raw_input(jenis_operasi.capitalize() + " data  berdasarkan  " + kolom_menu + " : ")
    kolom_benar = kolom in kolom_yg_digunakan
    if kolom_benar:
        nilai = raw_input("Masukkan "+kolom+" yang ingin di"+jenis_operasi+" : ")
        if str(pilihan_operasi['operasi']).lower()== "hapus" :
            kriteria_hapus={"kolom":kolom,"nilai":nilai}
            FungsiUmum.hapus_data( data, kriteria_hapus,opsi_penyimpanan)
        else:
            kriteria_cari={"kolom":kolom,"nilai":nilai}
            opsi_pencarian=pilihan_operasi['opsi']
            data_yg_ditemukan=FungsiUmum.cari(kriteria_cari, data, opsi_pencarian)
            print FungsiUmum.cetak_data(data_yg_ditemukan, kolom_yg_digunakan)
    else:
        cetak_pesan_error()

#Digunakan untuk mengubahn data, semua data yang bersifat sederhana dapat menggunakan fungsi ini
def menu_ubah(data, kolom_yg_digunakan, opsi_penyimpanan):
    pilihan_edit=str(kolom_yg_digunakan).replace(", u'", ", '")
    pilihan_edit=pilihan_edit.replace("[u","[")
    kolom_yg_diubah=raw_input("Edit berdasarkan : "+pilihan_edit+" : ")
    kolom_benar = kolom_yg_diubah in kolom_yg_digunakan
    if kolom_benar:
        nilai = raw_input("Ubah data yang memiliki "+kolom_yg_diubah+" :")
        kriteria_edit={"kolom" : kolom_yg_diubah,
                      "nilai" : nilai }

        FungsiUmum.ubah_data(kolom_yg_digunakan, kriteria_edit, data, opsi_penyimpanan)

#Digunakan untuk memasukkan data, semua data yang bersifat sederhana dapat menggunakan fungsi ini
def input_data(data, kolom_yg_digunakan, opsi_penyimpanan):
    kolom_input=kolom_yg_digunakan['keyInput']
    jumlah=input("Jumlah data yang ingin dimasukkan : ")
    data_baru=[]
    for i in range(jumlah):
        nilai_yg_diinput={}
        jumlah_kolom=len(kolom_input)
        for j in range (jumlah_kolom):
            nama_kolom=kolom_input[j]
            nilai_yg_diinput[nama_kolom]=raw_input("Masukkan "+nama_kolom+" : ")
            kolom_auto=kolom_yg_digunakan['auto']
            jumlah_kolom=len(kolom_auto)
        for j in range(jumlah_kolom):
            maximum_index=int(FungsiUmum.cari_indeks_terbesar(data, kolom_auto[j]))
            nilai_yg_diinput[kolom_auto[j]]=maximum_index+1
        data_baru.append(nilai_yg_diinput)
    print "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x="
    print  "                         DATA YANG DIMASUKKAN        "
    FungsiUmum.cetak_data(data_baru,list(kolom_input))
    simpan=raw_input("Simpan data yang dimasukkan (y/t) : ").lower()
    if simpan=="y":
        data+=data_baru
        FungsiUmum.simpan_data(opsi_penyimpanan, data)

def cetak_pesan_error ():
    print "Maaf pilihan tidak dikenali ..."






