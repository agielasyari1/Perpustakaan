from cryptography.fernet import Fernet
encKey="LTSZF5Vc1rQ9MI7_ErQYxDNOyt2vs_Cu5e37zaQkDZQ="

def enkripsi(teks_biasa, kunci_enkripsi):
    pengekripsi = Fernet(kunci_enkripsi)
    hasil_enkripsi = pengekripsi.encrypt(str(teks_biasa))
    return hasil_enkripsi
def dekripsi(teks, kunci_dekripsi):
    pendekripsi = Fernet(kunci_dekripsi)
    teks_biasa = pendekripsi.decrypt(str(teks))
    return teks_biasa

