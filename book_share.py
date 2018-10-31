import httplib
import json
import FungsiUmum


def ambil_data(judul):
    conn = httplib.HTTPSConnection("api.bookshare.org")
    key="AIzaSyAr8oDvUoXKfY5CGOcCIZi2SevZ8mgCDq8"
    url="/book/search/title/"+judul+"/limit/10/format/json?api_key="+key
    conn.request("GET", url)
    res = conn.getresponse()
    data = json.loads(res.read())
    return data['bookshare']['book']['list']['result']

def tampilan_utama():
    judul=raw_input("Masukkan judul : ")
    print "Loading ..."
    hasil=list(ambil_data(judul))
    setting= FungsiUmum.baca_setting("setting.txt")
    data_awal=list(FungsiUmum.ambil_data(setting['penyimpanan']['buku']['file']))
    print "Hasil pengambilan data"
    datax=[]
    for a in range(len(hasil)):
        judul=hasil[a]['title']
        cek =list(FungsiUmum.cari("judul",judul,data_awal,"persis"))
        blm_ada=len(cek)==0
        if blm_ada:
            pengarang=list_ke_string(hasil[a]['author'])
            index= FungsiUmum.cari_indeks_terbesar(data_awal,'kode')
            index+=1
            data_baru={"kode":index,
                              "judul":hasil[a]['title'],
                                "penerbit":hasil[a]['publisher'],
                                "kategori":"sains",
                              "pengarang":pengarang,
                                "status":"ada"}
            datax.append(data_baru)
    FungsiUmum.cetak_data(data_awal+datax,setting['key']['buku']['keyTampil'])
    simpan=raw_input("Simpan data y/t : ")
    if simpan=="y":
        FungsiUmum.simpan_data(setting['penyimpanan']['buku'], data_awal)

tampilan_utama()