import json
import datetime

import os.path
###########Fungsi Fungsi untuk baca dan simpan file###################
#untuk membaca sebuah isi file teks
def baca_file_teks(alamatFile):
    hasil=""
    file_ada=os.path.exists(alamatFile)
    file_berisi=os.stat(alamatFile).st_size > 0
    if  file_ada and file_berisi:
        with open(alamatFile) as isiPerbaris:
            hasil = isiPerbaris.read()
    return hasil
#untuk menyimpan teks ke dalam file
def simpan_teks_ke_file(opsi_penyimpanan, teks):
    text_file = open(opsi_penyimpanan['file'], opsi_penyimpanan["opsi"])
    text_file.write(teks)
    text_file.close()


#untuk membaca file settings.txt
def baca_setting(alamat_file):
    setting_bentuk_teks = baca_file_teks(alamat_file)
    setting_bentuk_dictionary = ubah_teks_ke_list_dictionary(setting_bentuk_teks)
    return setting_bentuk_dictionary


# Digunakan untuk menyimpan data list dictionary ke file
def simpan_data(opsi_penyimpanan, data):
    string_dari_data = ubah_list_dictionary_ke_teks(data)
    simpan_teks_ke_file(opsi_penyimpanan, string_dari_data)
    print "Data Berhasil Disimpan ke ",str(opsi_penyimpanan['file'])

# Digunakan untuk meneghasilkan data list dictionary dari sebuah file
def ambil_data(alamatFile):
    teks = baca_file_teks(alamatFile)
    hasil = ubah_teks_ke_list_dictionary(teks)
    return hasil

###########Fungsi fungsi melakukan koversi data###################
#Menhasilkan string dari sebuah list
def list_ke_string(data):
    hasil=""
    for i in range(len(data)):
        if i!=0:
            hasil+=", "
        hasil+=data[i]
    return hasil

#untuk mengubah teks dari sebuah file menjadi dictionary
def ubah_teks_ke_list_dictionary (teks):
    hasil = json.loads(teks)
    return hasil

#Mengubah Dictionary ke String
def ubah_list_dictionary_ke_teks(data):
    return json.dumps(data)



################Fungsi fungsi untuk operasi dalam data###############################
#Digunakan menghitung index terbesar, biasanya digunakan pada data yang autoincrement
def cari_indeks_terbesar(data, kolom):
    terbesar=0
    for nilai in data:
        if terbesar<int(nilai[kolom]):
            terbesar=int(nilai[kolom])
    return terbesar
#Digunakan untuk mengubah data
def ubah_data (daftar_kolom_diubah, kriteria_edit, data, opsi_penyimpanan):
    data_yag_terdampak=cari(kriteria_edit,data,"persis")
    nilai_baru={}
    for kolom_diubah in daftar_kolom_diubah:
        nilai_baru[kolom_diubah] = raw_input("Masukkan nilai " + str(kolom_diubah) + " baru : ")
    for i in range(len(data)):
        kolom_dicari=str(kriteria_edit['kolom']).lower()
        nilai_dicari=str(kriteria_edit['nilai']).lower()
        ketemu=str(data[i][kolom_dicari]).lower()==nilai_dicari
        if ketemu :
            for kolom_diubah in daftar_kolom_diubah:
                nilai_baru_tdk_kosong=nilai_baru[kolom_diubah]!=""
                if nilai_baru_tdk_kosong:
                    data[i][kolom_diubah]=nilai_baru[kolom_diubah]

    print "x=x=x=x=x=x=x=x=x=x=x PERINGATAN x=x=x=x=x=x=x=x=x=x=x=x=x=x"
    print "Perubahan akan dilakukan pada data berikut "
    cetak_data(data_yag_terdampak,daftar_kolom_diubah)

    simpan=raw_input("Simpan perubahan ? (y/t) : ")
    if simpan=="y":
        simpan_data(opsi_penyimpanan, data)
#Digunakan untuk memenghapus data
def hapus_data( data,kriteria_hapus, opsi_penyimpanan):
    data_terdampak=cari(kriteria_hapus,data,"persis")
    banyak_data=len(data)
    if banyak_data>0:
        print "x=x=x=x=x=x=x=x=x=x=x PERINGATAN x=x=x=x=x=x=x=x=x=x=x=x=x=x"
        print "Data yang akan dihapus adalah berikut "
        cetak_data(data_terdampak,"")
        hapus=raw_input("Hapus data ( y/t ) : ")
        if hapus=="y":
            kolom_dicari=str(kriteria_hapus['kolom']).lower()
            nilai_dicari=str(kriteria_hapus['nilai']).lower()
            for i in range (len(data)-1,-1,-1):
                nilai_dalam_data=str(data[i][kolom_dicari]).lower()
                ketemu=nilai_dicari == nilai_dalam_data
                if ketemu :
                    del(data[i])
                    print "Data berhasil dihapus..."
            simpan_data(opsi_penyimpanan, data)

#digunakan untuk mencari data
def cari(kriteria_cari, data, opsi_pencarian):
    hasil=[]
    kolom_dicari=kriteria_cari['kolom']
    nilai_dicari=kriteria_cari['nilai']
    for dataSatuan in data:
        nilai_dalam_data = str(dataSatuan[kolom_dicari])
        if opsi_pencarian== "mirip":
            ketemu=str(nilai_dicari).lower() in nilai_dalam_data.lower()
            if ketemu:
                hasil.append(dataSatuan)
        elif opsi_pencarian== "persis":
            ketemu=str(nilai_dicari).lower() == nilai_dalam_data.lower()
            if ketemu:
                hasil.append(dataSatuan)
        elif opsi_pencarian == "<":
            if str(type(nilai_dicari))=="<type 'datetime.datetime'>":
                ketemu = datetime.datetime.strptime(nilai_dalam_data, '%Y-%m-%d') < nilai_dicari
            else:
                ketemu= float(nilai_dalam_data) < float(nilai_dicari)
            if ketemu:
                hasil.append(dataSatuan)
        elif opsi_pencarian == ">":

            if str(type(nilai_dicari)) == "<type 'datetime.datetime'>":
                ketemu =  datetime.datetime.strptime(nilai_dalam_data, '%Y-%m-%d') > nilai_dicari
            else:
                ketemu = float(nilai_dalam_data) > float(nilai_dicari)
            if ketemu:
                hasil.append(dataSatuan)
    return hasil

#Digunakan untuk menncetak isi sebuah data
def cetak_data(data, kolom):
    print data_ke_string(data,kolom)

def data_ke_string(data, kolom):
  hasil = ""
  for i in range(len(data)):

      if kolom == "":
          kolom_data = dict(data[i]).keys()
      else:
          kolom_data = kolom
      hasil+= "\n-----------------------------------------------------------------\n"
      for kolom_satuan in kolom_data:
          if kolom_satuan in dict(data[i]).keys():
              nilai = str(data[i][str(kolom_satuan)])
              hasil+= str(kolom_satuan).capitalize()+ ":"+nilai.capitalize()+"\n"
  return hasil
