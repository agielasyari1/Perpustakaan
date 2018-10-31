import FungsiUmum
import Menu
import datetime

#Digunakan untuk menamipilkan menu khusus untuk peminjaman buku
def tampilan_menu(kolom_yg_digunakan, opsi_penyimpanan ):
    data_peminjaman= FungsiUmum.ambil_data(opsi_penyimpanan['file'])
    print "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x"
    print "        Selmat Datang di Perpustakaan UTM"
    print "Menu : 1. Tampilkan Data Peminjaman 2. Input Peminjaman 3. Kembalikan Buku 4.Hapus data \n 5.Cari Data Peminjaman  6.Ubah Data Peminjaman 7. Cetak surat Peringatan"
    menu= raw_input("Pilih Menu : ")
    if menu=="1":
        FungsiUmum.cetak_data(data_peminjaman, "")
    elif menu=="2":
        masukkan_peminjaman(opsi_penyimpanan)
    elif menu == "3":
        kembalikan_buku(opsi_penyimpanan)
    elif menu=="5":
        opsi_operasi = {'operasi': "cari", "opsi": ""}
        pilihan_operasi = raw_input("Pilihan pencarian [ Persis/ Mirip/ > / < ] : ").lower()
        opsi_operasi['opsi']=pilihan_operasi
        Menu.menu_cari_hapus(opsi_operasi, data_peminjaman, kolom_yg_digunakan['keyCari'], "")
    elif menu == "4":
        opsi_operasi = {'operasi': "hapus", "opsi": ""}
        Menu.menu_cari_hapus(opsi_operasi, data_peminjaman, kolom_yg_digunakan['keyHapus'], opsi_penyimpanan)
    elif menu=="6":
        Menu.menu_ubah(data_peminjaman, kolom_yg_digunakan['keyEdit'], opsi_penyimpanan)
    elif menu=="7" :
        file_anggota = FungsiUmum.baca_setting("setting.txt")["penyimpanan"]["anggota"]["file"]
        data_anggota = FungsiUmum.ambil_data(file_anggota)
        data_peminjaman_telat=cari_peminjaman_telat(data_peminjaman,14)
        cetak_surat_peringatan(data_peminjaman_telat,data_anggota)
    else:
        Menu.cetak_pesan_error()

#mencari daftar peminjaman yang telat
def cari_peminjaman_telat(data_peminjaman,hari_telat):
    tgl_kembali_telat = datetime.datetime.now() - datetime.timedelta(days=hari_telat)
    kriteria_pencarian = {"kolom": "tanggal_harus_kembali", "nilai": tgl_kembali_telat}
    data_peminjaman_telat = FungsiUmum.cari(kriteria_pencarian, data_peminjaman, "<")
    kriteria_pencarian = {"kolom": "status", "nilai": "pinjam"}
    data_peminjaman_telat = FungsiUmum.cari(kriteria_pencarian, data_peminjaman_telat, "persis")
    return data_peminjaman_telat

#cetak surat peringatan
def cetak_surat_peringatan(data_peminjaman_telat,data_anggota):
    for i in range(len(data_anggota)):
        kriteria_pencarian = {"kolom": "np", "nilai": data_anggota[i]['np']}
        anggota_telat = len(FungsiUmum.cari(kriteria_pencarian, data_peminjaman_telat, "persis"))>0
        if anggota_telat:
            isi_surat= "Dengan ini kami memberitahukan bahwa peminjaman dengan data dibawah ini : \n"
            isi_surat += "No Anggota\t: " + data_anggota[i]['np']+"\n"
            isi_surat+="Nama\t\t: "+data_anggota[i]['nama']+"\n"
            isi_surat += "Alamat\t\t: " + data_anggota[i]['alamat']+"\n"
            isi_surat += "\nHingga saat ini belum mengembalikan buku\n"
            kolom=["kode","judul","tanggal_pinjam","tanggal_harus_kembali"]
            isi_surat+=str(FungsiUmum.data_ke_string(data_peminjaman_telat,kolom))
            isi_surat+= "\nKami harap proses pengembalian buku segera dilakukan\n"
            isi_surat += "\nTerima kasih"
            nama_file="peringatan_"+data_anggota[i]['nama']+"_"+str(datetime.datetime.now().date())+".txt"
            opsi_penyimpanan={"file":nama_file,"opsi":"w"}
            FungsiUmum.simpan_teks_ke_file(opsi_penyimpanan,isi_surat)
            print "File "+nama_file+" berhasil dibuat"
#Digunakan untuk memproses peminjaman buku
def masukkan_peminjaman(opsi_penyimpanan):
    data_baru=[]
    setting= FungsiUmum.baca_setting("setting.txt")
    file_anggota=setting['penyimpanan']['anggota']['file']
    file_buku=setting['penyimpanan']['buku']['file']
    file_peminjaman=opsi_penyimpanan['file']
    data_anggota = FungsiUmum.ambil_data(file_anggota)
    data_buku= FungsiUmum.ambil_data(file_buku)
    data_peminjaman = FungsiUmum.ambil_data(file_peminjaman)
    np = raw_input("Masukkan NP : ")
    kode_buku = raw_input("Masukkan kode buku : ")
    daftar_kode_buku_dipinjam=str(kode_buku).split(",")
    index = int(FungsiUmum.cari_indeks_terbesar(data_peminjaman, "id_peminjaman"))
    index += 1
    kriteria_pencarian_anggota={"kolom":"np","nilai":np}
    anggota=FungsiUmum.cari(kriteria_pencarian_anggota,data_anggota, "persis")
    NP_ditemukan = len(anggota)==1
    daftar_peminjaman_anggota=FungsiUmum.cari(kriteria_pencarian_anggota, data_peminjaman, "persis")
    status_peminjaman = {"kolom": "status", "nilai": "pinjam"}
    tak_meminjam = len(FungsiUmum.cari(status_peminjaman, daftar_peminjaman_anggota, "persis")) == 0

    for i in range(len(daftar_kode_buku_dipinjam)):
        buku_tak_dipinjam = False
        buku_boleh_dipinjam = False
        kriteria_pencarian_buku = {"kolom": "kode", "nilai": daftar_kode_buku_dipinjam[i]}
        buku = FungsiUmum.cari(kriteria_pencarian_buku,data_buku,"persis")
        ada_buku=len(buku)>0

        if ada_buku:
            buku_boleh_dipinjam = buku[0]['status'] == "pinjam"
            kriteria_pencarian_buku = {"kolom": "kode_buku", "nilai": daftar_kode_buku_dipinjam[i]}
            buku_di_peminjaman = FungsiUmum.cari(kriteria_pencarian_buku, data_peminjaman, "persis")
            kriteria_pencarian_buku = {"kolom": "status", "nilai": "pinjam"}
            buku_di_peminjaman = FungsiUmum.cari(kriteria_pencarian_buku, buku_di_peminjaman, "persis")
            buku_tak_dipinjam=len(buku_di_peminjaman)==0

        if NP_ditemukan  and tak_meminjam and ada_buku and buku_tak_dipinjam and buku_boleh_dipinjam :
            tanggal_pinjam = datetime.datetime.now().date()
            tanggal_harus_kembali = datetime.datetime.now().date()+datetime.timedelta(days=5)
            data_baru.append({
            'id_peminjaman': str(index),
            'np': np,
            'nama' : anggota[0]['nama'],
            'kode_buku': daftar_kode_buku_dipinjam[i],
            'judul': buku[0]['judul'],
            'tanggal_pinjam': str(tanggal_pinjam),
            'tanggal_harus_kembali': str(tanggal_harus_kembali),
            'status': "pinjam",
                'denda': 0
        })
        else:
            print "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x="
            print "      MAAF DATA TIDAK DAPAT DIMASUKKAN !!!!!"
            print "  Pastikan Semua data dibawah ini bernilai True"
            print "------------------Status---------------------------"
            print "Nomer Anggota Perpustakaan terdaftar ? ", NP_ditemukan
            print "Tidak ada tanggungan pinjaman ? ", tak_meminjam
            print  "Buku ada dalam daftar ? ",ada_buku
            print  "Buku sedang tak dipinjam ? ",buku_tak_dipinjam
            print "Buku boleh dipinjam ? ", buku_boleh_dipinjam
            print "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x="

    print "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x="
    print "      DATA YANG DIMASUKKAN"
    FungsiUmum.cetak_data(data_baru, "")
    simpan = raw_input("Simpan data yang dimasukkan ? (y/t)")
    if simpan == "y":
        data_peminjaman += data_baru
        FungsiUmum.simpan_data(opsi_penyimpanan, data_peminjaman)

#Digunakan untuk memproses pengembalian buku
def kembalikan_buku(opsi_penyimpanan):
    alamat_file=opsi_penyimpanan['file']
    data_peminjaman= FungsiUmum.ambil_data(alamat_file)
    np_peminjam = raw_input("Masukkan Nomer Anggota Peminjam : ")
    daftar_buku_dipinjam = raw_input("Masukkan kode buku yang dikembalikan : ")
    daftar_buku_dipinjam=daftar_buku_dipinjam.split(",")
    total_denda = 0
    print "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x"
    print "               PEMINJAMAN YANG  DIKEMBALIKAN"
    print ""
    for i in range(len(daftar_buku_dipinjam)):

        for j in range(len(data_peminjaman)):
            np_peminjam_dalam_data=data_peminjaman[j]["np"]
            kode_buku_dalam_data=data_peminjaman[j]["kode_buku"]
            kode_buku_dicari=daftar_buku_dipinjam[i]

            np_peminjam_ketemu=np_peminjam_dalam_data==np_peminjam
            kode_buku_ketemu=kode_buku_dalam_data==kode_buku_dicari
            buku_belum_dikembalikan=data_peminjaman[j]["status"]=="pinjam"

            if np_peminjam_ketemu and kode_buku_ketemu and buku_belum_dikembalikan:
                data_peminjaman[j]["status"]="dikembalikan"
                tgl_string=data_peminjaman[j]['tanggal_harus_kembali']
                tanggal_harus_kembali = datetime.datetime.strptime(tgl_string, '%Y-%m-%d')
                tanggal_sekarang=datetime.datetime.now()
                data_peminjaman[j]["tanggal_kembali"] = str(tanggal_sekarang.date())
                telat =tanggal_harus_kembali<tanggal_sekarang
                if telat :
                    jumlah_hari_telat=(tanggal_sekarang-tanggal_harus_kembali ).days
                    denda=jumlah_hari_telat*2000
                    total_denda+=denda
                    data_peminjaman[j]["status"] = "dikembalikan"
                    data_peminjaman[j]["denda"]=denda
                FungsiUmum.cetak_data([data_peminjaman[j]],"")

    simpan=raw_input("Simpan data peminjaman (y/t) ").lower()
    if simpan=="y":
        FungsiUmum.simpan_data(opsi_penyimpanan, data_peminjaman)
        if total_denda>0:
            print "Anda telat mengembalikan buku selama ", jumlah_hari_telat," hari"
            print "Total Denda Anda adalah : ",total_denda


