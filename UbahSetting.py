import FungsiUmum
import OperasiFile

opsi_penyimpanan2 = {'file': "setting.txt",
                     'opsi': "w"}

key_anggota = ["np", "nama", "alamat", "prodi"]
key1 = {
    'keyInput': key_anggota,
    'keyEdit': key_anggota,
    'keyHapus': key_anggota,
    'keyCari': key_anggota,
    'keyTampil': key_anggota,
    'auto': []}

keyBuku = ["kode", "judul", "penerbit", "pengarang", "kategori","status","nomer_rak"]
keyInputBuku=["judul", "penerbit", "pengarang","kategori", "status","nomer_rak"]
key2 = {'keyInput':keyInputBuku ,
        'keyEdit': keyBuku,
        'keyHapus': keyBuku,
        'keyCari': keyBuku,
        'keyTampil': keyBuku,
        'auto': ['kode']}

key_peminjaman = ['id_peminjaman', 'np', 'nama', 'kode_buku', 'judul', 'tanggal_pinjam', 'tanggal_harus_kembali',
                  'status', 'denda']
key_tampil = ['id_peminjaman', 'np', 'nama', 'kode_buku', 'judul', 'tanggal_pinjam', 'tanggal_harus_kembali','tanggal_kembali',
                  'status', 'denda']
key3 = {'keyInput': ["nim", "kode_buku"],
        'keyEdit': key_peminjaman,
        'keyHapus': key_peminjaman,
        'keyCari': key_peminjaman,
        'keyTampil': key_tampil,
        'auto': ['id_peminjaman']}


setting_key = {"anggota": key1,
               "buku" :key2,
               "peminjaman" :key3}
setting_save= {"anggota": {'file': "dataAnggota.txt",
                            'opsi': "w"},
                "buku": {'file': "dataBuku.txt",
                         'opsi': "w"},
                "peminjaman": {'file': "dataPeminjaman.txt",
                               'opsi': "w"}}
setting = {"key": setting_key,
           "penyimpanan": setting_save}
teks_anggota = FungsiUmum.ubah_list_dictionary_ke_teks(setting)
FungsiUmum.simpan_teks_ke_file(opsi_penyimpanan2, teks_anggota)


