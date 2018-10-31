import FungsiUmum
from apiclient.discovery import build

def ambil_data(judul):
    api_key = "AIzaSyAr8oDvUoXKfY5CGOcCIZi2SevZ8mgCDq8"
    service = build('books', 'v1', developerKey=api_key)
    request = service.volumes().list(source='public', q=judul, maxResults=3)
    response = request.execute()
    return response['items']

def hapus_data_tak_dipilih(data, setting_kolom, daftar_indeks):
    for i in range(len(data)-1,-1,-1):
        if data[i][setting_kolom['index']] in daftar_indeks:
            continue
        else:
            del(data[i])
    return data

def sesuaikan_nama_kolom(hasil_dari_google):
    hasil=[]
    konversi_nama_kolom = {"judul": 'title', "pengarang": 'authors', "penerbit": 'publisher'}
    for i in range(len(hasil_dari_google)):
        nilai = {}
        for nama_kolom_indo in konversi_nama_kolom.keys():
            buku_dari_google=hasil_dari_google[i]['volumeInfo']
            if konversi_nama_kolom[nama_kolom_indo] in dict(buku_dari_google).keys():
                nilai["kode"]=str(i+1)
                kolom_google=konversi_nama_kolom[nama_kolom_indo]
                nilai_hasil_google=hasil_dari_google[i]['volumeInfo'][kolom_google]
                if str(type(nilai_hasil_google))=="<type 'list'>":
                    nilai[nama_kolom_indo]= FungsiUmum.list_ke_string(nilai_hasil_google)
                else:
                    nilai[nama_kolom_indo] = nilai_hasil_google
            else:
                nilai[nama_kolom_indo]="-"
        hasil.append(nilai)
    return hasil

def lengkapi_data(data,setting_kolom):
    setting_buku= FungsiUmum.baca_setting("setting.txt")
    opsi_penyimpanan_buku=setting_buku['penyimpanan']['buku']
    buku= FungsiUmum.ambil_data(opsi_penyimpanan_buku['file'])
    index_max=int(FungsiUmum.cari_indeks_terbesar(buku,setting_kolom['index']))+1
    for i in range(len(data)):
        print "Lengkapi data dibawah ini"
        data[i][setting_kolom['index']]=index_max
        index_max+=1
        FungsiUmum.cetak_data([data[i]], "")
        for key in setting_kolom["kolom_ditambahkan"]:
            data[i][key]=raw_input(" Masukkan data "+key+" : ")
    print "x=x=x=x=x=xx=x==x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x"
    print "                     Data"
    FungsiUmum.cetak_data(data,"")
    simpan=raw_input("Simpan data ? (y/t)")
    if simpan=="y":
        FungsiUmum.simpan_data(opsi_penyimpanan_buku, buku + data)

def tampilan_utama():
    daftar_kolom_buku= FungsiUmum.baca_setting("setting.txt")['key']['buku']['keyTampil']
    judul=raw_input("Masukkan Judul : ")
    print "Loading ..."
    hasil_dari_google=list(ambil_data(judul))
    print "Hasil pengambilan data"
    hasil_pengambilan=sesuaikan_nama_kolom(hasil_dari_google)
    FungsiUmum.cetak_data(hasil_pengambilan,daftar_kolom_buku)
    kolom_ditambahkan={"kolom_ditambahkan":['status','nomer_rak','kategori'],"index":"kode"}
    kode_buku_dipilih=raw_input("Masukkan kode buku yang ingin anda masukkan ke data : ").split(",")
    data_dipilih=hapus_data_tak_dipilih(hasil_pengambilan, kolom_ditambahkan, kode_buku_dipilih)
    lengkapi_data(data_dipilih,kolom_ditambahkan)

